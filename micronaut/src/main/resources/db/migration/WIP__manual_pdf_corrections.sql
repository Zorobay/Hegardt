UPDATE pdf_reference
SET height = LEAST(14.0, height);

/* ===== Page 15 ===== */
UPDATE pdf_reference
SET width = 353.65
WHERE person_id = 32
  AND pdf_page = 15;

/* ===== Page 16 ===== */
UPDATE pdf_reference
SET y0 = 185
WHERE person_id = 42
  AND pdf_page = 16;

UPDATE pdf_reference
SET y0 = 560
WHERE person_id = 43
  AND pdf_page = 16;

/* ===== Page 19 ===== */
UPDATE pdf_reference
SET y0 = 260
WHERE person_id = 67
  AND pdf_page = 19;

/* ===== Page 20 ===== */
UPDATE pdf_reference
SET y0 = 187
WHERE person_id = 88
  AND pdf_page = 20;

UPDATE pdf_reference
SET y0 = 233
WHERE person_id = 89
  AND pdf_page = 20;

UPDATE pdf_reference
SET y0 = 279
WHERE person_id = 90
  AND pdf_page = 20;

/* ===== Page 24 ===== */
UPDATE pdf_reference
SET y0 = 435
WHERE person_id = 73
  AND pdf_page = 24;

UPDATE pdf_reference
SET y0 = 468
WHERE person_id = 74
  AND pdf_page = 24;

UPDATE pdf_reference
SET y0 = 500
WHERE person_id = 75
  AND pdf_page = 24;

/* ===== Page 27 ===== */
UPDATE pdf_reference
SET y0 = 220
WHERE person_id = 195
  AND pdf_page = 27;

UPDATE pdf_reference
SET y0 = 550
WHERE person_id = 200
  and pdf_page=27;

/* ===== Page 30 ===== */
UPDATE pdf_reference
SET y0 = 230
WHERE person_id = 207
  and pdf_page=30;

UPDATE pdf_reference
SET y0 = 296
WHERE person_id = 209
  and pdf_page=30;

UPDATE pdf_reference
SET y0 = 310
WHERE person_id = 210
  and pdf_page=30;

/* ===== Page 34 ===== */
UPDATE pdf_reference
SET y0 = 365.0
WHERE person_id = 301
  AND pdf_page = 34;

UPDATE pdf_reference
SET y0 = 353
WHERE person_id = 300
  AND pdf_page = 34;