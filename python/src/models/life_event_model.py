from src.models.location_model import LocationModel
from src.models.partial_date_model import PartialDateModel
from src.sql_helpers import escape, sql_string, sql_number


class LifeEventModel:
    def __init__(self, json_data: dict):
        if not json_data:
            self.notes = ''
            self.date = PartialDateModel()
            self.location = None
            return

        self.notes = json_data.get('notes', '')
        self.date = PartialDateModel(json_data.get('date'))
        self.location = LocationModel(json_data['location']) if json_data.get('location') else None

    def get_insert_location_sql(self, location_id: int) -> str | None:
        return self.location.get_insert_sql(location_id) if self.location else None

    def get_insert_sql(self, id: int, location_id: int | None) -> str:
        day = sql_number(self.date.day)
        month = sql_number(self.date.month)
        year = sql_number(self.date.year)
        date = sql_string(self.date.date)
        loc = location_id if self.location is not None else 'null'
        return (
            f"INSERT INTO life_event (id, partial_day, partial_month, partial_year, partial_date, notes, location_id) "
            f"VALUES ({id}, {day}, {month}, {year}, {date}, '{escape(self.notes)}', {loc});"
        )
