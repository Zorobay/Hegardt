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
            "occupation": "Kontraktsprost",
            "notes": "(Tab 41:177 i GS).\nStudentexamen 1916 i Helsingborg. Teol fil examen 1922 och teol kand 1928 i Lund. Prakt teol prov 1929 samt prästvigd samma år. Missiv i Sturkö?Tjurkö pastorat i Blekinge 192931. Kyrkoherde i Sjörups och Katslösa pastorat i Malmöhus län vid Skånes sydkust 1931 med tillträde 1933. Avgick med pension 1961. Kontraktsprost i Ljunits och Herrestads kontrakt 1949.61. LVO. Ordförande i Sjörups och Katslösas barnavårdsnämnder och skolstyrelser 1932?52. Vid storkommunernas genomförande 1952 ordförande i Ljunits storkommuns skolstyrelse 1952-58. Hemvärnsman 1940?61 samt stf hemvärnsområdesbefälhavare från 1948. Hemvärnets tjänstemärken i silver, guld och guld med emalj samt tilldelad hemvärnets förtjänstmedalj i silver 1957. \"... Under prosten Hegardts studietid var den s k liberala teologien så gott som allenarådande. Som förkunnare har prosten förstått tillgodogöra sig det bestående i denna, men kastat loss från det tidsbestämda, utan att därför försvära sig åt någon viss teologisk eller kyrklig moderiktning. Ej heller är han benägen att utan vidare införa nyheter i församlingsarbetet. Kritiskt betraktar han allt nytt efterhand som det kommer fram och avgör själv, vad han anser sig böra acceptera. Det går väl samman med hans frimodiga väsen som alltid gjort honom uppskattad liksom hans tjänstaktighet och oföränderligt vänliga sätt mot alla. Han har därför blivit värderad i alla kretsar och förvärvat sig tillgivna vänner inom sina församlingar och vida omkring ....\" (Y A 13/4 1957 vid H:s 60?årsdag.) \"... Vi, hans gamla kontraktister, glömmer aldrig hur glatt och vänligt han tog emot oss i Sjörups prästgård antingen vi kom till kvartalskonventet eller för att bara hälsa på. Som kontraktsprost var han aldrig den stränge chefen. Han föredrog att leda oss med mild hand och i synnerhet våra konvent begagnade han sig av för att i samtalets form få fason på våra gemensamma angelägenheter och företag. Det må nu ha gällt församlingslivet eller samlingen i kontraktssammanhang. För min inre blick ser jag Helge Hegardt stå där mitt ibland oss och med ett gott, någon gång spjuveraktigt, leende göra sina tillägg och om så behövdes gjuta olja på de heta diskussionens heta vågor. Och när jag ser honom så,slår det mig att det ligger något symboliskt i att han fick en god bråd död. Ett långsamt avtynande hade på något sätt inte gått ihop med hans livfulla personlighet.... Under den tid prosten Hegardt verkade i Sjörup och Katslösa satt han intill kommunindelningsreformen som skolrådsordförande i båda församlingarna och genomförde en väsentlig förbättring av skolväsendet där. Ljunits storkommun visste också att begagna sig av den erfarne skolmannen. Prosten Hegardt var sålunda ordförande i Ljunits skolstyrelse sedan dess tillkomst. Före storkommuns tid var prosten Hegardt i många år ordförande i Sjörups och Katslösa barnavårdsnämnder. Han var också kyrkostämmornas ordförande. I dessa befattningar och som ordförande i församlingarnas kyrkoråd visade han sig alltid mån om kyrkorna. Ett synligt resultat härav var bland andra den pietetsfulla restaureringen av Sjörups vackra kyrka.... Matlagskamraterna under hans vistelse vid universitetet i Lund spådde att teologie studeranden Helge Hegardt skulle bli kontraktsprost. Också anförtrodde honom stiftets biskop den 5 oktober 1959 det vördiga prostämbetet i Ljunits och Herrestads kontrakt. För den initierade kom denna utnämning inte som en överraskning. ....\" (SDS 25/8 1964)",
            "file_id": "000/0000/419.htm",
            "spouses": [("000/0000/422.htm", "1929-06-05", "Lund")],
            "father": "000/0000/409.htm",
            "mother": "000/0000/417.htm",
            "children": ["000/0000/423.htm", "000/0000/424.htm", "000/0000/426.htm", "000/0000/427.htm",
                         "000/0000/429.htm"]
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
            "occupation": "",
            "notes": "Den tredje av de söner, som nämns i Peters dagbok.",
            "file_id": "000/0000/006.htm",
            "spouses": [],
            "father": "000/0000/003.htm",
            "mother": "000/0000/005.htm",
            "children": []
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
            "occupation": "Ingenjör",
            "notes": "Ingenjörsexamen 1953 i Malmö (M).\nAnställd 1955 vid Tetra Pak AB i Lund. Under åren 1958-64 servicechef för Tetra Pak i Toronto, Canada. Sedan 1964 tillbaka vid Tetra Pak i Lund.",
            "file_id": "000/0000/423.htm",
            "spouses": [("000/0000/430.htm", "1958-06-20", "Skellefteå"),
                        ("000/0000/602.htm", "1992-07-04", "ombord på S/Y Gita II")],
            "father": "000/0000/419.htm",
            "mother": "000/0000/422.htm",
            "children": ["000/0000/431.htm", "000/0000/432.htm", "000/0000/433.htm"]
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
            "occupation": "",
            "notes": "",
            "file_id": "000/0001/240.htm",
            "spouses": [("000/0001/433.htm", "", ""), ("000/0001/217.htm", "1737-02-15", "Håslöv")],
            "father": "000/0001/241.htm",
            "mother": "000/0001/242.htm",
            "children": ["000/0001/432.htm", "000/0001/434.htm", "000/0001/435.htm",
                         "000/0001/243.htm", "000/0001/244.htm", "000/0001/246.htm", "000/0001/247.htm",
                         "000/0001/248.htm"]
        }