from src.models.life_event_model import LifeEventModel
from src.models.marriage_model import MarriageModel
from src.models.occupation_model import OccupationModel
from src.sql_helpers import escape, sql_number, to_id

def normalize_name(name: str) -> str:
    import unicodedata
    nfd = unicodedata.normalize('NFD', name or '')
    stripped = ''.join(c for c in nfd if unicodedata.category(c) != 'Mn')
    return stripped.replace(' ', '').lower()

class PersonModel:
    def __init__(self, json_data: dict):
        self.id = to_id(json_data.get('id'))
        self.first_name = json_data.get('firstName', '')
        self.last_name = json_data.get('lastName', '')
        self.middle_names = ', '.join(json_data.get('middleNames') or [])
        self.normalized_name = normalize_name(' '.join([n for n in [self.first_name, ''.join(json_data.get('middleNames') or []), self.last_name] if n]))
        self.notes = json_data.get('notes', '')
        self.sex = json_data.get('sex', '').upper()
        self.father_id = to_id(json_data['father']) if json_data.get('father') else None
        self.mother_id = to_id(json_data['mother']) if json_data.get('mother') else None
        self.children_ids = [to_id(i) for i in json_data.get('children', [])]
        self.birth = LifeEventModel(json_data.get('birth')) if json_data.get('birth') else None
        self.death = LifeEventModel(json_data.get('death')) if json_data.get('death') else None
        self.burial = LifeEventModel(json_data.get('burial')) if json_data.get('burial') else None
        self.marriages = [MarriageModel(m) for m in json_data.get('marriages', [])]
        self.occupations = [OccupationModel(o) for o in json_data.get('occupations', [])]

        self.birth_id = None
        self.death_id = None
        self.burial_id = None
        
    def __str__(self):
        return f'Person(id: {self.id}, name: {self.first_name + " " + self.last_name})'

    def get_insert_life_event_sqls(self, life_event_start_id: int) -> tuple[str, int]:
        """Returns (sql_statements, updated_id_counter)"""
        life_event_id = life_event_start_id - 1
        sql_statements = []

        if self.birth:
            life_event_id += 1
            sql_statements.append(self.birth.get_insert_sql(life_event_start_id, None))
            self.birth_id = life_event_start_id

        if self.death:
            life_event_id += 1
            sql_statements.append(self.death.get_insert_sql(life_event_start_id, None))
            self.death_id = life_event_start_id

        if self.burial:
            life_event_id += 1
            sql_statements.append(self.burial.get_insert_sql(life_event_start_id, None))
            self.burial_id = life_event_start_id

        return '\n'.join(sql_statements), life_event_start_id

    def get_insert_person_sql(self) -> str:
        birth = sql_number(self.birth_id)
        death = sql_number(self.death_id)
        burial = sql_number(self.burial_id)
        return (
            f"INSERT INTO person (id, first_name, last_name, middle_names, normalized_name, notes, sex, "
            f"birth_id, death_id, burial_id, father_id, mother_id) "
            f"VALUES ({self.id}, '{escape(self.first_name)}', '{escape(self.last_name)}', "
            f"'{escape(self.middle_names)}', '{escape(self.normalized_name)}', '{escape(self.notes)}', '{self.sex}', "
            f"{birth}, {death}, {burial}, null, null);"
        )

    def get_insert_sql(self, location_id: int, life_event_id: int, occupation_id: int) -> tuple[str, int, int, int]:
        sql = [f'\n\n--======= Insert Person id: {self.id} =======']

        if self.birth:
            sql.append(self.birth.get_insert_location_sql(location_id))
            sql.append(self.birth.get_insert_sql(life_event_id, location_id))
            self.birth_id = life_event_id
            location_id = location_id + 1 if self.birth.location else location_id
            life_event_id += 1

        if self.death:
            sql.append(self.death.get_insert_location_sql(location_id))
            sql.append(self.death.get_insert_sql(life_event_id, location_id))
            self.death_id = life_event_id
            location_id = location_id + 1 if self.death.location else location_id
            life_event_id += 1

        if self.burial:
            sql.append(self.burial.get_insert_location_sql(location_id))
            sql.append(self.burial.get_insert_sql(life_event_id, location_id))
            self.burial_id = life_event_id
            location_id = location_id + 1 if self.burial.location else location_id
            life_event_id += 1

        for occupation in self.occupations:
            sql.append(occupation.get_insert_sql(occupation_id))
            occupation.id = occupation_id
            occupation_id += 1

        sql.append(self.get_insert_person_sql())
        sql = [s for s in sql if s]  # Remove None and empty lines
        return '\n'.join(sql), location_id, life_event_id, occupation_id

    def get_person_relations_sql(self) -> str:
        sql = []
        if self.father_id:
            sql.append(f"UPDATE person SET father_id = {self.father_id} WHERE id = {self.id};")
        if self.mother_id:
            sql.append(f"UPDATE person SET mother_id = {self.mother_id} WHERE id = {self.id};")

        sql = [s for s in sql if s]
        if len(sql) > 0:
            sql.insert(0, f'\n\n--======= Update Person id: {self.id} =======')
        return "\n".join(sql)
