import unittest

from pypdf import PdfReader, PageObject

from src.PeopleSection import PeopleSection
from parse_pdf import PDF_FILENAME_300DPI, extract_people_sections


def _read_pages() -> list[PageObject]:
    reader = PdfReader(PDF_FILENAME_300DPI)
    return reader.pages

def parseable(number: int, birth_year: int, first_name: str, last_name: str = '') -> PeopleSection:
    person = PeopleSection('')
    person.number = number
    person.birth_year = birth_year
    person.first_name = first_name
    person.last_name = last_name
    person.could_be_parsed = True
    return person

def unparseable(number: int) -> PeopleSection:
    person = PeopleSection('')
    person.number = number
    person.could_be_parsed = False
    return person

class MainTest(unittest.TestCase):

    def __init__(self, method_name: str):
        super().__init__(method_name)
        self.pages = []

    def setUp(self):
        self.pages = _read_pages()

    def test_page_9(self):
        self._test_page(9, [
            parseable(1, 1672, 'JOSIAS'),
            parseable(2, 1704, 'Peter', 'Josias'),
            parseable(191, 1708, 'Anders'),
            parseable(2, 1704, 'Peter', 'Josias'),
            parseable(3, 1736, 'Katarina'),
        ])

    def test_page_11(self):
        self._test_page(11, [
            unparseable(6),
            parseable(7, 1767, 'Helena', 'Elisabet'),
            parseable(8, 1769, 'Peter'),
            parseable(9, 1770, 'Peter'),
            parseable(10, 1772, 'Cecilia', 'Katarina'),
            parseable(11, 1776, 'Eva', 'Beata'),
        ])

    def test_page_48(self):
        self._test_page(48, [
            parseable(129, 1906, 'Anna', 'Elisabet'),
            parseable(130, 1908, 'Ingeborg', 'Maria'),
        ])

    def test_page_49(self):
        self._test_page(49, [
            parseable(131, 1910, 'Ebba', 'Margareta'),
            parseable(132, 1913, 'Klara', 'Elisabet'),
            parseable(134, 1831, 'Henrik', 'Bernhard')
        ])
    #
    # def test_page_39(self):
    #     self._test_page(11, [
    #         unparseable(6),
    #         parseable(7, 1767, 'Helena', 'Elisabet'),
    #         parseable(8, 1769, 'Peter'),
    #         parseable(9, 1770, 'Peter'),
    #         parseable(10, 1772, 'Cecilia', 'Katarina'),
    #         parseable(11, 1776, 'Eva', 'Beata'),
    #     ])

    def _test_page(self, page: int, expected_people: list[PeopleSection]):
        people = self._get_people_sections(page)
        for i, exp_person in enumerate(expected_people):
            res_person = people[i]

            self.assertEqual(exp_person.number, res_person.number, msg=f'Wrong number! Expected: {exp_person}')
            self.assertEqual(exp_person.could_be_parsed, res_person.could_be_parsed, msg=f'Wrong could_be_parsed! Expected: {exp_person}')
            self.assertEqual(res_person.book_page, page, msg=f'Wrong book_page! Expected: {exp_person}')

            if exp_person.could_be_parsed:
                self.assertEqual(exp_person.first_name.lower(), res_person.first_name.lower(), msg=f'Wrong first_name! Expected: {exp_person}')
                self.assertEqual(exp_person.last_name.lower(), res_person.last_name.lower(), msg=f'Wrong last_name! Expected: {exp_person}')
                self.assertEqual(exp_person.birth_year, res_person.birth_year, msg=f'Wrong birth_year! Expected: {exp_person}')

    def _get_people_sections(self, book_page: int):
        page_index = book_page+3
        page = self.pages[page_index]
        return extract_people_sections(page.extract_text(), book_page)


