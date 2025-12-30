import persons from '@/data/persons.ts';
import type { Person, PersonOptionalId, PersonsData } from '@/types/person.type.ts';
import { fuzzyMatch } from '@/helpers/util-helper.ts';
import { formatPersonFullName } from '@/helpers/person-helper.ts';

class PersonService {
  private readonly _data: PersonsData;
  private readonly _dataList: Person[] = [];

  constructor() {
    this._data = persons;
    this._dataList = this._personsToList(persons);
  }

  _personsToList(persons: PersonsData): Person[] {
    const out: Person[] = [];
    for (const id in persons) {
      const person: Person = persons[id];
      out.push(person);
    }
    return out;
  }

  getAllPersons(): PersonsData {
    return this._data;
  }

  getAllPersonsList(): Person[] {
    return this._dataList;
  }

  getPersonsByName(name: string): Person[] {
    return this._dataList.filter((p) => {
      const personFullName = formatPersonFullName(p);
      return fuzzyMatch(personFullName, name);
    });
  }

  getPersonById(id: PersonOptionalId): Person | null {
    if (!id) {
      return null;
    }
    return this._data[id];
  }

  getChilrenOfPersonById(id: PersonOptionalId): Person[] {
    const person = this.getPersonById(id);
    const out: Person[] = [];

    if (person) {
      const childIds: number[] = person.children;
      for (const childId of childIds) {
        const child = this.getPersonById(childId);
        if (child) {
          out.push(child);
        }
      }
    }
    return out;
  }

  getSiblingsOfPersonById(id: PersonOptionalId): Person[] {
    if (!id) {
      return [];
    }
    const person = this.getPersonById(id);
    const out = [];

    if (person) {
      const mother = this.getPersonById(person.mother);
      const father = this.getPersonById(person.father);

      const childrenIds = new Set([...(mother?.children ?? []), ...(father?.children ?? [])]);
      childrenIds.delete(id);
      for (const childId of childrenIds) {
        const child = this.getPersonById(childId);
        if (child) {
          out.push(child);
        }
      }
    }
    return out;
  }
}

export default new PersonService();
