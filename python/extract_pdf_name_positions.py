import json
import sys
from typing import Any

import pymupdf

from src.PeopleSection import PeopleSection
from src.constants import START_PAGE, PERSONS_JSON_FILENAME, END_PAGE, EXCLUDE_IMAGES_FROM_TEXT_EXTRACTION_FLAGS
from src.pdf_helper import get_person_pages, get_book_page
from src.person_helper import find_person_id, extract_people_sections


class PdfUpdateData:

    def __init__(self, page: int, text_line: 'TextLine'):
        self.page = page
        self.text_line = text_line

    def __eq__(self, other: 'PdfUpdateData') -> bool:
        return other.page == self.page and self.text_line.coords_and_dimensions_as_string() == other.text_line.coords_and_dimensions_as_string()


class TextLine(dict):

    def __init__(self, text_line: dict[str, Any]):
        super().__init__()
        self._bbox = text_line.get('bbox')
        self.text = ''.join([span.get('text', '') for span in text_line.get('spans', [])])
        self.x0 = self._bbox[0]
        self.top = self._bbox[1]
        self.x1 = self._bbox[2]
        self.bottom = self._bbox[3]

    def __str__(self) -> str:
        return f'{self.text} - {self.coords_and_dimensions_as_string()}'
    
    def __repr__(self) -> str:
        return self.__str__()

    def coords_and_dimensions_as_string(self) -> str:
        return f'{round(self.x0, 2)}, {round(self.top, 2)}, {round(self.width(), 2)}, {round(self.height(), 2)}'

    def height(self) -> float:
        return self.bottom - self.top

    def width(self) -> float:
        return self.x1 - self.x0


def get_pdf_update_sql(all_data: dict[int, list[PdfUpdateData]]) -> list[str]:
    out = []
    pdf_id = 1
    for person_id, pdf_data in all_data.items():
        sql = f'/* Inserts for person with id: {person_id} */'

        checked = []
        for data in pdf_data:
            if data not in checked:
                text_line = data.text_line
                sql += f'''
INSERT INTO pdf_reference (id, version, person_id, pdf_page, x0, y0, width, height) 
VALUES ({pdf_id}, 1, {person_id}, {data.page}, {text_line.coords_and_dimensions_as_string()});
    '''
                checked.append(data)
                pdf_id += 1
        sql += '\n'
        out.append(sql)
    return out


def find_text_lines(search_string: str, text_lines: list[TextLine]) -> list[TextLine]:
    out = []
    for line in text_lines:
        if line.text.lower().startswith(search_string.lower()):
            out.append(line)
    return out


def get_text_lines(page: pymupdf.Page):
    all_lines = []
    blocks = page.get_text('dict', sort=True, flags=EXCLUDE_IMAGES_FROM_TEXT_EXTRACTION_FLAGS).get('blocks', [])
    for block in blocks:
        lines = block.get('lines', [])
        all_lines.extend(lines)
    return [TextLine(l) for l in all_lines]


def extract_pdf_name_positions():
    path = sys.argv[1]
    with open(PERSONS_JSON_FILENAME, 'r') as f:
        print(f'Reading PDF at {path}')
        persons_data = json.load(f)

    out = {}
    missing_people: dict[int, list[PeopleSection]] = dict()
    # with pdfplumber.open(path) as pdf:
    with pymupdf.open(path) as pdf:
        for page in get_person_pages(pdf):
            page_number = page.number + 1  # convert to 1 based indexing
            missing_people[page_number] = []
            book_page = get_book_page(page)

            text = page.get_text()
            text_lines = get_text_lines(page)
            people_sections = extract_people_sections(text, book_page)
            page_matches = []

            print(f'\n>>>> Found {len(people_sections)} on page {page_number}')

            for person in people_sections:
                search_string = person.full_section[:8]
                matching_lines = find_text_lines(search_string, text_lines)
                person_id = find_person_id(persons_data, person)

                if not person_id:
                    print(f'WARNING: Could not find id for person:\n\t{person}')
                    if person.first_name or person.birth_year:
                        missing_people[page_number].append(person)
                    continue

                if matching_lines:
                    for line in matching_lines:
                        page_matches.append(line)
                        if person_id not in out:
                            out[person_id] = []

                        out[person_id].append(PdfUpdateData(page_number, line))
                    print(f'Found {len(matching_lines)} for {person}')

    sql_output_filename = 'V3__seed_pdf_reference_data.sql'
    sql_data_lines = get_pdf_update_sql(out)
    with open(sql_output_filename, 'w', encoding='utf-8') as f:
        f.writelines(sql_data_lines)
        print(f'Written SQL data to {sql_output_filename}')

    print('------------------- Missing People! -----------------------')
    for page, people in missing_people.items():
        if people:
            print(f'\n==== Page {page} ====')
            for person in people:
                print(f'\t{person}')


if __name__ == '__main__':
    extract_pdf_name_positions()
