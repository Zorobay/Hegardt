from src.sql_helpers import escape, sql_number

FETCH_STATUS_MAP = {
    'FETCHED': 'FETCHED_WITH_SUCCESS',
    'NOT_FETCHED': 'AWAITING',
    'FAILED': 'FETCHED_WITH_ERRORS',
    None: 'AWAITING'
}

class LocationModel:
    def __init__(self, json_data: dict):
        if not json_data:
            return
        self.city = json_data.get('city', '')
        self.country = json_data.get('country', '')
        self.region = json_data.get('region', '')
        self.notes = json_data.get('notes', '')
        self.latitude = json_data.get('latitude')
        self.longitude = json_data.get('longitude')
        self.fetch_status = self._map_fetch_status(json_data.get('fetchStatus'))

    def get_insert_sql(self, id: int) -> str:
        lat = sql_number(self.latitude)
        lon = sql_number(self.longitude)
        return (
            f"INSERT INTO location (id, city, country, region, notes, latitude, longitude, fetch_status) "
            f"VALUES ({id}, '{escape(self.city)}', '{escape(self.country)}', '{escape(self.region)}', "
            f"'{escape(self.notes)}', {lat}, {lon}, '{escape(self.fetch_status)}');"
        )

    @staticmethod
    def _map_fetch_status(fetch_status: str) -> str:
        if fetch_status not in FETCH_STATUS_MAP:
            raise ValueError(f"Could not map '{fetch_status}' to fetch_status ordinal")
        return FETCH_STATUS_MAP[fetch_status]