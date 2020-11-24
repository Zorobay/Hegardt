export default class ConditionModel {
  constructor() {
    this.conditions = {};
  }

  addCondition(key, value) {
    this.conditions[key] = value;
  }

  evaluate(obj) {
    for (const k in this.conditions) {
      if (obj[k] === undefined || obj[k] !== this.conditions[k]) {
        return false;
      }
    }
    return true;
  }
}
