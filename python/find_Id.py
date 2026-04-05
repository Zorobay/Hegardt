import json
from pathlib import Path


def full_name(person: dict):
    first_name = person.get('firstName')
    last_name = person.get('lastName')
    middle_names = person.get('middleNames')
    return f'{first_name} {middle_names} {last_name}'


if __name__ == '__main__':
    PORTRAITS_DIR = Path('contour_portraits')
    with open('persons.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    while True:
        birth_year = int(input('Birth: '))
        first_name = input('First name: ')
        year_check = False
        name_check = False
        found = False
        for _, person in data.items():
            date = person.get('birth').get('date')
            year = date.get('year') if date else None
            if year and year == birth_year:
                year_check = True
            name = person.get('firstName')
            if name and name.lower().strip() == first_name.lower().strip():
                name_check = True
                
            if year_check and name_check:
                found = True
                page, pn = [e.strip() for e in input('Page and pn:').split(' ')]
                pid = person.get('id') + 1
                print(f'Found! {full_name(person)} f. {year} -> id: {pid}')
                filename = f'p{page}_pn{pn}.png'
                new_filename = f'id{pid}.png'
                (PORTRAITS_DIR / filename).rename(PORTRAITS_DIR/new_filename)
                print(f'Renamed {filename} -> {new_filename}')
                break
        if not found:
            print('!No person found!')
        print('')