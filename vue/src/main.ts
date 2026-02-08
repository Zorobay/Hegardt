import './assets/css/main.css';

import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import router from './router/router.ts';

import PrimeVue from 'primevue/config';

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { library } from '@fortawesome/fontawesome-svg-core';

// Import FontAwesome icons
import {
  faAnglesUp,
  faArrowsToCircle,
  faBook,
  faMars,
  faSitemap,
  faUser,
  faVenus,
} from '@fortawesome/free-solid-svg-icons';

// Import PrimeVue
import 'primeicons/primeicons.css';
import { AccordionContent, AccordionHeader, AccordionPanel, Button } from 'primevue';

// Import Bootstrap CSS
import 'bootstrap/dist/css/bootstrap.min.css';

// Import custom theme CSS
import './assets/css/theme.scss';
import Theme from '@/theme/theme.ts';
import Menu from 'primevue/menu';
import Menubar from 'primevue/menubar';
import Accordion from 'primevue/accordion';
import Card from 'primevue/card';
import Checkbox from 'primevue/checkbox';
import InputNumber from 'primevue/inputnumber';

// Configure FontAwesome icons
library.add(faAnglesUp, faMars, faVenus, faArrowsToCircle, faSitemap, faUser, faBook);

const app = createApp(App);

app.component('FontAwesomeIcon', FontAwesomeIcon);

// Setup PrimeVue components
app.component('ButtonPrime', Button);
app.component('MenubarPrime', Menubar);
app.component('MenuPrime', Menu);
// app.component('DataTable', DataTable);
app.component('AccordionPrime', Accordion);
app.component('AccordionPanelPrime', AccordionPanel);
app.component('AccordionHeaderPrime', AccordionHeader);
app.component('AccordionContentPrime', AccordionContent);
app.component('CardPrime', Card);
app.component('CheckboxPrime', Checkbox);
app.component('InputNumberPrime', InputNumber);

app.use(createPinia());
app.use(router);
app.use(PrimeVue, {
  theme: {
    preset: Theme,
    options: {
      prefix: 'p',
      darkModeSelector: false,
    },
  },
});

app.mount('#app');
