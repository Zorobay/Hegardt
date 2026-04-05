from src.sql_helpers import sql_string, sql_number, to_id
from src.models.location_model import LocationModel
from src.models.partial_date_model import PartialDateModel


class MarriageModel:
    def __init__(self, json_data: dict):
        self.spouse_id = to_id(json_data['personId']) if json_data.get('personId') else None
        self.date = PartialDateModel(json_data.get('date'))
        self.location = LocationModel(json_data['location']) if json_data.get('location') else None

    def get_insert_sql(self, spouse1_id:int, spouse2_id:int, location_id: int):
        sql = []
        resolved_location_id = 'null'
        if self.location:
            sql.append(self.location.get_insert_sql(location_id))
            resolved_location_id = location_id
            
        date = sql_string(self.date.date)
        sql.append(f"INSERT INTO marriage (spouse_1_id, spouse_2_id, location_id, partial_day, partial_month, partial_year, partial_date) VALUES ({spouse1_id}, {spouse2_id}, {resolved_location_id}, {sql_number(self.date.day)}, {sql_number(self.date.month)}, {sql_number(self.date.year)}, {date});")
        return '\n'.join(sql)
