import json
from datetime import datetime

from src.models.marriage_model import MarriageModel
from src.models.person_model import PersonModel

location_id = 1
life_event_id = 1
occupation_id = 1
sql = []


def marriage_key(id1: int, id2: int) -> tuple:
    return min(id1, id2), max(id1, id2)


with open("persons.json", "r", encoding="utf-8") as f:
    data = json.load(f)

persons: list[PersonModel] = []
sequence_reset = []

for key_id, person_data in data.items():
    person = PersonModel(person_data)
    persons.append(person)
    
# Sort persons by id
persons.sort(key = lambda p: p.id)

# Add disabling of triggers for speed
sql.append("\n\n--========== Disable triggers ==========\n")
sql.append("ALTER TABLE person DISABLE TRIGGER ALL;\n")
sql.append("ALTER TABLE life_event DISABLE TRIGGER ALL;\n")
sql.append("ALTER TABLE location DISABLE TRIGGER ALL;\n")
sql.append("ALTER TABLE occupation DISABLE TRIGGER ALL;\n")

# Add initial insert rows
for person in persons:
    person_sql, location_id, life_event_id, occupation_id = person.get_insert_sql(location_id, life_event_id,
                                                                                  occupation_id)
    sql.append(person_sql)

# Add update rows for person -> person relations
for person in persons:
    sql.append(person.get_person_relations_sql())

# Create non duplicate marriage entities
all_marriages: dict[tuple[int, int], MarriageModel] = {}
for person in persons:
    for marriage in person.marriages:
        key = marriage_key(person.id, marriage.spouse_id)
        if key not in all_marriages:
            all_marriages[key] = marriage

# Insert marriages (no duplicates)
for key, marriage in all_marriages.items():
    marriage_sql = [
        f'\n\n--======= Insert Marriage between id: {key[0]} and id: {key[1]} =======',
        marriage.get_insert_sql(key[0], key[1], location_id)
    ]
    location_id = location_id + 1 if marriage.location else location_id
    marriage_sql = [s for s in marriage_sql if s]
    sql.append('\n'.join(marriage_sql))

sql.append("\n\n--========== Resetting Sequences ============")
sql.append("\nSELECT setval('person_seq', (SELECT MAX(id) FROM person));")
sql.append("\nSELECT setval('life_event_seq', (SELECT MAX(id) FROM life_event));")
sql.append("\nSELECT setval('location_seq', (SELECT MAX(id) FROM location));")
sql.append("\nSELECT setval('occupation_seq', (SELECT MAX(id) FROM occupation));")

# Enable triggers
# Add disabling of triggers for speed
sql.append("\n\n--========== Re-enable triggers ==========\n")
sql.append("ALTER TABLE person ENABLE TRIGGER ALL;\n")
sql.append("ALTER TABLE life_event ENABLE TRIGGER ALL;\n")
sql.append("ALTER TABLE location ENABLE TRIGGER ALL;\n")
sql.append("ALTER TABLE occupation ENABLE TRIGGER ALL;\n")

output_path = "../micronaut/src/main/resources/db/migration/V2__seed_persons.sql"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(f"--============ Auto-generated seed file ({datetime.now()}) ================")
    f.writelines(sql)

print(f"Done! Written to {output_path}")
print(f"Persons: {len(data)}")
