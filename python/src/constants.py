import re

import pymupdf

PDF_FILENAME_300DPI = "res/hegardt_300dpi_searchable.pdf"
PERSONS_JSON_FILENAME = "persons.json"

REG_PEOPLE_SECTION = re.compile(r'(?=\n\d+(?:\s\w\))?\.)\s')
REG_NUMBER = re.compile(r'\n\d+\.\s?')
REG_NAME_BIRTH_YEAR = re.compile(r'^([\w\s]+)\(?.*\)?, f. \D*(\d+).*')
SKIPPABLE_PAGES = [90]
START_PAGE = 9
END_PAGE = 102

EXCLUDE_IMAGES_FROM_TEXT_EXTRACTION_FLAGS = pymupdf.TEXTFLAGS_DICT & ~pymupdf.TEXT_PRESERVE_IMAGES
