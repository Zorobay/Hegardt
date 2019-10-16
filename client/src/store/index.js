import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);

import people from "./people.module";

export default new Vuex.Store({

  modules: {
    people
  },
  });
