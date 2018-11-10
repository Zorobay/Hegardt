from bs4 import BeautifulSoup
import re


# Declare regex
reg_name = re.compile("\w+", re.IGNORECASE | re.UNICODE)

def parse_person(html):


def main():
    with open("ansedel_christian.html", 'r') as file:
        html = file.read()

    person = parse_person(html)

if __name__ == "__main__":
    main()

