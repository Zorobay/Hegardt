import Vue from 'vue';
// Import Bootstrap and Bootstrap Vue
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
// Import FontAwesome icons
import {library} from '@fortawesome/fontawesome-svg-core';
import {faCalendarAlt, faMapMarkedAlt} from '@fortawesome/free-solid-svg-icons';
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome';

import router from './router';
import App from './App.vue';

Vue.use(BootstrapVue);
Vue.config.productionTip = false;

// Add required icons to the library here, one by one
library.add(faMapMarkedAlt, faCalendarAlt);
Vue.component('font-awesome-icon', FontAwesomeIcon);

// Import and use leaflet for maps
import { Icon } from "leaflet";
//import "leaflet.icon.glyph";
delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png")
});

// Define vue mixins
Vue.mixin({
  methods: {
    formatDate: function (date) {
      var moment = require("moment");
      if (date == null) {
        return "?";
      } else {
        let d = moment(date.date);
        return d.format("YYYY-MM-DD");
      }
    },
    formatOccupations: function (occupations) {
      if (occupations == null) {
        return "?";
      } else {
        return occupations.join(", ");
      }
    },
    formatLocation: function (location) {
      if (location) {
        return [location.country, location.region, location.city].join(", ");
      } else {
        return "?";
      }
    }
  }
});

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
