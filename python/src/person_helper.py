from src.PeopleSection import PeopleSection
from src.constants import START_PAGE, REG_NUMBER, REG_PEOPLE_SECTION


class PersonSimple:
    def __init__(self, first_name: str, birth_year: int | None, id: int):
        self.first_name: str = first_name.lower().strip()
        self.birth_year: int = birth_year
        self.person_id = id


MANUAL_PERSON_MAP = [
    PersonSimple('Johannes', 1743, 21),
    PersonSimple('en', None, 32),
    PersonSimple('Helena', 1767, 33),
    PersonSimple('Apollonia', 1827, 68),
    PersonSimple('Carl', 1826, 67),
    PersonSimple('Julia', 1857, 86),
    PersonSimple('Gunnar', 1893, 96),
    PersonSimple('Hillevi', 1926, 112),
    PersonSimple('Carl', 1923, 118),
    PersonSimple('Nils', 1925, 119),
    PersonSimple('Johannes', 1815, 75),
    PersonSimple('Karl', 1859, 179),
    PersonSimple('Oskar', 1850, 175),
    PersonSimple('Anna', 1871, 190),
    PersonSimple('Gustaf', 1882, 194),
    PersonSimple('Alma', 1884, 195),
    PersonSimple('Oskar', 1889, 197),
    PersonSimple('Agnes', 1892, 198),
    PersonSimple('Gerd', 1922, 221),
    PersonSimple('Ingrid', 1918, 234),
    PersonSimple('Gustaf', 1846, 299),
    PersonSimple('Katarina', 1770, 296),
    PersonSimple('Karl', 1799, 322),
    PersonSimple('Claire', 1898, 399),
    PersonSimple('Carl', 1857, 381),
    PersonSimple('Nelly', 1899, 412),
    PersonSimple('Märta', 1894, 415),
    PersonSimple('Klara', 1913, 421),
    PersonSimple('Lechard', 1859, 565),
    PersonSimple('Johan', 1857, 563),
    PersonSimple('En', 1895, 579),
    PersonSimple('Peter', 1687, 9),
    PersonSimple('Kornelius', 1715, 703),
    PersonSimple('En', 1763, 716),
    PersonSimple('Bernhard', 1832, 764),
    PersonSimple('Märta', 1890, 792),
    PersonSimple('William', 1860, 779),
    PersonSimple('Robert', 1905, 823),
    PersonSimple('Peter', 1748, 720),
    PersonSimple('Jöran', 1682, 932),
    PersonSimple('Jöran', 1714, 948),
    PersonSimple('Lovisa', 1736, 961),
    PersonSimple('Peter', 1742, 983),
    PersonSimple('Jöran', 1745, 985)

]

for person in MANUAL_PERSON_MAP:
    duplicate_name = [p for p in MANUAL_PERSON_MAP if
                      p.first_name == person.first_name and p.person_id != person.person_id]
    for dp in duplicate_name:
        assert dp.birth_year != person.birth_year, 'Duplicate first_name and birth_year!'


def find_person_id(persons_data: dict, person: PeopleSection) -> int | None:
    for key, item in persons_data.items():
        first_name = item['firstName']
        middle_names = [mn.lower() for mn in item['middleNames']]
        birth_date = item['birth']['date']
        if birth_date:
            birth_year = birth_date['year']

            if first_name.lower() == person.first_name.lower() and birth_year == person.birth_year:
                if person.middle_name:
                    if person.middle_name.lower() in middle_names:
                        return int(key) + 1  # The JSON Ids are 0 based, but the database starts from 1
                else:
                    return int(key) + 1  # The JSON Ids are 0 based, but the database starts from 1

    for mp in MANUAL_PERSON_MAP:
        if mp.first_name == person.first_name.lower() and mp.birth_year == person.birth_year:
            return mp.person_id

    return None


def extract_people_sections(page_text: str, book_page: int) -> list[PeopleSection]:
    start_index = 0
    missing_header = book_page == START_PAGE

    # Cut characters until first '1., 2. etc.'
    if not missing_header:
        if match := REG_NUMBER.search(page_text):
            start_index = match.start() + 1

    splits = REG_PEOPLE_SECTION.split(page_text[start_index:])
    return [PeopleSection(s, book_page) for s in splits]
