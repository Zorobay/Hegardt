import json
from pathlib import Path


def full_name(person: dict):
    first_name = person.get('firstName')
    last_name = person.get('lastName')
    middle_names = person.get('middleNames')
    return f'{first_name} {middle_names} {last_name}'

def person_identifier_str(person: dict, year: str, pid: str):
    return f'{full_name(person)} f. {year} -> id: {pid}'

if __name__ == '__main__':
    PORTRAITS_DIR = Path('contour_portraits')
    FINISHED_PORTRAITS_DIR = Path('../static_media/portraits')
    with open('persons.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    while True:
        birth_year = int(input('Birth: '))
        first_name = input('First name: ')
        year_check = False
        name_check = False
        found = []
        for _, person in data.items():
            date = person.get('birth').get('date')
            year = date.get('year') if date else None
            name = person.get('firstName')
            
            if year and year == birth_year and name and name.lower().strip() == first_name.lower().strip():
                found.append(person)
        
        selected = 0
        if not found:
            print('!No person found!')
            continue
        elif len(found) > 1:
            for i,person in enumerate(found):
                pid = person.get('id') + 1
                print(f'  {i}. {person_identifier_str(person, year, pid)}')
            selected = input('Multiple people matched. Select correct:')
        person = found[selected]
        page, pn = [e.strip() for e in input('Page and pn:').split(' ')]
        pid = person.get('id') + 1
        print(f'Found! {person_identifier_str(person, year, pid)}')
        filename = f'p{page}_pn{pn}.png'
        new_filename = f'id{pid}.png'
        (PORTRAITS_DIR / filename).rename(FINISHED_PORTRAITS_DIR/new_filename)
        print(f'Renamed {filename} -> {new_filename}')
        print('')