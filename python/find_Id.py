import json
import re
import sys
from pathlib import Path

import pymupdf

from src.PeopleSection import PeopleSection
from src.pdf_helper import book_page_to_pdf_index
from src.person_helper import extract_people_sections, find_person_id

REG_PORTRAIT_NAME = re.compile(r'^p(\d+)_pn(\d+)')


def full_name(person: dict):
    first_name = person.get('firstName')
    last_name = person.get('lastName')
    middle_names = person.get('middleNames')
    return f'{first_name} {middle_names} {last_name}'


def person_identifier_str(person: dict, pid: str):
    birth_year = person.get('birth', {}).get('date', {}).get('year', None)
    return f'{full_name(person)} f. {birth_year} -> id: {pid}'


def portrait_sort_key(img_path: Path) -> int:
    if match := REG_PORTRAIT_NAME.match(img_path.stem):
        return int(match.group(1)) * 1000 + int(match.group(2))
    raise Exception(f'Could not match {img_path.stem}')


def get_people_sections(pages: list[pymupdf.Page], book_page: int) -> list[PeopleSection]:
    index = book_page_to_pdf_index(book_page)
    page = pages[index]
    text = page.get_text()
    return extract_people_sections(text, book_page)


def manually_find_person_pid(persons_data: dict) -> int | None:
    birth_year = int(input('Birth: '))
    first_name = input('First name: ')
    found: list[dict] = []

    for _, person in persons_data.items():
        date = person.get('birth').get('date')
        year = date.get('year') if date else None
        name = person.get('firstName')

        if year and year == birth_year and name and name.lower().strip() == first_name.lower().strip():
            found.append(person)

    selected = 0
    if not found:
        print('❌ No person found!')
        return None
    elif len(found) > 1:
        for i, person in enumerate(found):
            pid = person.get('id') + 1
            print(f'  {i}. {person_identifier_str(person, pid)}')
        selected = int(input('Multiple people matched. Select correct:').strip())

    person = found[selected]
    pid = person.get('id') + 1
    print(f'✅ {person_identifier_str(person, pid)}')
    return pid


if __name__ == '__main__':
    PORTRAITS_DIR = Path('contour_portraits')
    FINISHED_PORTRAITS_DIR = Path('../static_media/portraits')
    portraits = list(sorted(PORTRAITS_DIR.glob('*.png'), key=portrait_sort_key))
    pdf_path = sys.argv[1]
    with open('persons.json', 'r', encoding='utf-8') as f:
        persons_data = json.load(f)

    with pymupdf.open(pdf_path) as pdf:
        print(f'Reading PDF from {pdf_path}')
        pages = list(pdf.pages())

        portrait_index = 0
        while True:
            portrait = portraits[portrait_index]
            match = REG_PORTRAIT_NAME.match(portrait.stem)
            book_page = int(match.group(1))
            pn = match.group(2)
            print(f'Processing Page {book_page}: {portrait}')

            people_sections = [p for p in get_people_sections(pages, book_page) if p.first_name and p.birth_year]
            print(f'Found {len(people_sections)} people on page.')
            
            for i, person in enumerate(people_sections):
                print(f'\t{i+1}: {person}')

            print(f'\t0: None of the above!')

            person_index = int(input('Select the correct one:'))
            if person_index == 0:
                pid = manually_find_person_pid(persons_data)
            else:
                person = people_sections[person_index-1]
                pid = find_person_id(persons_data, person)
                print(f'✅ {person}')
                
            if pid:
                new_filename = f'id{pid}.png'
                output_name = FINISHED_PORTRAITS_DIR / new_filename
                (PORTRAITS_DIR / portrait.name).rename(output_name)
                print(f'Renamed {portrait} -> {output_name}')
                print('')
                portrait_index += 1
