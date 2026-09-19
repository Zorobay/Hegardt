import typing

import pymupdf

from src.constants import START_PAGE, END_PAGE


def get_person_pages(pdf: pymupdf.Document) -> typing.Iterable[pymupdf.Page]:
    return pdf.pages(START_PAGE + 4, END_PAGE + 4 + 1)


def book_page_to_pdf_index(book_page: int) -> int:
    return book_page + 4 - 1


def get_book_page(page: pymupdf.Page) -> int:
    return page.number + 1 - 4  # Convert to 1 based indexing, then subtract 4 for book page
