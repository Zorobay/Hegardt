/* Spell Mickaël af Christiernin correct */
UPDATE person
SET first_name = 'Mikaël',
    updated_at = NOW()
WHERE id = 80;

/* Update Sebastian Hegardt's birthday */
UPDATE life_event le
SET partial_month = 1,
    partial_day   = 15,
    partial_date  = '1994-01-15',
    updated_at    = NOW()
FROM person p
WHERE p.birth_id = le.id
  AND p.id = 619;