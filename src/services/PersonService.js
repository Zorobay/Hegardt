import persons from '../db/persons.js';

export default class PersonService {

    constructor() {
        this._personsList = []
        debugger;
    }

    getPersonById(id) {
        return persons[id]
    }

    getAllPersons() {
        return persons
    }
}
