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
}

export default new PersonService()
