import json
from typing import Any

import pdfplumber

from src.PeopleSection import PeopleSection
from src.constants import REG_NUMBER, START_PAGE, REG_PEOPLE_SECTION, PDF_FILENAME_300DPI, PERSONS_JSON_FILENAME


class PdfUpdateData:

    def __init__(self, page: int, text_line: 'TextLine'):
        self.page = page
        self.text_line = text_line

    def __eq__(self, other: 'PdfUpdateData') -> bool:
        return other.page == self.page and self.text_line.coords_as_string() == other.text_line.coords_as_string()


class TextLine(dict):

    def __init__(self, text_line: dict[str, Any]):
        super().__init__(
            x0=text_line["x0"],
            top=text_line["top"],
            x1=text_line["x1"],
            bottom=text_line["bottom"]
        )
        self.text = text_line['text']
        self.x0 = text_line['x0']
        self.top = text_line['top']
        self.x1 = text_line['x1']
        self.bottom = text_line['bottom']

    def coords_as_string(self) -> str:
        return f'{round(self.x0, 2)}, {round(self.top, 2)}, {round(self.x1, 2)}, {round(self.bottom, 2)}'

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
INSERT INTO pdf_reference (id, version, person_id, pdf_page, x0, y0, x1, y1) 
VALUES ({pdf_id}, 1, {person_id}, {data.page}, {text_line.coords_as_string()});
    '''
                checked.append(data)
                pdf_id += 1
        sql += '\n'
        out.append(sql)
    return out


def extract_people_sections(page_text: str, book_page: int) -> list[PeopleSection]:
    start_index = 0
    missing_header = book_page == START_PAGE

    # Cut characters until first '1., 2. etc.'
    if not missing_header:
        if match := REG_NUMBER.search(page_text):
            start_index = match.start() + 1

    splits = REG_PEOPLE_SECTION.split(page_text[start_index:])
    return [PeopleSection(s, book_page) for s in splits]


def find_id(persons_data: dict, person: PeopleSection) -> int | None:
    for key, item in persons_data.items():
        first_name = item['firstName']
        middle_names = [mn.lower() for mn in item['middleNames']]
        birth_date = item['birth']['date']
        if birth_date:
            birth_year = birth_date['year']

            if first_name.lower() == person.first_name.lower() and birth_year == person.birth_year:
                if person.middle_name:
                    if person.middle_name.lower() in middle_names:
                        return int(key) + 1  # The JSON Ids are 0 based, but the database starts from 1
                else:
                    return int(key) + 1  # The JSON Ids are 0 based, but the database starts from 1

    return None


def find_text_lines(search_string: str, text_lines: list[TextLine]) -> list[TextLine]:
    out = []
    for line in text_lines:
        if line.text.lower().startswith(search_string.lower()):
            out.append(line)
    return out


def save_page_to_image(page, rects):
    image = page.to_image(resolution=150)
    image.draw_rects(rects)
    debug_img_name = f"debug_page_{page.page_number}.png"
    image.save(f"debug_page_{page.page_number}.png")
    print(f'Saved debug image {debug_img_name}')


def extract_name_coordinates():
    with open(PERSONS_JSON_FILENAME, 'r') as f:
        persons_data = json.load(f)

    out = {}
    with pdfplumber.open(PDF_FILENAME_300DPI) as pdf:
        for page in pdf.pages:
            book_page = page.page_number - 4

            if book_page < START_PAGE or book_page > 102:
                continue

            text = page.extract_text()
            text_lines = [TextLine(tl) for tl in page.extract_text_lines()]
            people_sections = extract_people_sections(text, book_page)
            page_matches = []

            print(f'\n>>>> Found {len(people_sections)} on page {page.page_number}')

            for person in people_sections:
                search_string = person.full_section[:8]
                matching_lines = find_text_lines(search_string, text_lines)
                person_id = find_id(persons_data, person)

                if not person_id:
                    print(f'WARNING: Could not find id for person:\n\t{person}')
                    continue

                if matching_lines:
                    for line in matching_lines:
                        page_matches.append(line)
                        if person_id not in out:
                            out[person_id] = []

                        out[person_id].append(PdfUpdateData(page.page_number, line))
                    print(f'Found {len(matching_lines)} for {person}')

    sql_output_filename = 'V3__seed_pdf_data.sql'
    sql_data_lines = get_pdf_update_sql(out)
    with open(sql_output_filename, 'w', encoding='utf-8') as f:
        f.writelines(sql_data_lines)
        print(f'Written SQL data to {sql_output_filename}')


if __name__ == '__main__':
    extract_name_coordinates()
