import './assets/css/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router/router.ts'

import "bootstrap"
import "@fortawesome/fontawesome-free/js/fontawesome"
import "@fortawesome/fontawesome-free/js/regular"
import "@fortawesome/fontawesome-free/js/solid"
import "@fortawesome/fontawesome-free/css/fontawesome.css"
import "@fortawesome/fontawesome-free/css/solid.css"
import "@fortawesome/fontawesome-free/css/brands.css"

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
