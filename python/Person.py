from bs4 import BeautifulSoup
import re
import bleach
import os

# Declare regex

reg_ansedel = re.compile("ansedel", re.IGNORECASE | re.UNICODE)
reg_name = re.compile("[\w-]+", re.IGNORECASE | re.UNICODE)
date_str = "[\sa-öA-Ö]*([\d-]*)"
loc_str = "[\w\s-]*\s+i\s+([a-öA-Ö,\s]*)"
rem_letters = "[0-9\s\.-]*([a-öA-Ö\s,]*)"
reg_date = re.compile(date_str, re.IGNORECASE | re.UNICODE)
reg_loc = re.compile(loc_str, re.IGNORECASE | re.UNICODE)
reg_birth_date = re.compile("Född{}".format(date_str), re.IGNORECASE | re.UNICODE)
reg_birth_loc = re.compile("Född{}".format(loc_str), re.IGNORECASE | re.UNICODE)
reg_birth_remaining = re.compile("Född {}".format(rem_letters), re.IGNORECASE | re.UNICODE)
reg_death_date = re.compile("Död {}".format(date_str), re.IGNORECASE | re.UNICODE)
reg_death_loc = re.compile("Död {}".format(loc_str), re.IGNORECASE | re.UNICODE)
reg_death_remaining = re.compile("Död{}".format(rem_letters), re.IGNORECASE | re.UNICODE)
reg_occupation = re.compile("([\w\s,]*)", re.IGNORECASE | re.UNICODE)
reg_newline_on_full_stop = re.compile("(?<=[^\.])\n", re.UNICODE)
reg_space_after_newline = re.compile("\n ", re.UNICODE | re.IGNORECASE)
reg_long_space = re.compile(" {2,}", re.UNICODE)
reg_file_id = re.compile("\/\d*\/\d*\/\d*.htm", re.IGNORECASE | re.UNICODE)


def match_or_else(match, pos, other):
    try:
        return match.group(pos)
    except:
        return other


def get_first_cell(table):
    cell = table.find("tr").find_all("td")  # Extract the cell containing person info
    if len(cell[0].contents) > 0:
        return cell[0]
    else:
        return cell[1]


def path_to_file_id(file_name):
    """
    Gets the unique path id of this file, which corresponds to the path of the last two directories.
    :param file_name: the file's name as a string
    :return: a string on the form "folder1/folder2/filename"
    """
    file_name = re.sub("\\\\", "/", file_name)
    path = file_name.split("/")
    return "/".join(path[-3:])


class Person:

    def __init__(self, file):
        self.html = file.read()
        self.file_id = path_to_file_id(file.name)
        self.bs = BeautifulSoup(self.html, 'html.parser')
        self.tables = self.bs.find_all("table")

        # Declare empty holders
        self.first_name = ""
        self.middle_names = []
        self.last_name = ""
        self.birth_date = ""
        self.birth_loc = ""
        self.death_date = ""
        self.death_loc = ""
        self.bury_date = ""
        self.bury_loc = ""
        self.occupation = ""
        self.notes = ""
        self.spouses = []  # list of spouses on the form (spouse id, date, location)
        self.father = ""  # unique html file path
        self.mother = ""  # unique html file path
        self.children = []  # list of unique html file paths
        self.references = []

        self.set_names(self.bs.find_all("title")[-1].string)  # Find names from innermost title tag
        self.parse_cell()
        self.set_notes()
        if len(self.notes.strip()) < 2:
            # Residual symbols might be parsed as notes.
            # If less than 2 symbols, this is garbage.
            self.notes = ""
        self.set_father()
        self.set_mother()
        self.set_children()
        self.set_spouses()
        self.set_references()

    def set_references(self):
        font = self.bs.find_all("table")[-1].find_next("hr").find_next("font")
        if "Källor" in font.text:
            for item in font.find("ol").find_all("li"):
                self.references.append(item.text.strip())

    def set_spouses(self):

        table = self.tables[-1]
        cell = table.find("tr").find_all("td")[1]
        all_x5 = cell.find_all("x5")

        for x5 in all_x5:
            date_and_loc = str(x5.contents[0]).strip()
            match = reg_date.search(date_and_loc)
            date_pos = match.regs[1][1]
            date = match_or_else(match, 1, "")
            match = reg_loc.search(date_and_loc)
            loc = match_or_else(match, 1, date_and_loc[date_pos:])

            a_tags = x5.find_all("a")
            for a in a_tags:
                if "href" in a.attrs and reg_file_id.search(a.attrs["href"]):
                    spouse_id = path_to_file_id(a.attrs["href"])
                    self.spouses.append((spouse_id, date.strip(), loc.strip()))
                    break

    def set_children(self):

        table = self.tables[-1]
        cell = table.find("tr").find_all("td")[1]
        bqs = cell.find_all("blockquote")  # Blocks where childrens names are listed

        for bq in bqs:
            a_tags = bq.find_all("a")
            for a in a_tags:
                if "href" in a.attrs and reg_file_id.search(a.attrs["href"]):  # href is refering to a child
                    self.children.append(path_to_file_id(a.attrs["href"]))

    def set_father(self):
        father = self.set_parent(self.tables[0], 0, 1)
        if father == "":
            if len(self.tables) < 2:
                return
            father = self.set_parent(self.tables[1], 0, 1)

        self.father = father

    def set_mother(self):
        mother = self.set_parent(self.tables[0], 2, 0)
        if mother == "":
            if len(self.tables) < 2:
                return
            mother = self.set_parent(self.tables[1], 2, 0)

        self.mother = mother

    def set_parent(self, table, row, col):
        try:
            cell = table.find_all("tr")[row].find_all("td")[col]  # Get cell from first row second column
        except:
            # The parent is not in table 0, try table 1
            return ""

        if cell.a and "href" in cell.a.attrs:
            path = cell.a.attrs["href"]
            return path_to_file_id(path)
        return ""

    def set_notes(self):
        if len(self.tables) < 2:
            return

        cell = get_first_cell(self.tables[1])

        if len(self.tables) > 2:  # Other type of html, we only have 2 tables
            cell = get_first_cell(self.tables[2])

        if cell.font and cell.font.contents[0].strip().startswith("Levnadsbeskrivning"):  # Has notes!
            for line in cell.contents[1:]:  # Skip content with header 'Levnadsbeskrivning'
                line_str = str(line).strip()

                if line_str.lower().startswith("<br"):  # Insert line break
                    self.notes += "\n"
                elif line_str and line_str[0] != "<":
                    self.notes += line_str.strip()

        # Trim excess newline and space
        self.notes = reg_newline_on_full_stop.sub(' ', self.notes).strip()
        self.notes = reg_long_space.sub(' ', self.notes)
        self.notes = reg_space_after_newline.sub('\n', self.notes)

    def parse_cell(self):
        cell = get_first_cell(self.tables[0])  # Extract the cell containing person info
        clean = bleach.clean(cell.text, tags=[], strip=True)
        lines = clean.split("\n")  # Split on newline
        lines = [l.strip() for l in lines]  # remove whitespace
        lines = list(filter(None, lines))  # remove empty elements
        found_name = self.first_name != ""

        last_found_i = 0
        for line in lines:
            if line.lower().startswith("född"):  # parse born line
                self.set_birth(line)
                last_found_i += 1
            elif line.lower().startswith("död"):  # parse death line
                self.set_death(line)
                last_found_i += 1
            elif line.lower().startswith("begravd"):
                self.set_bury(line)
                last_found_i += 1
            elif found_name and line and line[0].isalpha():  # Remaining line is occupation
                if len(self.occupation) == 0 and not (line.startswith(self.first_name) or line.startswith(self.last_name)):
                    match = reg_occupation.search(line)
                    self.occupation = match_or_else(match, 1, "").strip()
                    last_found_i += 1

        for line in lines[last_found_i:]:  # Remaining lines should be notes
            if self.first_name == "" and self.last_name == "":
                self.notes += line + "\n"
            elif not line.startswith(self.first_name[0:-1]) and not line.startswith(self.last_name[0:-1]):
                self.notes += line + "\n"

    def set_bury(self, bury_str):
        match = reg_date.search(bury_str)
        self.bury_date = match_or_else(match, 1, "").strip()
        match = reg_loc.search(bury_str)
        self.bury_loc = match_or_else(match, 1, "").strip()

    def set_birth(self, birth_str):
        # Get the birth date
        match = reg_birth_date.search(birth_str)
        self.birth_date = match_or_else(match, 1, "").strip()
        # Get the birth location
        if "i" and "på" in birth_str: # Complex form, remove date and extract all
            birth_str = birth_str.replace(self.birth_date, "")  # Remove birth date from string
            birth_str = reg_long_space.subn(" ", birth_str)[0]
            match_or_else(reg_birth_remaining.search(birth_str), 1, "")
        else:
            match = reg_birth_loc.search(birth_str)
            self.birth_loc = match_or_else(match, 1, match_or_else(reg_birth_remaining.search(birth_str), 1, "")).strip()

    def set_death(self, death_str):
        # Get the death date
        match = reg_death_date.search(death_str)
        self.death_date = match_or_else(match, 1, "").strip()
        # Get the death location
        if " i " and " på " in death_str:  # Complex form, remove date and extract all
            death_str = death_str.replace(self.death_date, "")  # Remove death date from string
            death_str = reg_long_space.subn(" ", death_str)[0]
            self.death_loc = match_or_else(reg_death_remaining.search(death_str), 1, "").strip()
        else:
            match = re.search(reg_death_loc, death_str)
            self.death_loc = match_or_else(match, 1, match_or_else(reg_death_remaining.search(death_str), 1, "")).strip()

    def set_names(self, name_str):
        """
        Finds and appropriately sets the names of the person. If there is only one name available,
        interprets it as a last name.
        :return:
        """
        names = reg_name.findall(reg_ansedel.sub('', name_str))
        if len(names) > 0:
            self.last_name = names[-1]
            if len(names) > 1:
                if "af" in names:  # Special last name, should be two words
                    self.last_name = " ".join(names[-2:])
                    if len(names) > 2:
                        self.first_name = names[0]
                        if len(names) > 3:
                            self.middle_names = names[1:-2]
                else:
                    self.first_name = names[0]
                    if len(names) > 2:
                        self.middle_names = names[1:-1]

    def as_json(self):

        json = {
            "first_name": self.first_name,
            "middle_name": self.middle_names,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "birth_loc": self.birth_loc,
            "death_date": self.death_date,
            "death_loc": self.death_loc,
            "bury_date": self.bury_date,
            "bury_loc": self.bury_loc,
            "occupation": self.occupation,
            "notes": self.notes,
            "file_id": self.file_id,
            "spouses": self.spouses,
            "father": self.father,
            "mother": self.mother,
            "children": self.children,
            "references": self.references
        }

        return json
