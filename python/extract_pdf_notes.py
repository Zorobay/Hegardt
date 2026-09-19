import json
import sys

import pdfplumber

from src.constants import PERSONS_JSON_FILENAME, START_PAGE, END_PAGE
from src.person_helper import extract_people_sections, find_person_id

def escape(text: str) -> str:
    return text.replace("'", "''")
    
def create_sql_update_line(person_id: int, note: str)->str:
    return rf"""
/* Appending notes to person with id: {person_id} */
UPDATE person AS p
SET notes = CONCAT(notes, E'\n\n', '<strong>Notes from Family Book</strong>', E'\n', '{escape(note)}')
WHERE p.id = {person_id};
"""

def extract_pdf_notes():
    path = sys.argv[1]
    with open(PERSONS_JSON_FILENAME, 'r') as f:
        print(f'Reading PDF at {path}')
        persons_data = json.load(f)

    sql_output=[]
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:

            book_page = page.page_number - 4

            if book_page < START_PAGE or book_page > END_PAGE:
                continue

            print(f'\n==== Processing page {page.page_number} ====')

            people_sections = extract_people_sections(page.extract_text(), book_page)
            for person in people_sections:
                person_id = find_person_id(persons_data, person)
                
                if not person_id and (person.first_name or person.birth_year):
                    print(f'WARNING: Could not find id for person:\n\t{person}')
                    continue
                
                sql_output.append(create_sql_update_line(person_id, person.notes))
            
        OUTPUT_FILENAME = 'V4__seed_note_updates.sql'
        with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
            f.writelines(sql_output)
            print(f'Written output to {OUTPUT_FILENAME}')
                

if __name__ == '__main__':
    extract_pdf_notes()