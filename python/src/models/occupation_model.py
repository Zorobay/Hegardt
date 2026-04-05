from src.sql_helpers import escape


class OccupationModel:
    def __init__(self, notes: str):
        self.id = None
        self.notes = notes
        self.location = None
        self.date = None

    def get_insert_sql(self, id: int) -> str:
        return (
            f"INSERT INTO occupation (id, notes, partial_day, partial_month, partial_year, partial_date, location_id) "
            f"VALUES ({id}, '{escape(self.notes)}', null, null, null, null, null);"
        )
