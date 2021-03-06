import Vue from 'vue';
import Vuex from 'vuex';
import people from './people.module';
import recipes from './recipe.module';
import language from './language.module';
import mapcontrols from './mapcontrols.module';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    people,
    recipes,
    language,
    mapcontrols,
  },
});
