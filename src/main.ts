import './assets/css/main.css';

import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import router from './router/router.ts';

import 'bootstrap';

/* import the fontawesome core */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { library } from '@fortawesome/fontawesome-svg-core';

/* import specific icons */
import { faAnglesUp } from '@fortawesome/free-solid-svg-icons';

/* add icons to the library */
library.add(faAnglesUp);

const app = createApp(App);

app.component('FontAwesomeIcon', FontAwesomeIcon);
app.use(createPinia());
app.use(router);

app.mount('#app');
