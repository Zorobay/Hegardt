import {CHANGE_MAPSETTINGS} from "./actions.type";
import {SET_MAPSETTINGS} from "./mutations.type";


export const state = {
  mapSettings: {
    checked: [],
    gender: {
      options: ["male", "female", "both"],
      selected: "both"
    },
    location: {
      options: ["Birth Location", "Death Location", "Bury Location"],
      selected: "Birth Location",
    }
  }
};

export const mutations = {
  [SET_MAPSETTINGS](state, settings) {
    state.mapSettings = settings;
  }
};

export const actions = {
  [CHANGE_MAPSETTINGS](context, settings) {
    context.commit(SET_MAPSETTINGS, settings);
  }
};

export const getters = {
  mapSettings(state) {
    return state.mapSettings;
  }
};

export default {
  state,
  actions,
  mutations,
  getters
};
