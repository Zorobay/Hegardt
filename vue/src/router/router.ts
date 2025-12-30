import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import PersonView from '@/views/PersonView.vue';
import PersonTableView from '@/views/PersonTableView.vue';
import NotFoundView from '@/views/NotFoundView.vue';
import PersonMapView from '@/views/PersonMapView.vue';
import FamilyTreeView from '@/views/FamilyTreeView.vue';

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
      props: true,
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
      path: '/tree/:personId?',
      name: 'tree',
      component: FamilyTreeView,
      props: true,
    },
  ],
});

export default router;
