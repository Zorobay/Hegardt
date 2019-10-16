import {FETCH_ALL_PEOPLE, FETCH_PEOPLE_BY_NAME} from "./actions.type";
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
  async [FETCH_PEOPLE_BY_NAME](context, keyword) {
    return PeopleService.getPeopleByName()
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
