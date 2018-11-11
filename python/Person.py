from bs4 import BeautifulSoup
import re
import bleach

# Declare regex

reg_ansedel = re.compile("ansedel", re.IGNORECASE | re.UNICODE)
reg_name = re.compile("\w+", re.IGNORECASE | re.UNICODE)
date_str = "[\sa-zA-Z]*([\d-]*)"
loc_str = "[\w\s-]*\s+i\s+([\w,\s]*)"
reg_birth_date = re.compile("Född{}".format(date_str), re.IGNORECASE | re.UNICODE)
reg_birth_loc = re.compile("Född{}".format(loc_str), re.IGNORECASE | re.UNICODE)
reg_death_date = re.compile("Död{}".format(date_str), re.IGNORECASE | re.UNICODE)
reg_death_loc = re.compile("Död{}".format(loc_str), re.IGNORECASE | re.UNICODE)
reg_occupation = re.compile("(\w*)", re.IGNORECASE | re.UNICODE)
reg_newline_no_full_stop = re.compile("(?<=[^\.])\n", re.UNICODE)
reg_long_space = re.compile("\s{2,}", re.UNICODE)


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
    :param file: the file's name as a string
    :return: a string on the form "folder1/folder2/filename"
    """
    path = file_name.split('/')
    return "/".join(path[-3:])

class Person:

    def __init__(self, file):
        self.html = file.read()
        self.file_id = path_to_file_id(file.name)
        self.bs = BeautifulSoup(self.html, 'html.parser')
        self.tables = self.bs.find_all("table")

        # Declare empty holders
        self.first_name = ""
        self.middle_names = [""]
        self.last_name = ""
        self.birth_date = ""
        self.birth_loc = ""
        self.death_date = ""
        self.death_loc = ""
        self.occupation = ""
        self.notes = ""
        self.spouses = [dict]  # list of spouses on the form
        self.father = ""  # unique html file path
        self.mother = ""  # unique html file path
        self.children = [""]  # list of unique html file paths

        self.set_names(self.bs.find_all("title")[-1].string)  # Find names from innermost title tag
        self.parse_cell()
        self.set_notes()
        self.set_father()
        self.set_mother()
        self.set_spouse_and_children()

    def set_spouse_and_children(self):
        if len(self.tables) < 3:
            return
        table = self.tables[-1]
        cell = table.find("tr").find_all("td")[1]
        cell

    def set_father(self):
        self.father = self.set_ancestor(0,1)

    def set_mother(self):
        self.mother = self.set_ancestor(2, 0)

    def set_ancestor(self, row, col):
        table = self.tables[0]
        if len(self.tables) > 2:
            table = self.tables[1]

        cell = table.find_all("tr")[row].find_all("td")[col]  # Get cell from first row second column
        path = cell.a.attrs["href"]
        return path_to_file_id(path)

    def set_notes(self):
        cell = get_first_cell(self.tables[1])

        if len(self.tables) > 2:  # Other type of html, we only have 2 tables
            cell = get_first_cell(self.tables[2])

        if cell.font.contents[0].strip().startswith("Levnadsbeskrivning"):  # Has notes!
            for line in cell.contents[1:]:  # Skip content with header 'Levnadsbeskrivning'
                line_str = str(line).strip()

                if line_str.lower().startswith("<br"):  # Insert line break
                    self.notes += "\n"
                elif line_str and line_str[0] != "<":
                    self.notes += line_str.strip()

        # Trim excess newline and space
        self.notes = reg_newline_no_full_stop.sub('', self.notes).strip()
        self.notes = reg_long_space.sub(' ', self.notes)

    def parse_cell(self):
        cell = get_first_cell(self.tables[0])  # Extract the cell containing person info
        clean = bleach.clean(cell.text, tags=[], strip=True)
        lines = clean.split("\n")  # Split on newline
        lines = [l.strip() for l in lines]  # remove whitespace
        lines = list(filter(None, lines))  # remove empty elements
        found_name = self.first_name != ""

        for line in lines:
            if line.lower().startswith("född"):  # parse born line
                self.set_birth(line)
            elif line.lower().startswith("död"):  # parse death line
                self.set_death(line)
            elif not found_name and (line.lower().startswith("<b") or line and line[0].isalpha()):  # parse name line
                found_name = True
                self.set_names(line)
            elif found_name and len(lines) > 1 and line and line[
                0].isalpha():  # Remaining line is occupation if more than 1 line
                match = reg_occupation.search(line)
                self.occupation = match_or_else(match, 1, "").strip()

    def set_birth(self, birth_str):
        match = reg_birth_date.search(birth_str)
        self.birth_date = match_or_else(match, 1, "").strip()
        match = reg_birth_loc.search(birth_str)
        self.birth_loc = match_or_else(match, 1, "").strip()

    def set_death(self, death_str):
        match = reg_death_date.search(death_str)
        self.death_date = match_or_else(match, 1, "").strip()
        match = reg_death_loc.search(death_str)
        self.death_loc = match_or_else(match, 1, "").strip()

    def set_names(self, name_str):
        """
        Finds and appropriately sets the names of the person.
        :return:
        """
        names = reg_name.findall(reg_ansedel.sub('', name_str))
        self.first_name = names[0]
        if len(names) > 1:
            self.last_name = names[-1]
            if len(names) > 2:
                self.middle_names = names[1:-1]
