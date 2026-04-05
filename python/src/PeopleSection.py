import re





class PeopleSection:
    REG_FULL = re.compile(r'^(\d+)\.(?:\s\d+\.)?\s(.+),(?=\sf\.)(?:(?!f\.).)+f\.\D+(\d+)')
    REG_NUMBER = re.compile(r'^(\d+)\..*')
    REG_BIRTH_YEAR = re.compile(r'f\.\s(?:[a-zA-Z\s]+\s)?(\d+)')
    REG_FULL_NAMES = re.compile(r'^\d+\.(?:\s\d+\.)?\s([\w\(\)\s]+),')
    REG_NAMES = re.compile(r'(\w+)\s*(\w*)')

    def __init__(self, section: str, book_page: int = -1):
        self.full_section = section.replace('\n', '')
        self.book_page = book_page
        self.full_description = ''
        self.number = None
        self.first_name = ''
        self.last_name = ''
        self.birth_year = None
        self.could_be_parsed = False
        self._parse()

    @classmethod
    def csv_headers(cls) -> str:
        return ';'.join(['Page', 'Number', 'FirstName', 'LastName', 'BirthYear'])
    def csv_data(self) -> str:
        return ';'.join(str(d) for d in [self.book_page, self.number, self.first_name, self.last_name, self.birth_year])

    def __str__(self):
        return f'{self.number}. {self.first_name} {self.last_name} f. {self.birth_year}'

    def _parse(self):
        if match := self.REG_NUMBER.match(self.full_section):
            num = match.group(1)
            self.number = int(num) if num else None

        if match := self.REG_BIRTH_YEAR.search(self.full_section):
            year = match.group(1)
            self.birth_year = int(year) if year else None

        self._parse_name()

        if self.first_name and self.birth_year and self.number:
            self.could_be_parsed = True

    def _parse_name(self):
        if match := self.REG_FULL_NAMES.match(self.full_section):
            full_name = match.group(1)
            open_index = full_name.find('(')
            if open_index > 0:
                close_index = full_name.find(')', open_index)+1
                if close_index > 0:
                    # Remove nickname
                    full_name = full_name[:open_index] + full_name[close_index:]
                else:
                    # Remove all left of and including '('
                    full_name = full_name[:open_index]

            if match := self.REG_NAMES.match(full_name.strip()):
                self.first_name = match.group(1)
                self.last_name = match.group(2) or ''
