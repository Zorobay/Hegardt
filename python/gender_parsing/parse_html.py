import json
import os
from pathlib import Path
from time import time

from bs4 import BeautifulSoup
from bson import json_util

from python.Person import path_to_file_id

FILEPATH = Path() / "python" / "all_ppl.json"
OUTFILE = FILEPATH / ".." / "all_ppl_with_sex.json"


def main():
    file_nr = 0
    start = time()
    with open(FILEPATH, "r", encoding="utf-8") as f_read:
        all_ppl = json.loads(f_read.read())
        all_ppl = all_ppl_to_dict(all_ppl)
        for root, dirs, files in os.walk("hegardt"):
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
                                    new_sex = genders[pid]
                                    old_sex = all_ppl[pid]["sex"]
                                    if old_sex not in ["", None] and old_sex != new_sex:
                                        raise RuntimeError("Sexes for file_id {} do not match! {} != {}".format(pid, old_sex, new_sex))
                                    all_ppl[pid]["sex"] = new_sex

                        except Exception as e:
                            print("{}Error in file: {}{}".format('\033[91m', p, '\033[0m'))
                            raise e

    end = time()
    print("Finished parsing {} files in {:3g}s".format(file_nr, (end - start)))

    all_ppl = reset_all_ppl_to_list(all_ppl)
    i = 0
    for p in all_ppl:
        if p["sex"] in ["", None]:
            i += 1

    print("{} persons are missing gender!".format(i))

    with open(OUTFILE, 'w+', encoding='utf-8') as outfile:
        json.dump(all_ppl, outfile, ensure_ascii=False, default=json_util.default)

    print("Wrote output to {}".format(OUTFILE.resolve()))


def all_ppl_to_dict(all_ppl: list) -> dict:
    out = dict()
    for p in all_ppl:
        f_id = p["file_id"]
        out[f_id] = p
    return out


def reset_all_ppl_to_list(all_ppl: dict) -> list:
    out = list()
    for pid in all_ppl:
        out.append(all_ppl[pid])
    return out


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
