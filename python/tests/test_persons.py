import os
import unittest

from python.Person import Person
from python.MyDate import MyDate
from python.MyLocation import MyLocation
from python.MySpouse import MySpouse


class TestHelge(unittest.TestCase):
    """Helge has a lot of notes, 5 children and a wife. Birth and death are recorded."""

    def setUp(self):
        with open("../../Disgen/html/000/0000/419.htm", 'r') as file:
            self.person = Person(file)

        self.props = {
            "first_name": "Helge",
            "middle_name": ["Lechard"],
            "last_name": "Hegardt",
            "birth_date": MyDate("1897-04-13"),
            "birth_location": MyLocation("Helsingborg"),
            "death_date": MyDate("1964-08-22"),
            "death_location": MyLocation("Lund"),
            "bury_date": MyDate(""),
            "bury_location": MyLocation(""),
            "occupation": ["Kontraktsprost"],
            "notes": "(Tab 41:177 i GS).\nStudentexamen 1916 i Helsingborg. Teol fil examen 1922 och teol kand 1928 i Lund. Prakt teol prov 1929 samt prästvigd samma år. Missiv i Sturkö?Tjurkö pastorat i Blekinge 192931. Kyrkoherde i Sjörups och Katslösa pastorat i Malmöhus län vid Skånes sydkust 1931 med tillträde 1933. Avgick med pension 1961. Kontraktsprost i Ljunits och Herrestads kontrakt 1949.61. LVO.\nOrdförande i Sjörups och Katslösas barnavårdsnämnder och skolstyrelser 1932?52. Vid storkommunernas genomförande 1952 ordförande i Ljunits storkommuns skolstyrelse 1952-58. Hemvärnsman 1940?61 samt stf hemvärnsområdesbefälhavare från 1948. Hemvärnets tjänstemärken i silver, guld och guld med emalj samt tilldelad hemvärnets förtjänstmedalj i silver 1957.\n\"... Under prosten Hegardts studietid var den s k liberala teologien så gott som allenarådande. Som förkunnare har prosten förstått tillgodogöra sig det bestående i denna, men kastat loss från det tidsbestämda, utan att därför försvära sig åt någon viss teologisk eller kyrklig moderiktning. Ej heller är han benägen att utan vidare införa nyheter i församlingsarbetet. Kritiskt betraktar han allt nytt efterhand som det kommer fram och avgör själv, vad han anser sig böra acceptera.\nDet går väl samman med hans frimodiga väsen som alltid gjort honom uppskattad liksom hans tjänstaktighet och oföränderligt vänliga sätt mot alla. Han har därför blivit värderad i alla kretsar och förvärvat sig tillgivna vänner inom sina församlingar och vida omkring ....\" (Y A 13/4 1957 vid H:s 60?årsdag.) \"... Vi, hans gamla kontraktister, glömmer aldrig hur glatt och vänligt han tog emot oss i Sjörups prästgård antingen vi kom till kvartalskonventet eller för att bara hälsa på. Som kontraktsprost var han aldrig den stränge chefen. Han föredrog att leda oss med mild hand och i synnerhet våra konvent begagnade han sig av för att i samtalets form få fason på våra gemensamma angelägenheter och företag. Det må nu ha gällt församlingslivet eller samlingen i kontraktssammanhang.\nFör min inre blick ser jag Helge Hegardt stå där mitt ibland oss och med ett gott, någon gång spjuveraktigt, leende göra sina tillägg och om så behövdes gjuta olja på de heta diskussionens heta vågor. Och när jag ser honom så,slår det mig att det ligger något symboliskt i att han fick en god bråd död. Ett långsamt avtynande hade på något sätt inte gått ihop med hans livfulla personlighet....\nUnder den tid prosten Hegardt verkade i Sjörup och Katslösa satt han intill kommunindelningsreformen som skolrådsordförande i båda församlingarna och genomförde en väsentlig förbättring av skolväsendet där. Ljunits storkommun visste också att begagna sig av den erfarne skolmannen. Prosten Hegardt var sålunda ordförande i Ljunits skolstyrelse sedan dess tillkomst.\nFöre storkommuns tid var prosten Hegardt i många år ordförande i Sjörups och Katslösa barnavårdsnämnder. Han var också kyrkostämmornas ordförande. I dessa befattningar och som ordförande i församlingarnas kyrkoråd visade han sig alltid mån om kyrkorna. Ett synligt resultat härav var bland andra den pietetsfulla restaureringen av Sjörups vackra kyrka....\nMatlagskamraterna under hans vistelse vid universitetet i Lund spådde att teologie studeranden Helge Hegardt skulle bli kontraktsprost. Också anförtrodde honom stiftets biskop den 5 oktober 1959 det vördiga prostämbetet i Ljunits och Herrestads kontrakt. För den initierade kom denna utnämning inte som en överraskning. ....\" (SDS 25/8 1964)",
            "file_id": "0000000419",
            "spouses": [MySpouse("0000000422", "1929-06-05", "Lund")],
            "father": "0000000409",
            "mother": "0000000417",
            "children": ["0000000423", "0000000424", "0000000426", "0000000427",
                         "0000000429"],
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

    def test_birth_location(self):
        self.assertEqual(self.props["birth_location"], self.person.birth_location)

    def test_death_date(self):
        self.assertEqual(self.props["death_date"], self.person.death_date)

    def test_death_location(self):
        self.assertEqual(self.props["death_location"], self.person.death_location)

    def test_bury_date(self):
        self.assertEqual(self.props["bury_date"], self.person.bury_date)

    def test_bury_location(self):
        self.assertEqual(self.props["bury_location"], self.person.bury_location)

    def test_occupation(self):
        self.assertListEqual(self.props["occupation"], self.person.occupation)

    def test_notes(self):
        self.assertEqual(self.props["notes"], self.person.notes)

    def test_file(self):
        self.assertEqual(self.props["file_id"], self.person.file_id)

    def test_spouses(self):
        self.assertListEqual(self.props["spouses"], [sp for sp in self.person.spouses])

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
            "birth_date": MyDate(""),
            "birth_location": MyLocation(""),
            "death_date": MyDate(""),
            "death_location": MyLocation(""),
            "bury_date": MyDate(""),
            "bury_location": MyLocation(""),
            "occupation": [""],
            "notes": "Den tredje av de söner, som nämns i Peters dagbok.",
            "file_id": "0000000006",
            "spouses": [],
            "father": "0000000003",
            "mother": "0000000005",
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
            "birth_date": MyDate("1930-04-12"),
            "birth_location": MyLocation("Lund"),
            "death_date": MyDate("1996-07-13"),
            "death_location": MyLocation("Abbekås, Skivarp"),
            "bury_date": MyDate(""),
            "bury_location": MyLocation(""),
            "occupation": ["Ingenjör"],
            "notes": "Ingenjörsexamen 1953 i Malmö (M).\nAnställd 1955 vid Tetra Pak AB i Lund. Under åren 1958-64 servicechef för Tetra Pak i Toronto, Canada. Sedan 1964 tillbaka vid Tetra Pak i Lund.",
            "file_id": "0000000423",
            "spouses": [MySpouse("0000000430", "1958-06-20", "Skellefteå"),
                        MySpouse("0000000602", "1992-07-04", "ombord på S/Y Gita II")],
            "father": "0000000419",
            "mother": "0000000422",
            "children": ["0000000431", "0000000432", "0000000433"],
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
            "birth_date": MyDate("1708-10-14"),
            "birth_location": MyLocation(""),
            "death_date": MyDate("1755-12-06"),
            "death_location": MyLocation("Håslöv"),
            "bury_date": MyDate(""),
            "bury_location": MyLocation(""),
            "occupation": "",
            "notes": "",
            "file_id": "0000001240",
            "spouses": [MySpouse("0000001433", "", ""), MySpouse("0000001217", "1737-02-15", "Håslöv")],
            "father": "0000001241",
            "mother": "0000001242",
            "children": ["0000001432", "0000001434", "0000001435",
                         "0000001243", "0000001244", "0000001246", "0000001247",
                         "0000001248"],
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
            "birth_date": MyDate(""),
            "birth_location": MyLocation(""),
            "death_date": MyDate(""),
            "death_location": MyLocation(""),
            "bury_date": MyDate(""),
            "bury_location": MyLocation(""),
            "occupation": [""],
            "notes": "",
            "file_id": "0000001433",
            "spouses": [MySpouse("0000001240", "", "")],
            "father": "",
            "mother": "",
            "children": ["0000001432", "0000001434", "0000001435"],
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
            "birth_date": MyDate(""),
            "birth_location": MyLocation(""),
            "death_date": MyDate("1610"),
            "death_location": MyLocation(""),
            "bury_date": MyDate("1610"),
            "bury_location": MyLocation("Ö Höjst, Danmark"),
            "occupation": [""],
            "notes": "",
            "file_id": "0000000002",
            "spouses": [],
            "father": "0000000001",
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
            "birth_date": MyDate(""),
            "birth_location": MyLocation(""),
            "death_date": MyDate(""),
            "death_location": MyLocation(""),
            "bury_date": MyDate(""),
            "bury_location": MyLocation(""),
            "occupation": [""],
            "notes": "Oforskat Fullständiga uppgifter (sid 1).\nOforskat Fullständiga uppgifter om föräldrar (sid 4).",
            "file_id": "0000000465",
            "spouses": [MySpouse("0000000103", "", "")],
            "father": "",
            "mother": "",
            "children": ["0000000104", "0000000150"],
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
            "birth_date": MyDate(""),
            "birth_location": MyLocation(""),
            "death_date": MyDate(""),
            "death_location": MyLocation(""),
            "bury_date": MyDate(""),
            "bury_location": MyLocation(""),
            "occupation": [""],
            "notes": "",
            "file_id": "0000000908",
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
            "birth_date": MyDate("1750"),
            "birth_location": MyLocation(""),
            "death_date": MyDate("1802-03-01"),
            "death_location": MyLocation("på sin gård Håkanstorp"),
            "bury_date": MyDate(""),
            "bury_location": MyLocation(""),
            "occupation": ["Kyrkoinspektör"],
            "notes": "",
            "file_id": "0000001046",
            "spouses": [
                MySpouse("0000001045", "1783-10-05", "Malmö")
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
            "birth_date": MyDate("1933-02-21"),
            "birth_location": MyLocation("Skellefteå"),
            "death_date": MyDate("1988-06-14"),
            "death_location": MyLocation("Lund"),
            "bury_date": MyDate(""),
            "bury_location": MyLocation(""),
            "occupation": ["Fil dr"],
            "notes": "",
            "file_id": "0000000430",
            "spouses": [MySpouse("0000000423", "1958-06-20", "Skellefteå")],
            "father": "0000000477",
            "mother": "0000000478",
            "children": [
                "0000000431",
                "0000000432",
                "0000000433"
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
            "birth_date": MyDate("1753-06-12"),
            "birth_location": MyLocation("Uddevalla"),
            "death_date": MyDate("1835-03-10"),
            "death_location": MyLocation("på Annegreteberg i Uddevalla"),
            "bury_date": MyDate(""),
            "bury_location": MyLocation(""),
            "occupation": [""],
            "notes": "",
            "file_id": "0000000022",
            "spouses": [
                MySpouse(
                    "0000000017",
                    "1774-09-13",
                    "Uddevalla"
                )
            ],
            "father": "0000000484",
            "mother": "0000000485",
            "children": [
                "0000000588",
                "0000000032",
                "0000000033",
                "0000000200",
                "0000000034",
                "0000000036",
                "0000000038"
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
            "birth_date": MyDate("1718-03-07"),
            "birth_location": MyLocation(""),
            "death_date": MyDate("1796-11-21"),
            "death_location": MyLocation("på Berga i Högsby"),
            "bury_date": MyDate(""),
            "bury_location": MyLocation(""),
            "occupation": ["Friherrinna"],
            "notes": "",
            "file_id": "0000001306",
            "spouses": [
                MySpouse(
                    "0000001305",
                    "1762",
                    ""
                )
            ],
            "father": "0000001307",
            "mother": "0000001308",
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
            "birth_date": MyDate(""),
            "birth_location": MyLocation(""),
            "death_date": MyDate(""),
            "death_location": MyLocation(""),
            "bury_date": MyDate(""),
            "bury_location": MyLocation(""),
            "occupation": ["Överste", "Friherre"],
            "notes": "",
            "file_id": "0000001307",
            "spouses": [
                MySpouse(
                    "0000001308",
                    "",
                    ""
                )
            ],
            "father": "",
            "mother": "",
            "children": [
                "0000001306"
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
            "birth_date": MyDate("1946-07-30"),
            "birth_location": MyLocation("Zaragosa, Spanien"),
            "death_date": MyDate(""),
            "death_location": MyLocation(""),
            "bury_date": MyDate(""),
            "bury_location": MyLocation(""),
            "occupation": ["Licenciat i kemi"],
            "notes": "Adress Calle del Rio 31-9 D, Miranda de Ebro, Burgos, Spanien.\nBor i Burgos, Spanien.",
            "file_id": "0000000304",
            "spouses": [
                MySpouse(
                    "0000000305",
                    "1973-07-02",
                    "Barbastro, Spanien"
                )
            ],
            "father": "0000000294",
            "mother": "0000000293",
            "children": [
                "0000000312",
                "0000000313",
                "0000000314"
            ],
            "references": []
        }
