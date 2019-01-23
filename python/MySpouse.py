from python.MyDate import MyDate
from python.MyLocation import MyLocation


class MySpouse:

    def __init__(self, spouse_id="", date="", location=""):
        self.date = MyDate(date)
        self.location = MyLocation(location)
        self.spouse_id = spouse_id

    def get_json(self):
        if self.spouse_id == "":
            return None
        else:
            return {
                "_id": self.spouse_id,
                "marriage_date": self.date.get_json(),
                "location": self.location.get_json(),
            }

    def __eq__(self, other):
        return self.date == other.date and self.location == other.location and self.spouse_id == other.spouse_id
