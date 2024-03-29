import {FETCH_ALL_PEOPLE, FETCH_COMPLETE_PERSON_BY_ID, FETCH_PERSON_BY_ID, FETCH_PERSON_BY_NAME} from './actions.type';
import PeopleService from '../common/api.service';
import {ADD_PERSON_TO_HASH, SET_ALL_PEOPLE} from './mutations.type';

export const state = {
  allPeopleFetched: false,
  peoples: [],
  personsHashMap: new Map(),
};

export const mutations = {
  [SET_ALL_PEOPLE](state, allPeople) {
    state.peoples = allPeople;
    state.allPeopleFetched = true;

    for (const p of allPeople) {
      const id = p._id;
      state.personsHashMap.set(id, p);
    }
  },
  [ADD_PERSON_TO_HASH](state, person) {
    if (person) state.personsHashMap.set(person._id, person);
  },
};

export const actions = {
  async [FETCH_PERSON_BY_ID](context, id) {
    // First, check if the person is in the hash map
    if (state.personsHashMap.has(id)) {
      return new Promise((resolve, reject) => {
        resolve(state.personsHashMap.get(id));
      });
    } else {
      return PeopleService.getPersonById(id)
          .then(person => {
            context.commit(ADD_PERSON_TO_HASH, person);
            return person;
          });
    }
  },
  async [FETCH_PERSON_BY_NAME](context, keyword) {
    const processed = keyword.split(' ').map(t => `(.*${t})`);
    const reg = new RegExp(processed, 'ig');

    if (false) { // Find people by filtering the existing collection
      const subset = state.peoples.filter(p => p.fullName.match(reg));
      return new Promise((resolve, reject) => {
        resolve(subset);
      });
    } else {
      return PeopleService.getPersonsByName(keyword)
          .then(person => {
            context.commit(ADD_PERSON_TO_HASH, person);
            return person;
          });
    }
  },
  async [FETCH_COMPLETE_PERSON_BY_ID](context, id) {
    return PeopleService.getCompletePersonById(id);
  },
  async [FETCH_ALL_PEOPLE](context) {
    return PeopleService.getAllPersons()
        .then(data => {
          if (data) {
            context.commit(SET_ALL_PEOPLE, data);
          }
          return data;
        });
  },
};

export const getters = {
  people(state) {
    return state.peoples;
  },
  allPeopleFetched(state) {
    return state.allPeopleFetched;
  },
};

export default {
  state,
  actions,
  mutations,
  getters,
};
