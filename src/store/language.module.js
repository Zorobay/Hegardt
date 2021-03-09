import {SET_LANGUAGE, SET_LANGUAGE_DICT} from './mutations.type';
import {CHANGE_LANGUAGE} from './actions.type';
import {LanguageService} from '@/common/api.service';
import language from '@/common/enums/language';


export const state = {
  language: language.ENGLISH,
  languageDict: {},
};

export const actions = {
  [CHANGE_LANGUAGE](context, lang) {
    if (Object.values(language).includes(lang)) {
      context.commit(SET_LANGUAGE, lang);
      LanguageService.getLanguageFile(`${lang}.json`)
          .then(data => {
            context.commit(SET_LANGUAGE_DICT, data);
          })
          .catch(err => {
            console.error(`Failed to retrieve language file ${lang}.json\nReason: ${err}`);
          });
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
