import Vue from 'vue';

// Import Bootstrap and Bootstrap Vue
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

// Import FontAwesome icons
import { library } from '@fortawesome/fontawesome-svg-core';
import { faMapMarkedAlt, faCalendarAlt } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

import router from './router';
import App from './App.vue';


// Import and use JQuery
window.$ = require('jquery');
window.JQuery = require('jquery');

Vue.use(BootstrapVue);
Vue.config.productionTip = false;

// Add required icons to the library here, one by one
library.add(faMapMarkedAlt, faCalendarAlt);
Vue.component('font-awesome-icon', FontAwesomeIcon);


new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
