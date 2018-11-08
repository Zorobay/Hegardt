from bs4 import BeautifulSoup
import re

# Declare regex
reg_ansedel = re.compile("ansedel", re.IGNORECASE | re.UNICODE)
reg_name = re.compile("\w+", re.IGNORECASE | re.UNICODE)


def to_html(file):
    with open(file, 'r') as of:
        return of.read()


class Person:

    def __init__(self, file):
        self.html = to_html(file)
        self.path = file
        self.bs = BeautifulSoup(self.html)
        self.table1 = self.bs.find("table")
        self.table2 = self.bs.find_next("table")

        # Declare empty holders
        self.first_name = ""
        self.middle_names = [""]
        self.last_name = ""
        self.born_date = None
        self.born_location = ""
        self.dead = None
        self.dead_location = ""
        self.occupation = ""
        self.notes = ""
        self.father = ""  # unique html file path
        self.mother = ""  # unique html file path
        self.children = [""]  # list of unique html file paths

        self.set_names(self.bs.title.string)

    def set_names(self, title_string):
        """
        Finds and appropriately sets the names of the person.
        :param title_string: the contents of the <title> tags.
        :return:
        """

        names = reg_name.findall(reg_ansedel.sub('', title_string))
        self.first_name = names[0]
        if len(names) > 1:
            self.last_name = names[-1]
            if len(names) > 2:
                self.middle_names = names[1:-1]


