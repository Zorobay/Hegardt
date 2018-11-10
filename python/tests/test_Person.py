import unittest

from python.Person import Person


class TestPerson(unittest.TestCase):

    def setUp(self):
        with open("ansedel_christian.html", 'r') as file:
            self.person = Person(file)

    def test_first_name(self):
        self.assertEqual("Christian", self.person.first_name)

    def test_middle_name(self):
        names = self.person.middle_names
        self.assertEqual(1, len(names))
        self.assertEqual("Lechard", names[0])

    def test_last_name(self):
        self.assertEqual("Hegardt", self.person.last_name)

    def test_birth_date(self):
        self.assertEqual("1930-04-12", self.person.birth_date)

    def test_birth_loc(self):
        self.assertEqual("Lund", self.person.birth_loc)

    def test_death_date(self):
        self.assertEqual("1996-07-13", self.person.death_date)

    def test_death_loc(self):
        self.assertEqual("Abbekås, Skivarp", self.person.death_loc)

    def test_occupation(self):
        self.assertEqual("Ingenjör", self.person.occupation)

    def test_notes(self):
        notes = "Ingenjörsexamen 1953 i Malmö (M).\nAnställd 1955 vid Tetra Pak AB i Lund. Under åren 1958-64 " \
                "servicechef för Tetra Pak i Toronto, Canada. Sedan 1964 tillbaka vid Tetra Pak i Lund."
        self.assertEqual(notes, self.person.notes)
