import persons from "@/data/persons.js";

class PersonService {

  constructor() {
    this._data = persons
    this._dataList = this._personsToList(persons)
  }

  _personsToList(persons) {
    let out = []
    for (const id in persons) {
      const person = persons[id]
      out.push(person)
    }
    return out
  }

  getAllPersonsList() {
    return this._dataList
  }

  getPersonById(id) {
    return this._data[id]
  }

  getChilrenOfPersonById(id) {
    const person = this.getPersonById(id);
    const out = [];

    if (person) {
      const childIds = person.children;
      for(const childId of childIds) {
        out.push(this.getPersonById(childId));
      }
    }
    return out;
  }

  getSiblingsOfPersonById(id) {
    const person = this.getPersonById(id);
    const out = [];

    if (person) {
      const mother = this.getPersonById(person.mother);
      const father = this.getPersonById(person.father);

      const childrenIds = new Set([...mother?.children, ...father?.children]);
      for (const childId of childrenIds) {
        out.push(this.getPersonById(childId));
      }
    }
    return out;
  }
}

export default new PersonService()
