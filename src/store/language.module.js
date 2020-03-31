import {SET_LANGUAGE, SET_LANGUAGE_DICT} from './mutations.type';
import {CHANGE_LANGUAGE} from './actions.type';

export const state = {
  language: 'en',
  languageDict: {},
};

export const actions = {
  [CHANGE_LANGUAGE](context, lang) {
    if (lang === 'en' || lang === 'se') {
      context.commit(SET_LANGUAGE, lang);
      const xhr = new XMLHttpRequest();
      xhr.open('GET', `/lang/${lang}.json`, false);
      // xhr.responseType = 'json';
      xhr.onload = function() {
        if (xhr.status !== 200) {
          console.error(`Failed to retrieve language file ${lang}.json`);
        } else {
          try {
            context.commit(SET_LANGUAGE_DICT, JSON.parse(xhr.responseText));
          } catch (e) {
            console.error('Could not parse response as JSON: ' + xhr.responseText);
          }
        }
      };

      xhr.send();
    }
  },
};

export const mutations = {
  [SET_LANGUAGE](state, lang) {
    state.language = lang;
  },
  [SET_LANGUAGE_DICT](state, langDict) {
    state.languageDict = langDict;
  },
};

export const getters = {
  language(state) {
    return state.language;
  },
  languageDict(state) {
    return state.languageDict;
  },
};

export default {
  state,
  actions,
  mutations,
  getters,
};
