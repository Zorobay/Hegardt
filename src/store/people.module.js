import {FETCH_ALL_PEOPLE, FETCH_PEOPLE_BY_ID, FETCH_PEOPLE_BY_NAME} from "./actions.type";
import PeopleService from "../common/api.service";
import {SET_ALL_PEOPLE} from "./mutations.type";


export const state = {
  allPeopleFetched: false,
  peoples: [],
  globalMsg: "Fök ya'll"
};

export const mutations = {
  [SET_ALL_PEOPLE](state, allPeople) {
    state.peoples = allPeople;
    state.allPeopleFetched = true;
  }
};

export const actions = {
  async [FETCH_PEOPLE_BY_ID](context, id) {
    if (state.allPeopleFetched) {
      let subset = state.peoples.filter(p => p._id.match(id));
      return new Promise((resolve, reject) => {
        if (subset.length > 0){
          resolve(subset[0]);
        } else {
          reject(`No person found for id [${id}]`);
        }
      })
    } else {
      return PeopleService.getPersonById(id);
    }
  },
  async [FETCH_PEOPLE_BY_NAME](context, keyword) {
    if (state.allPeopleFetched) {     // Find people by filtering the existing collection
      let reg = new RegExp(keyword, 'ig');
      let subset = state.peoples.filter(p => p.full_name.match(reg));
      return new Promise((resolve, reject) => {
        resolve(subset);
      });
    } else {
        return PeopleService.getPeopleByName(keyword)
    }
  },
  async [FETCH_ALL_PEOPLE](context) {
    return PeopleService.getAllPeople()
      .then(data => {
        context.commit(SET_ALL_PEOPLE, data);
        return data;
      });
  }
};

export const getters = {
  people(state) {
    return state.peoples;
  },
  allPeopleFetched(state) {
    return state.allPeopleFetched;
  }
};

export default {
  state,
  actions,
  mutations,
  getters
};
