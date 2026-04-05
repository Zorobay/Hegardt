from datetime import date

class PartialDateModel:
    def __init__(self, json_data: dict = None):
        self.year = None
        self.month = None
        self.day = None
        self.date = None

        if not json_data:
            return

        self.year = json_data.get('year')
        self.month = json_data.get('month')
        self.day = json_data.get('day')
        self.date = self._compute_date()

    def _compute_date(self) -> date | None:
        if not self.year:
            return None
        return date(self.year, self.month or 1, self.day or 1)