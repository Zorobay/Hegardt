import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PersonView from "@/views/PersonView.vue";
import PersonTableView from "@/views/PersonTableView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/person/:id',
      name: 'person',
      component: PersonView
    },
    {
      path: '/table',
      name: 'table',
      component: PersonTableView
    }
  ],
})

export default router
