import '../scss/custom.scss';
import '../public/global.css';
import formatDate from 'date-fns/format';
import {enUS, sv} from 'date-fns/locale';
import _get from 'lodash/get';
import language from '@/common/enums/language';

import Vue from 'vue';
import Vuex from 'vuex';
import store from './store';

// Import Bootstrap and Bootstrap Vue
import {BootstrapVue, IconsPlugin} from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

import router from './router';
import App from './App.vue';

// Fontawesome icons
import {library} from '@fortawesome/fontawesome-svg-core';
import {faVenus, faMars, faStickyNote} from '@fortawesome/free-solid-svg-icons';
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome';

library.add(faVenus, faMars, faStickyNote);
Vue.component('font-awesome-icon', FontAwesomeIcon);

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(Vuex);
Vue.config.productionTip = false;

// Import and use leaflet for maps
import {Icon} from 'leaflet';


// import "leaflet.icon.glyph";
delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

// Define vue mixins
Vue.mixin({
  methods: {
    Text(path) {
      const value = _get(this.$store.getters.languageDict, path);
      return value ? value : path;
    },
    getLanguage() {
      return this.$store.getters.language;
    },
    getLocale() {
      const lang = this.getLanguage();
      switch (lang) {
        case language.ENGLISH:
          return enUS;
        case language.SWEDISH:
          return sv;
        default:
          throw Error(`Could not find locale for language ${lang} as it is not supported!`);
      }
    },
    formatRange(range) {
      let out = range[0];
      if (range[1]) {
        out += ` - ${range[1]}`;
      }
      return out;
    },
    formatDate(dateObject) {
      if (!dateObject || !dateObject.date) {
        return '';
      }

      let formatString = '';

      if (dateObject.year) {
        formatString += 'yyyy';
      }

      if (dateObject.month) {
        formatString += '-MM';
        if (dateObject.day) {
          formatString += '-dd';
        }
      }

      return formatDate(new Date(dateObject.date), formatString);
    },
    prettyDate(dateObject) {
      if (!dateObject || !dateObject.date) {
        return '';
      }
      const locale = this.getLocale();

      if (this.isCompleteDate(dateObject) && dateObject.date) {
        return formatDate(new Date(dateObject.date), 'cccc, d MMMM yyyy', {locale: locale});
      } else {
        const date = new Date();
        let format = '';

        if (dateObject.day) {
          date.setDate(dateObject.date);
          format += 'd';
        }

        if (dateObject.month) {
          date.setMonth(dateObject.month);
          format += ' MMMM';
        }

        if (dateObject.year) {
          date.setFullYear(dateObject.year);
          format += ' yyyy';
        }

        return formatDate(date, format, {locale: locale}).trim();
      }
    },
    isCompleteDate: function(dateObject) {
      return dateObject.year && dateObject.month && dateObject.day;
    },
    formatOccupations: function(occupations) {
      if (occupations == null) {
        return '?';
      } else {
        return occupations.join(', ');
      }
    },
    formatLocation: function(location) {
      if (location) {
        const locs = [location.city, location.region, location.country];
        return locs.filter(l => !!l).join(', ');
      }
    },
    elvis: function(obj, path) {
      return _get(obj, path);
    },
  },
});

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
