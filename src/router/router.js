import {createRouter, createWebHashHistory, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PersonView from "@/views/PersonView.vue";
import PersonTableView from "@/views/PersonTableView.vue";
import NotFoundView from "@/views/NotFoundView.vue";

const router = createRouter({
  history: createWebHistory(),
  // history: createWebHashHistory(),
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
    },
    {
      path: '/:pathMatch(.*)',
      name: '404 catch all',
      component: NotFoundView
    }
  ],
})

export default router
