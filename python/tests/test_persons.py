import os
import unittest

from python.Person import Person


class TestHelge(unittest.TestCase):
    """Helge has a lot of notes, 5 children and a wife. Birth and death are recorded."""

    def setUp(self):
        with open("../../Disgen/html/000/0000/419.htm", 'r') as file:
            self.person = Person(file)

        self.props = {
            "first_name": "Helge",
            "middle_name": ["Lechard"],
            "last_name": "Hegardt",
            "birth_date": "1897-04-13",
            "birth_loc": "Helsingborg",
            "death_date": "1964-08-22",
            "death_loc": "Lund",
            "bury_date": "",
            "bury_loc": "",
            "occupation": "Kontraktsprost",
            "notes": "(Tab 41:177 i GS).\nStudentexamen 1916 i Helsingborg. Teol fil examen 1922 och teol kand 1928 i Lund. Prakt teol prov 1929 samt prästvigd samma år. Missiv i Sturkö?Tjurkö pastorat i Blekinge 192931. Kyrkoherde i Sjörups och Katslösa pastorat i Malmöhus län vid Skånes sydkust 1931 med tillträde 1933. Avgick med pension 1961. Kontraktsprost i Ljunits och Herrestads kontrakt 1949.61. LVO.\nOrdförande i Sjörups och Katslösas barnavårdsnämnder och skolstyrelser 1932?52. Vid storkommunernas genomförande 1952 ordförande i Ljunits storkommuns skolstyrelse 1952-58. Hemvärnsman 1940?61 samt stf hemvärnsområdesbefälhavare från 1948. Hemvärnets tjänstemärken i silver, guld och guld med emalj samt tilldelad hemvärnets förtjänstmedalj i silver 1957.\n\"... Under prosten Hegardts studietid var den s k liberala teologien så gott som allenarådande. Som förkunnare har prosten förstått tillgodogöra sig det bestående i denna, men kastat loss från det tidsbestämda, utan att därför försvära sig åt någon viss teologisk eller kyrklig moderiktning. Ej heller är han benägen att utan vidare införa nyheter i församlingsarbetet. Kritiskt betraktar han allt nytt efterhand som det kommer fram och avgör själv, vad han anser sig böra acceptera.\nDet går väl samman med hans frimodiga väsen som alltid gjort honom uppskattad liksom hans tjänstaktighet och oföränderligt vänliga sätt mot alla. Han har därför blivit värderad i alla kretsar och förvärvat sig tillgivna vänner inom sina församlingar och vida omkring ....\" (Y A 13/4 1957 vid H:s 60?årsdag.) \"... Vi, hans gamla kontraktister, glömmer aldrig hur glatt och vänligt han tog emot oss i Sjörups prästgård antingen vi kom till kvartalskonventet eller för att bara hälsa på. Som kontraktsprost var han aldrig den stränge chefen. Han föredrog att leda oss med mild hand och i synnerhet våra konvent begagnade han sig av för att i samtalets form få fason på våra gemensamma angelägenheter och företag. Det må nu ha gällt församlingslivet eller samlingen i kontraktssammanhang.\nFör min inre blick ser jag Helge Hegardt stå där mitt ibland oss och med ett gott, någon gång spjuveraktigt, leende göra sina tillägg och om så behövdes gjuta olja på de heta diskussionens heta vågor. Och när jag ser honom så,slår det mig att det ligger något symboliskt i att han fick en god bråd död. Ett långsamt avtynande hade på något sätt inte gått ihop med hans livfulla personlighet....\nUnder den tid prosten Hegardt verkade i Sjörup och Katslösa satt han intill kommunindelningsreformen som skolrådsordförande i båda församlingarna och genomförde en väsentlig förbättring av skolväsendet där. Ljunits storkommun visste också att begagna sig av den erfarne skolmannen. Prosten Hegardt var sålunda ordförande i Ljunits skolstyrelse sedan dess tillkomst.\nFöre storkommuns tid var prosten Hegardt i många år ordförande i Sjörups och Katslösa barnavårdsnämnder. Han var också kyrkostämmornas ordförande. I dessa befattningar och som ordförande i församlingarnas kyrkoråd visade han sig alltid mån om kyrkorna. Ett synligt resultat härav var bland andra den pietetsfulla restaureringen av Sjörups vackra kyrka....\nMatlagskamraterna under hans vistelse vid universitetet i Lund spådde att teologie studeranden Helge Hegardt skulle bli kontraktsprost. Också anförtrodde honom stiftets biskop den 5 oktober 1959 det vördiga prostämbetet i Ljunits och Herrestads kontrakt. För den initierade kom denna utnämning inte som en överraskning. ....\" (SDS 25/8 1964)",
            "file_id": "000/0000/419.htm",
            "spouses": [("000/0000/422.htm", "1929-06-05", "Lund")],
            "father": "000/0000/409.htm",
            "mother": "000/0000/417.htm",
            "children": ["000/0000/423.htm", "000/0000/424.htm", "000/0000/426.htm", "000/0000/427.htm",
                         "000/0000/429.htm"],
            "references": []
        }

    def test_first_name(self):
        self.assertEqual(self.props["first_name"], self.person.first_name)

    def test_middle_name(self):
        names = self.person.middle_names
        self.assertListEqual(self.props["middle_name"], names)

    def test_last_name(self):
        self.assertEqual(self.props["last_name"], self.person.last_name)

    def test_birth_date(self):
        self.assertEqual(self.props["birth_date"], self.person.birth_date)

    def test_birth_loc(self):
        self.assertEqual(self.props["birth_loc"], self.person.birth_loc)

    def test_death_date(self):
        self.assertEqual(self.props["death_date"], self.person.death_date)

    def test_death_loc(self):
        self.assertEqual(self.props["death_loc"], self.person.death_loc)

    def test_bury_date(self):
        self.assertEqual(self.props["bury_date"], self.person.bury_date)

    def test_bury_loc(self):
        self.assertEqual(self.props["bury_loc"], self.person.bury_loc)

    def test_occupation(self):
        self.assertEqual(self.props["occupation"], self.person.occupation)

    def test_notes(self):
        self.assertEqual(self.props["notes"], self.person.notes)

    def test_file(self):
        self.assertEqual(self.props["file_id"], self.person.file_id)

    def test_spouses(self):
        self.assertListEqual(self.props["spouses"], self.person.spouses)

    def test_father(self):
        self.assertEqual(self.props["father"], self.person.father)

    def test_mother(self):
        self.assertEqual(self.props["mother"], self.person.mother)

    def test_children(self):
        self.assertListEqual(self.props["children"], self.person.children)

    def test_references(self):
        self.assertEqual(self.props["references"], self.person.references)


class TestJurgen(TestHelge):
    """Jurgen is very simple. No kids or wife, birth or death recorded."""

    def setUp(self):
        with open('../../Disgen/html/000/0000/006.htm') as file:
            self.person = Person(file)

        self.props = {
            "first_name": "Christian",
            "middle_name": ["Jürgen"],
            "last_name": "Hegardt",
            "birth_date": "",
            "birth_loc": "",
            "death_date": "",
            "death_loc": "",
            "bury_date": "",
            "bury_loc": "",
            "occupation": "",
            "notes": "Den tredje av de söner, som nämns i Peters dagbok.",
            "file_id": "000/0000/006.htm",
            "spouses": [],
            "father": "000/0000/003.htm",
            "mother": "000/0000/005.htm",
            "children": [],
            "references": ["se Peters dagbok"]
        }


class TestChristian(TestHelge):
    """Christian have had TWO wives!"""

    def setUp(self):
        with open("../../Disgen/html/000/0000/423.htm", 'r') as file:
            self.person = Person(file)

        self.props = {
            "first_name": "Christian",
            "middle_name": ["Lechard"],
            "last_name": "Hegardt",
            "birth_date": "1930-04-12",
            "birth_loc": "Lund",
            "death_date": "1996-07-13",
            "death_loc": "Abbekås, Skivarp",
            "bury_date": "",
            "bury_loc": "",
            "occupation": "Ingenjör",
            "notes": "Ingenjörsexamen 1953 i Malmö (M).\nAnställd 1955 vid Tetra Pak AB i Lund. Under åren 1958-64 servicechef för Tetra Pak i Toronto, Canada. Sedan 1964 tillbaka vid Tetra Pak i Lund.",
            "file_id": "000/0000/423.htm",
            "spouses": [("000/0000/430.htm", "1958-06-20", "Skellefteå"),
                        ("000/0000/602.htm", "1992-07-04", "ombord på S/Y Gita II")],
            "father": "000/0000/419.htm",
            "mother": "000/0000/422.htm",
            "children": ["000/0000/431.htm", "000/0000/432.htm", "000/0000/433.htm"],
            "references": []
        }


class TestAnna(TestHelge):
    """Christian have had TWO wives!"""

    def setUp(self):
        with open("../../Disgen/html/000/0001/240.htm", 'r') as file:
            self.person = Person(file)

        self.props = {
            "first_name": "Anna",
            "middle_name": [],
            "last_name": "Aquilonia",
            "birth_date": "1708-10-14",
            "birth_loc": "",
            "death_date": "1755-12-06",
            "death_loc": "Håslöv",
            "bury_date": "",
            "bury_loc": "",
            "occupation": "",
            "notes": "",
            "file_id": "000/0001/240.htm",
            "spouses": [("000/0001/433.htm", "", ""), ("000/0001/217.htm", "1737-02-15", "Håslöv")],
            "father": "000/0001/241.htm",
            "mother": "000/0001/242.htm",
            "children": ["000/0001/432.htm", "000/0001/434.htm", "000/0001/435.htm",
                         "000/0001/243.htm", "000/0001/244.htm", "000/0001/246.htm", "000/0001/247.htm",
                         "000/0001/248.htm"],
            "references": []
        }


class TestMorsing(TestHelge):
    """Morsing only has one name and a marriage, nothing else!"""

    def setUp(self):
        with open("../../Disgen/html/000/0001/433.htm", 'r') as file:
            self.person = Person(file)

        self.props = {
            "first_name": "",
            "middle_name": [],
            "last_name": "Morsing",
            "birth_date": "",
            "birth_loc": "",
            "death_date": "",
            "death_loc": "",
            "bury_date": "",
            "bury_loc": "",
            "occupation": "",
            "notes": "",
            "file_id": "000/0001/433.htm",
            "spouses": [("000/0001/240.htm", "", "")],
            "father": "",
            "mother": "",
            "children": ["000/0001/432.htm", "000/0001/434.htm", "000/0001/435.htm"],
            "references": []
        }


class TestBotel(TestHelge):
    """
    Extra info in header, like bury info.
    """

    def setUp(self):
        with open("../../Disgen/html/000/0000/002.htm", 'r') as file:
            self.person = Person(file)

        self.props = {
            "first_name": "Botel",
            "middle_name": [],
            "last_name": "Hegardt",
            "birth_date": "",
            "birth_loc": "",
            "death_date": "1610",
            "death_loc": "",
            "bury_date": "1610",
            "bury_loc": "Ö Höjst, Danmark",
            "occupation": "",
            "notes": "",
            "file_id": "000/0000/002.htm",
            "spouses": [],
            "father": "000/0000/001.htm",
            "mother": "",
            "children": [],
            "references": []
        }


class TestUnknown(TestHelge):
    """
    Unknown person without name or parents. Has a spouse however.
    """

    def setUp(self):
        with open("../../Disgen/html/000/0000/465.htm", 'r') as file:
            self.person = Person(file)

        self.props = {
            "first_name": "",
            "middle_name": [],
            "last_name": "",
            "birth_date": "",
            "birth_loc": "",
            "death_date": "",
            "death_loc": "",
            "bury_date": "",
            "bury_loc": "",
            "occupation": "",
            "notes": "Oforskat Fullständiga uppgifter (sid 1).\nOforskat Fullständiga uppgifter om föräldrar (sid 4).",
            "file_id": "000/0000/465.htm",
            "spouses": [("000/0000/103.htm", "", "")],
            "father": "",
            "mother": "",
            "children": ["000/0000/104.htm", "000/0000/150.htm"],
            "references": []
        }


class TestNonExisting(TestHelge):
    """Completely empty"""

    def setUp(self):
        with open("../../Disgen/html/000/0000/908.htm", 'r') as file:
            self.person = Person(file)

        self.props = {
            "first_name": "",
            "middle_name": [],
            "last_name": "",
            "birth_date": "",
            "birth_loc": "",
            "death_date": "",
            "death_loc": "",
            "bury_date": "",
            "bury_loc": "",
            "occupation": "",
            "notes": "",
            "file_id": "000/0000/908.htm",
            "spouses": [],
            "father": "",
            "mother": "",
            "children": [],
            "references": []
        }


class TestArvid(TestHelge):
    """Weird format for death"""

    def setUp(self):
        with open("../../Disgen/html/000/0001/046.htm", 'r') as file:
            self.person = Person(file)

        self.props = {
            "first_name": "Arvid",
            "middle_name": [],
            "last_name": "Ausell",
            "birth_date": "1750",
            "birth_loc": "",
            "death_date": "1802-03-01",
            "death_loc": "på sin gård Håkanstorp",
            "bury_date": "",
            "bury_loc": "",
            "occupation": "Kyrkoinspektör",
            "notes": "",
            "file_id": "000/0001/046.htm",
            "spouses": [
                ("000/0001/045.htm", "1783-10-05", "Malmö")
            ],
            "father": "",
            "mother": "",
            "children": [],
            "references": []
        }


class TestWaaraGrape(TestHelge):
    """Unique last name with dash."""

    def setUp(self):
        with open("../../Disgen/html/000/0000/430.htm", 'r') as file:
            self.person = Person(file)

        self.props = {
            "first_name": "Elna",
            "middle_name": ["Birgitta"],
            "last_name": "Waara-Grape",
            "birth_date": "1933-02-21",
            "birth_loc": "Skellefteå",
            "death_date": "1988-06-14",
            "death_loc": "Lund",
            "bury_date": "",
            "bury_loc": "",
            "occupation": "Fil dr",
            "notes": "",
            "file_id": "000/0000/430.htm",
            "spouses": [
                (
                    "000/0000/423.htm",
                    "1958-06-20",
                    "Skellefteå"
                )
            ],
            "father": "000/0000/477.htm",
            "mother": "000/0000/478.htm",
            "children": [
                "000/0000/431.htm",
                "000/0000/432.htm",
                "000/0000/433.htm"
            ],
            "references": []
        }


class TestAnna(TestHelge):
    """Has a death with lot of information."""

    def setUp(self):
        with open("../../Disgen/html/000/0000/022.htm", 'r') as file:
            self.person = Person(file)

        self.props = {
            "first_name": "Anna",
            "middle_name": [
                "Elisabeth"
            ],
            "last_name": "Bratt",
            "birth_date": "1753-06-12",
            "birth_loc": "Uddevalla",
            "death_date": "1835-03-10",
            "death_loc": "på Annegreteberg i Uddevalla",
            "bury_date": "",
            "bury_loc": "",
            "occupation": "",
            "notes": "",
            "file_id": "000/0000/022.htm",
            "spouses": [
                (
                    "000/0000/017.htm",
                    "1774-09-13",
                    "Uddevalla"
                )
            ],
            "father": "000/0000/484.htm",
            "mother": "000/0000/485.htm",
            "children": [
                "000/0000/588.htm",
                "000/0000/032.htm",
                "000/0000/033.htm",
                "000/0000/200.htm",
                "000/0000/034.htm",
                "000/0000/036.htm",
                "000/0000/038.htm"
            ],
            "references": []
        }


class TestAfÅminne(TestHelge):
    """Last name with 'af'"""

    def setUp(self):
        with open("../../Disgen/html/000/0001/306.htm", 'r') as file:
            self.person = Person(file)

        self.props = {
            "first_name": "Anna",
            "middle_name": [
                "Regina",
                "Horn"
            ],
            "last_name": "af Åminne",
            "birth_date": "1718-03-07",
            "birth_loc": "",
            "death_date": "1796-11-21",
            "death_loc": "på Berga i Högsby",
            "bury_date": "",
            "bury_loc": "",
            "occupation": "Friherrinna",
            "notes": "",
            "file_id": "000/0001/306.htm",
            "spouses": [
                (
                    "000/0001/305.htm",
                    "1762",
                    ""
                )
            ],
            "father": "000/0001/307.htm",
            "mother": "000/0001/308.htm",
            "children": [],
            "references": []
        }


class TestHorn(TestHelge):
    def setUp(self):
        with open("../../Disgen/html/000/0001/307.htm", 'r') as file:
            self.person = Person(file)

        self.props = {
            "first_name": "Christer",
            "middle_name": [],
            "last_name": "Horn",
            "birth_date": "",
            "birth_loc": "",
            "death_date": "",
            "death_loc": "",
            "bury_date": "",
            "bury_loc": "",
            "occupation": "Överste, friherre",
            "notes": "",
            "file_id": "000/0001/307.htm",
            "spouses": [
                (
                    "000/0001/308.htm",
                    "",
                    ""
                )
            ],
            "father": "",
            "mother": "",
            "children": [
                "000/0001/306.htm"
            ],
            "references": []
        }


class TestCarlos(TestHelge):
    def setUp(self):
        with open("../../Disgen/html/000/0000/304.htm", 'r') as file:
            self.person = Person(file)

        self.props = {
            "first_name": "Carlos",
            "middle_name": [
                "Alfonso",
                "José"
            ],
            "last_name": "Garcia-Hegardt",
            "birth_date": "1946-07-30",
            "birth_loc": "Zaragosa, Spanien",
            "death_date": "",
            "death_loc": "",
            "bury_date": "",
            "bury_loc": "",
            "occupation": "Licenciat i kemi",
            "notes": "Adress Calle del Rio 31-9 D, Miranda de Ebro, Burgos, Spanien.\nBor i Burgos, Spanien.",
            "file_id": "000/0000/304.htm",
            "spouses": [
                (
                    "000/0000/305.htm",
                    "1973-07-02",
                    "Barbastro, Spanien"
                )
            ],
            "father": "000/0000/294.htm",
            "mother": "000/0000/293.htm",
            "children": [
                "000/0000/312.htm",
                "000/0000/313.htm",
                "000/0000/314.htm"
            ],
            "references": []
        }
