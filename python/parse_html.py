import os
import sys
from python.Person import Person
from time import time
import json


def main():
    ppl = []
    file_nr = 0
    start = time()
    for root, dirs, files in os.walk("../Disgen/html"):
        for file in files:
            if "-" not in file and file.endswith(".htm") or file.endswith(".html"):
                p = os.path.join(root, file)
                file_nr += 1
                print("Processing [{}]: {}".format(file_nr, p))
                with open(p, 'r') as f:
                    try:
                        person = Person(f)
                        ppl.append(person.as_json())
                    except:
                        print("{}Error in file: {}{}".format('\033[91m', p, '\033[0m'))
                        return

    end = time()
    print("Finished parsing {} files in {:3g}s".format(file_nr, (end - start)))

    with open("all_ppl.json", 'w+', encoding='utf-16') as outfile:
        json.dump(ppl, outfile, ensure_ascii=False)

    print("Wrote output to [all_ppl.json]")


if __name__ == "__main__":
    main()

