import os

from bs4 import BeautifulSoup

from python.Person import path_to_file_id
from time import time
import json
from bson import json_util

OUT_FILE = "all_genders.json"


def main():
    ppl = {}
    file_nr = 0
    start = time()
    for root, dirs, files in os.walk("../../hegardt"):
        for file in files:
            if "-" not in file and file.endswith(".htm") or file.endswith(".html"):
                p = os.path.join(root, file)
                file_nr += 1
                print("Processing [{}]: {}".format(file_nr, p))

                with open(p, 'r') as f:
                    try:
                        genders = extract_genders(f)
                        if genders:
                            for pid in genders:
                                if pid not in ppl:
                                    ppl[pid] = genders[pid]
                    except Exception as e:
                        print(e.with_traceback())
                        print("{}Error in file: {}{}".format('\033[91m', p, '\033[0m'))
                        return

    end = time()
    print("Finished parsing {} files in {:3g}s".format(file_nr, (end - start)))

    with open(OUT_FILE, 'w+', encoding='utf-8') as outfile:
        json.dump(ppl, outfile, ensure_ascii=False, default=json_util.default)

    print("Wrote output to [{}]".format(OUT_FILE))


def extract_genders(f) -> dict:
    genders = {}
    bs = BeautifulSoup(f.read(), 'html.parser')

    try:
        if "Ansedel" in bs.body.font.center.font.text:
            table = bs.find('table', {'border': '1'})
            cells = table.find_all('td')
            for c in cells:
                if c.a:
                    gender = string_to_gender(c.contents[0])
                    link_id = path_to_file_id(c.a.attrs['href'])
                    if gender:
                        genders[link_id] = gender
        else:
            return None
    except AttributeError:
        print("{} is not an 'Ansedel'".format(f.name))
        return None

    return genders


def string_to_gender(g):
    g = g.strip()
    if g in ['f', 'ff', 'mf']:
        return 'MAN'
    elif g in ['m', 'mm', 'fm']:
        return 'WOMAN'
    else:
        return ''


if __name__ == "__main__":
    main()
