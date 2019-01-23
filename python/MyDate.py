from datetime import datetime
import calendar


def get_to_int_or(lst, pos, other):
    try:
        return int(lst[pos])
    except:
        return None


class MyDate:

    def __init__(self, date_str=""):
        self.date_str = date_str

        self.year = None
        self.month = None
        self.day = None
        self.date = None

        self.set_date()

    def set_date(self):
        split = self.date_str.split('-')
        self.year = get_to_int_or(split, 0, None)
        self.month = get_to_int_or(split, 1, None)
        self.day = get_to_int_or(split, 2, None)
        try:
            d_year = self.year if self.year != None else 1
            d_month = self.month if self.month != None else 1
            d_day = self.day if self.day != None else 1
            self.date = datetime(d_year, d_month, d_day)
        except ValueError as e:
            if ("day is out of range for month" in str(e)):
                self.date = datetime(d_year, d_month, calendar.monthrange(d_year, d_month)[1])
            else:
                e.with_traceback()

    def get_json(self):
        if self.date_str is None or self.date_str == "":
            return None
        else:
            return {"date": self.date,
                    "year": self.year,
                    "month": self.month,
                    "day": self.day}

    def __str__(self):
        return "MyDate(" + self.year + "-" + self.month + "-" + self.day + ")"

    def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day
