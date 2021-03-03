export default class JSONPerson {

  constructor(person) {
    this.json_person = {};
    this.setPerson(person);
  }

  setPerson(person) {
    const a = this.toFamilyTreeJson(person);
    this.json_person = a;
  }

  setMother(mother) {
    this.json_person.mother = this.toFamilyTreeJson(mother);
  }

  setFather(father) {
    this.json_person.father = this.toFamilyTreeJson(father);
  }

  /**
   * Returns a simple JSON representation of this person with only the properties needed to draw a family tree.
   * @return {Object}
   */
  toFamilyTreeJson(person) {
    return JSONPerson.toSimpleJSON(person, ['id', 'full_name', 'mother', 'father', 'children', 'siblings', 'spouses']);
  }

  /**
   * Returns a simple JSON representation of a person with only the given properties.
   * @param {Object} person a person to convert to JSON
   * @param {Array} properties a list of properties of a person object to retain.
   * @return {Object} a simple JSON representation of person
   */
  static toSimpleJSON(person, properties) {
    if (!person) return null;
    if (!(person instanceof Object)) return person;
    const out = {};

    for (const prop of properties) {
      if (person.hasOwnProperty(prop)) {
        let data = null;
        switch (prop) {
          case 'mother': data = this.toSimpleJSON(person[prop], properties); break;
          case 'father': data = this.toSimpleJSON(person[prop], properties); break;
          case 'children': data = JSONPerson.listPropertyToJSON(person[prop], properties); break;
          case 'siblings': data = JSONPerson.listPropertyToJSON(person[prop], properties); break;
          case 'spouses': data = JSONPerson.listPropertyToJSON(person[prop], properties); break;
          default: data = person[prop];
        }
        out[prop] = data;
      }
    }

    return out;
  }

  static listPropertyToJSON(data, properties) {
    const out = [];
    const filtered = data.filter(d => !!d);
    if (filtered.length > 0) {
      filtered.forEach(d => out.push(JSONPerson.toSimpleJSON(d, properties)));
    }
    return out;
  }
}
