def get_str_or(lst, pos, other):
    try:
        return lst[pos]
    except:
        return other


class MyLocation:

    def __init__(self, loc_str=""):

        self.loc_str = loc_str

        split = loc_str.split(",")
        self.city = get_str_or(split, 0, "")
        self.region = ""
        self.notes = ""

        if len(split) == 1:
            self.country = "Sverige"
        elif len(split) == 2:
            self.country = get_str_or(split, 1, "")
        elif len(split) == 3:
            self.region = get_str_or(split, 1, "")
            self.country = get_str_or(split, 2, "")

    def get_json(self):
        if self.loc_str == "" or self.loc_str is None:
            return None
        else:
            return {
                "country": self.country,
                "region": self.region,
                "city": self.city,
                "notes": self.notes
            }

    def __str__(self):
        return "MyLocation(" + self.city + ", " + self.region + ", " + self.country + ")"

    def __eq__(self, other):
        return self.city == other.city and self.region == other.region and self.country == other.country and self.notes == other.notes