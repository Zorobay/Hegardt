import Vue from 'vue';
import Vuex from 'vuex';
import people from './people.module';
import language from './language.module';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    people,
    language
  },
});
