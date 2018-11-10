from bs4 import BeautifulSoup
import re

# Declare regex

reg_ansedel = re.compile("ansedel", re.IGNORECASE | re.UNICODE)
reg_name = re.compile("\w+", re.IGNORECASE | re.UNICODE)
date_str = "[\sa-zA-Z]*([\d-]*)"
loc_str = "[\w\s-]*\s+i\s+([\w,\s]*)"
reg_birth_date = re.compile("Född{}".format(date_str),  re.IGNORECASE | re.UNICODE)
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
    cell = table.find("tr").find_all("td")[1]  # Extract the cell containing person info
    return cell


class Person:

    def __init__(self, file):
        self.html = file.read()
        self.file = file
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
        self.father = ""  # unique html file path
        self.mother = ""  # unique html file path
        self.children = [""]  # list of unique html file paths

        self.set_names()
        self.set_birth_death_and_occupation()
        self.set_notes()

    def set_notes(self):
        cell = get_first_cell(self.tables[2])

        if cell.font.contents[0].strip().startswith("Levnadsbeskrivning"):  # Has notes!
            for line in cell.contents[1:]:  # Skip content with header 'Levnadsbeskrivning'
                line_str = str(line).strip()

                if line_str.lower().startswith("<br"):  # Insert line break
                    self.notes += "\n"
                elif line_str and line_str[0].isalpha():
                    self.notes += line_str.strip()

        # Trim excess newline and space
        self.notes = reg_newline_no_full_stop.sub('', self.notes).strip()
        self.notes = reg_long_space.sub(' ', self.notes)

    def set_birth_death_and_occupation(self):
        """
        Finds and appropriately sets the locations and dates of birth and death
        :return:
        """
        cell = get_first_cell(self.tables[0])  # Extract the cell containing person info

        for line in cell.contents:
            line_str = str(line).strip()
            if line_str.lower().startswith("född"):
                match = reg_birth_date.search(line_str)
                self.birth_date = match_or_else(match, 1, "").strip()
                match = reg_birth_loc.search(line_str)
                self.birth_loc = match_or_else(match, 1, "").strip()
            elif line_str.lower().startswith("död"):
                match = reg_death_date.search(line_str)
                self.death_date = match_or_else(match, 1, "").strip()
                match = reg_death_loc.search(line_str)
                self.death_loc = match_or_else(match, 1, "").strip()
            elif line_str and line_str[0].isalpha():
                match = reg_occupation.search(line_str)
                self.occupation = match_or_else(match, 1, "").strip()

    def set_names(self):
        """
        Finds and appropriately sets the names of the person.
        :return:
        """
        title_string = self.bs.title.string

        names = reg_name.findall(reg_ansedel.sub('', title_string))
        self.first_name = names[0]
        if len(names) > 1:
            self.last_name = names[-1]
            if len(names) > 2:
                self.middle_names = names[1:-1]


