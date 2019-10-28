const API_BASE = "https://hegardt-backend.herokuapp.com/";
const PEOPLE_ID = API_BASE + "person/id/";
const PEOPLE_ALL = API_BASE + "person/all";
const PEOPLE_NAME = API_BASE + "person/query/name/";
const PEOPLE_STATS = API_BASE + "person/stats";

import axios from "axios";

const PeopleService = {

  async _get(url) {
    return axios(url)
      .then(res => res.data)
      .catch(err => console.error(err));
  },

  async getStats() {
    return this._get(PEOPLE_STATS);
  },

  async getPersonById(id) {
    return this._get(PEOPLE_ID + id);
  },

  async getPeopleByName(query) {
    return this._get(PEOPLE_NAME + query);
  },

  async getAllPeople() {
    return this._get(PEOPLE_ALL);
  }
};

export default PeopleService;
