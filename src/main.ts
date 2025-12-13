import './assets/css/main.css';

import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import router from './router/router.ts';

import 'bootstrap';
import '@fortawesome/fontawesome-free/js/fontawesome';
import '@fortawesome/fontawesome-free/js/regular';
import '@fortawesome/fontawesome-free/js/solid';
import '@fortawesome/fontawesome-free/css/fontawesome.css';
import '@fortawesome/fontawesome-free/css/solid.css';
import '@fortawesome/fontawesome-free/css/brands.css';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core';

/* import specific icons */
import { faAnglesUp } from '@fortawesome/free-solid-svg-icons';

/* add icons to the library */
library.add(faAnglesUp);

const app = createApp(App);

app.component('font-awesome-icon', FontAwesomeIcon);
app.use(createPinia());
app.use(router);

app.mount('#app');
