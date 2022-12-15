import {CHANGE_MAP_SETTINGS} from './actions.type';
import {SET_MAP_SETTINGS} from './mutations.type';


export const state = {
  mapSettings: {
    checked: [],
    gender: {
      options: ['male', 'female', 'both'],
      selected: 'both',
    },
    location: {
      options: ['Birth Location', 'Death Location', 'Bury Location'],
      selected: 'Birth Location',
    },
  },
};

export const mutations = {
  [SET_MAP_SETTINGS](state, settings) {
    state.mapSettings = settings;
  },
};

export const actions = {
  [CHANGE_MAP_SETTINGS](context, settings) {
    context.commit(SET_MAP_SETTINGS, settings);
  },
};

export const getters = {
  mapSettings(state) {
    return state.mapSettings;
  },
};

export default {
  state,
  actions,
  mutations,
  getters,
};
