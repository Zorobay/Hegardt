/* Correct spelling of Mickaël af Christiernin */
UPDATE person
SET first_name = 'Mikaël',
    updated_at = NOW()
WHERE id = 80;

/* Correct birthday of Sebastian Hegardt's*/
UPDATE life_event le
SET partial_month = 1,
    partial_day   = 15,
    partial_date  = '1994-01-15',
    updated_at    = NOW()
FROM person p
WHERE p.birth_id = le.id
  AND p.id = 619;

/* Correct last name of Josias Hegardt's "En Dotter" */
UPDATE person
SET first_name = 'Unknown',
    last_name  = 'Hegardt',
    sex        = 'WOMAN',
    updated_at = NOW()
WHERE id = 32;

/* Correct last name of Oskar Hegardt (prev. Hagardt) */
UPDATE person
SET last_name  = 'Hegardt',
    updated_at = NOW()
WHERE id = 197;

/* Add apostrophe to middle name for Agnes Linnéa */
UPDATE person
SET middle_names = 'Linnéa',
    updated_at   = NOW()
WHERE id = 198;

/* Add apostrophe to middle name for Ingrid Linnéa */
UPDATE person
SET middle_names = 'Linnéa, Maria',
    updated_at   = NOW()
WHERE id = 234;

/* Move first name to middle name and add first name of Katarina Cecilia Hegardt */
UPDATE person
SET first_name   = 'Katarina',
    middle_names = 'Cecilia',
    updated_at   = NOW()
WHERE id = 296;

/* Add apostrophes to middle name of Claire Hélène Hegardt */
UPDATE person
SET middle_names = 'Hélène',
    updated_at   = NOW()
WHERE id = 399;

/* Correct first name spelling of Carl Vilhelm Hegardt */
UPDATE person
SET first_name = 'Carl',
    updated_at = NOW()
WHERE id = 381;

/* Correct first name of Nelly Margareta Hegardt */
UPDATE person
SET first_name = 'Nelly',
    updated_at = NOW()
WHERE id = 412;

/* Correct spelling of first name of Klara Elisabet Hegardt */
UPDATE person
SET first_name = 'Klara',
    updated_at = NOW()
WHERE id = 421;

/* Update spelling of middle name for Lechard Jonathan Hegardt */
UPDATE person
SET middle_names = 'Jonathan',
    updated_at   = NOW()
WHERE id = 565;

/* Correct first and last name for En Son */
UPDATE person
SET first_name = 'En Son',
    last_name  = 'Hegardt',
    updated_at = NOW()
WHERE id = 579;

/* Correct first name of Kornelius Hegardt */
UPDATE person
SET first_name = 'Kornelius',
    updated_at = NOW()
WHERE id = 703;

/* Correct first and last name for En Son (b. 1763) */
UPDATE person
SET first_name = 'En Son',
    last_name  = 'Hegardt',
    updated_at = NOW()
WHERE id = 716;

/* Correct birth date of Bernhard Hegardt */
UPDATE life_event AS le
SET partial_year = 1832,
    partial_date = MAKE_DATE(1832, COALESCE(partial_month, 1), COALESCE(partial_day, 1)),
    updated_at   = NOW()
FROM person AS p
WHERE p.birth_id = le.id
  AND p.id = 764;

/* Add missing middle name to Märta Sigrid Hegardt */
UPDATE person
SET middle_names = 'Sigrid',
    updated_at=NOW()
WHERE id = 792;

/* Add missing middle name to William Gustaf Hegardt */
UPDATE person
SET middle_names= 'Gustaf',
    updated_at  = NOW()
WHERE id = 779;

/* Update middle name of Robert Raviler Hegardt */
UPDATE person
SET middle_names='Raviler',
    updated_at  = NOW()
WHERE id = 823;

/* Update first name and middle name of Lovisa Sofia Charlotta Hegardt */
UPDATE person
SET first_name  = 'Lovisa',
    middle_names= 'Sofia, Charlotta',
    last_name   = NOW()
WHERE id = 961;

/* TODO !! Fixa Klara Adela (Adèle) mellannamn (smeknamn)?*/

/* TODO Fix id 105 nickname (Hanna) */