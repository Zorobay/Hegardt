import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router/router.js'

import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import "@fortawesome/fontawesome-free/js/fontawesome"
import "@fortawesome/fontawesome-free/js/regular"
import "@fortawesome/fontawesome-free/js/solid"
import "@fortawesome/fontawesome-free/css/fontawesome.css"
import "@fortawesome/fontawesome-free/css/solid.css"
import "@fortawesome/fontawesome-free/css/brands.css"

// Define global helpers (mixins)
const mixin = {
  methods: {
    formatFullName(firstName, middleNames, lastName) {
      if (!firstName && !middleNames && !lastName) {
        return '?';
      }

      const middleNamesStr = middleNames ? middleNames.join(' ') : '';
      const nameParts = [firstName, middleNamesStr, lastName];
      return nameParts.join(' ');
    }
  }
};

const app = createApp(App)
app.mixin(mixin);

app.use(createPinia())
app.use(router)

app.mount('#app')
