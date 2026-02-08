import re
import json
from pypdf import PdfReader

PERSONS_JSON_FILENAME = "persons.ts"
OUTPUT_PERSON_DATA_FILENAME = 'person_data.txt'
READ_FILENAME = "Hegardt_300dpi_sökbar_adobe_komprimerad.pdf"
OUTPUT_PDF_FILENAME = "Hegardt_300dpi_sökbar_adobe_komprimerad_HYPERLINKS.pdf"
START_PAGE = 13-1 # 0 based
PDF_PAGE_KEY = 'pdfPage'

REG_PEOPLE_SECTION = re.compile(r'\n\d\.\s')
REG_NUMBER = re.compile(r'\d+\.\s?')
REG_NAME_BIRTH_YEAR = re.compile(r'^([\w\s]+)\(?.*\)?, f. \D*(\d+).*')
def separate_page_by_people_sections(page_text: str) -> list[str]:
    # Cut characters until first '1., 2. etc.'
    i = 0
    while True:
        t = page_text[i:i+2]
        if match:=REG_NUMBER.match(t):
            break
        i+=1

    splits = REG_PEOPLE_SECTION.split(page_text[i:])
    splits[0] = REG_NUMBER.sub('', splits[0])
    return splits

def extract_name_birth_year(people_section: str) -> tuple[str, int]:
    if match := REG_NAME_BIRTH_YEAR.match(people_section):
        name = match.group(1)
        year = match.group(2)
        return name, year
    raise Exception(f'Could not extract name and year from {people_section}')


if __name__ == '__main__':
    reader = PdfReader(READ_FILENAME)
    out = []
    for page in reader.pages:
        if page.page_number < START_PAGE:
            continue

        text = page.extract_text()
        print(f'\n==== Processing page {page.page_number} ====')
        people_sections = separate_page_by_people_sections(text)

        for section in people_sections:
            name, year = extract_name_birth_year(section)
            print(f'\tFound name: {name}, year: {year}')
            out.append([name, year, page.page_number])

    with open(OUTPUT_PERSON_DATA_FILENAME, 'w', encoding='utf-8') as f:
        f.writelines(out)