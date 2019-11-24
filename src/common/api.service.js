//const API_BASE = "https://hegardt-backend.herokuapp.com/";
const API_BASE = "http://localhost:3000/";

const PEOPLE_ID = API_BASE + "person/id/";
const PEOPLE_ALL = API_BASE + "person/all";
const PEOPLE_NAME = API_BASE + "person/query/name/";
const PEOPLE_STATS = API_BASE + "person/stats";

const USER_REGISTER = API_BASE + "user/register";
const USER_AUTHENTICATE = API_BASE + "user/authenticate";

import axios from 'axios';
import qs from 'qs';

const Service = {
  async _get(url) {
    return axios(url)
      .then(res => res.data)
      .catch(err => console.error(err));
  },

  async _post(url, data) {
    const config = {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      }
    };
    let data_str = qs.stringify(data);
    return axios.post(url, data_str, config);
  }
};

const PeopleService = {

  ...Service,

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

export const UserService = {
  ...Service,

  async registerUser(user) {
    return this._post(USER_REGISTER, user);
  },

  async authenticateUser(user) {
    return this._post(USER_AUTHENTICATE, user);
  }
};

export default PeopleService;
