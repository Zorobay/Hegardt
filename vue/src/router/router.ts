import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PersonView from '@/views/PersonView.vue'
import PersonTableView from '@/views/PersonTableView.vue'
import NotFoundView from '@/views/NotFoundView.vue'
import PersonMapView from '@/views/PersonMapView.vue'
import PersonTreeView from '@/views/PersonTreeView.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/person/:id',
      name: 'person',
      component: PersonView,
      props: true
    },
    {
      path: '/table',
      name: 'table',
      component: PersonTableView,
    },
    {
      path: '/:pathMatch(.*)',
      name: '404 catch all',
      component: NotFoundView,
    },
    {
      path: '/map',
      name: 'map',
      component: PersonMapView,
    },
    {
      path: '/tree/:id?',
      name: 'tree',
      component: PersonTreeView,
      props: true
    },
  ],
})

export default router
