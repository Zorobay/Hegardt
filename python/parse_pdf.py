import re
from pathlib import Path

import cv2
import fitz
import numpy as np
from pymupdf import Page
from pypdf import PdfReader, PageObject

from src.PeopleSection import PeopleSection

PERSONS_JSON_FILENAME = "persons.json"
OUTPUT_PERSON_DATA_FILENAME = 'person_data.csv'
PDF_FILENAME_300DPI = "hegardt_300dpi_searchable.pdf"
PDF_FILENAME_600DPI = "hegardt_600dpi_searchable.pdf"
OUTPUT_PDF_FILENAME = "Hegardt_300dpi_sökbar_adobe_komprimerad_HYPERLINKS.pdf"
OUTPUT_PORTRAIT_PATH = Path('extracted_portraits')
SKIPPABLE_PAGES = [90]
START_PAGE = 9
END_PAGE = 102
PDF_PAGE_KEY = 'pdfPage'

REG_PEOPLE_SECTION = re.compile(r'(?=\n\d+\.)\s')
REG_NUMBER = re.compile(r'\n\d+\.\s?')
REG_NAME_BIRTH_YEAR = re.compile(r'^([\w\s]+)\(?.*\)?, f. \D*(\d+).*')


def get_book_page(page: PageObject | Page) -> int:
    if isinstance(page, Page):
        return page.number - 3
    return page.page_number - 3


def extract_people_sections(page_text: str, book_page: int) -> list[PeopleSection]:
    start_index = 0
    missing_header = book_page == START_PAGE

    # Cut characters until first '1., 2. etc.'
    if not missing_header:
        if match := REG_NUMBER.search(page_text):
            start_index = match.start() + 1

    splits = REG_PEOPLE_SECTION.split(page_text[start_index:])
    return [PeopleSection(s, book_page) for s in splits]


def extract_text():
    reader = PdfReader(PDF_FILENAME_600DPI)
    out: list[PeopleSection] = []
    for page in reader.pages:
        book_page = get_book_page(page)

        if book_page < START_PAGE or book_page > END_PAGE:
            continue

        text = page.extract_text()
        print(f'\n==== Processing page {book_page} ====')
        if book_page not in SKIPPABLE_PAGES:
            people_sections = extract_people_sections(text, book_page)
            for person in people_sections:
                print(f'\t* {person}')
            out.extend(people_sections)

    with open(OUTPUT_PERSON_DATA_FILENAME, 'w', encoding='utf-8') as f:
        f.write(PeopleSection.csv_headers())
        f.write('\n')
        for person in out:
            f.write(person.csv_data())
            f.write('\n')
        print(f"Wrote data to {OUTPUT_PERSON_DATA_FILENAME}")


def extract_pages_as_images():
    doc = fitz.open(PDF_FILENAME_600DPI)

    for page in doc.pages():
        book_page = get_book_page(page)

        if book_page < 10 or book_page > END_PAGE:
            continue

        matrix = fitz.Matrix(600 / 72, 600 / 72)  # 600 DPI
        pixmap = page.get_pixmap(matrix=matrix)
        path = f"pages_as_images/page_{book_page}.png"
        pixmap.save(path)
        print(f"Saved page {book_page} to {path}")


def extract_portraits_contour():
    PAGES_DIR = Path('./pages_as_images')
    OUTPUT_DIR = Path('./contour_portraits')
    REG_FILENAME = re.compile(r'page_(\d+)')

    # ─────────────────────── Tuning knobs ──────────────────────────
    AREA_MIN = 50_000  # ignore contours smaller than this (noise)
    AREA_MAX = 5_000_000  # ignore contours larger than this (full-page blobs)
    TARGET_HW_RATIO = 1.28  # expected height/width ratio of portraits
    HW_TOLERANCE = 0.20  # accept ratios within ±this of the target
    WHITE_LEVEL_THRESHOLD = 235  # Pixels with this brightness or brighter will be set to 100% white
    ELLIPSE_SHRINK = 0.95
    TARGET_W, TARGET_H = 712, 920
    SCALE = 2  # supersampling factor for smooth ellipse edges
    BLUR_KERNEL = (13, 13)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for page in PAGES_DIR.glob('*.png'):
        page_num = int(REG_FILENAME.match(page.name).group(1))
        print(f'=== Page {page_num} ===')
        img = cv2.imread(str(page))

        # Convert to grayscale and blur
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blurred = cv2.blur(gray, BLUR_KERNEL)

        # Threshold (inverse binary) - light content becomes white, dark content becomes black
        thresh_val, thresh = cv2.threshold(blurred, WHITE_LEVEL_THRESHOLD, 255, cv2.THRESH_BINARY_INV)

        # Find contours and filter out small ones
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        large_contours = [cont for cont in contours if (AREA_MIN <= cv2.contourArea(cont) <= AREA_MAX)]

        # Draw elipses around acceptable contours
        portrait_contours = []  # list of (contour, ellipse, x, y, w, h)
        for contour in large_contours:
            ellipse = cv2.fitEllipse(contour)
            x, y, wc, hc = cv2.boundingRect(contour)
            hw_ratio = hc / wc if wc > 0 else 0

            ratio_ok = abs(hw_ratio - TARGET_HW_RATIO) <= HW_TOLERANCE

            if ratio_ok:
                portrait_contours.append((contour, ellipse, x, y, wc, hc))

        print(f'Found {len(portrait_contours)} portraits on page {page_num}')

        # Cut out portraits based on the contour ellipses
        for portrait_num, (contour, ellipse, x, y, wc, hc) in enumerate(portrait_contours):
            x1 = max(0, x)
            y1 = max(0, y)
            x2 = min(img.shape[1], x + wc)
            y2 = min(img.shape[0], y + hc)
            crop_bgr = img[y1:y2, x1:x2]

            crop_h, crop_w = crop_bgr.shape[:2]

            # ── Antialiased ellipse mask via supersampling ──────────────────
            mask_big = np.zeros((crop_h * SCALE, crop_w * SCALE), dtype=np.uint8)
            cx_big = (crop_w * SCALE) // 2
            cy_big = (crop_h * SCALE) // 2
            semi_a = int((crop_w * SCALE) // 2 * ELLIPSE_SHRINK)
            semi_b = int((crop_h * SCALE) // 2 * ELLIPSE_SHRINK)
            cv2.ellipse(mask_big, (cx_big, cy_big), (semi_a, semi_b),
                        0, 0, 360, 255, thickness=-1)
            mask = cv2.resize(mask_big, (crop_w, crop_h), interpolation=cv2.INTER_AREA)

            rgba = cv2.cvtColor(crop_bgr, cv2.COLOR_BGR2BGRA)
            rgba[:, :, 3] = mask

            # ── Place crop centered on a blank TARGET_W x TARGET_H canvas ──
            canvas = np.zeros((TARGET_H, TARGET_W, 4), dtype=np.uint8)

            # Clamp in case a portrait is larger than the target canvas
            paste_w = min(crop_w, TARGET_W)
            paste_h = min(crop_h, TARGET_H)

            cx_off = (TARGET_W - paste_w) // 2
            cy_off = (TARGET_H - paste_h) // 2

            canvas[cy_off:cy_off + paste_h, cx_off:cx_off + paste_w] = rgba[:paste_h, :paste_w]

            out_path = OUTPUT_DIR / f'p{page_num}_pn{portrait_num}.png'
            cv2.imwrite(str(out_path), rgba)
            print(f'Saved: {out_path}')


if __name__ == '__main__':
    extract_portraits_contour()
