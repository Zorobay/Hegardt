const API_BASE = `${process.env.VUE_APP_API_BASE_URL}/`;

const RECIPE_ALL = API_BASE + 'recipe/all';
const RECIPE_NAME = API_BASE + 'recipe/title/';

const PEOPLE_ID = API_BASE + 'person/id/';
const PEOPLE_ALL = API_BASE + 'person/all';
const PEOPLE_NAME = API_BASE + 'person/query/name/';
const PEOPLE_STATS = API_BASE + 'person/stats';

const USER_REGISTER = API_BASE + 'user/register';
const USER_AUTHENTICATE = API_BASE + 'user/authenticate';

import axios from 'axios';
import qs from 'qs';

const Service = {
  async _get(url) {
    console.log(`[GET] ${url}`);
    return axios(url)
        .then(res => res.data)
        .catch(err => console.error(err));
  },

  async _post(url, data) {
    console.log(`[POST] ${url}`);
    const config = {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    };
    const dataStr = qs.stringify(data);
    return axios.post(url, dataStr, config);
  },
};

const PeopleService = {

  ...Service,

  async getStats() {
    return this._get(PEOPLE_STATS);
  },

  async getPersonById(id) {
    return this._get(PEOPLE_ID + id);
  },

  async getPersonsByName(query) {
    return this._get(PEOPLE_NAME + query);
  },

  async getAllPersons() {
    return this._get(PEOPLE_ALL);
  },
};

export const UserService = {
  ...Service,

  async registerUser(user) {
    return this._post(USER_REGISTER, user);
  },

  async authenticateUser(user) {
    return this._post(USER_AUTHENTICATE, user);
  },
};

export const RecipeService = {
  ...Service,

  async getAllRecipes() {
    return this._get(RECIPE_ALL);
  },

  async getRecipeByTitle(title) {
    return this._get(RECIPE_NAME + title);
  },
};

export default PeopleService;
