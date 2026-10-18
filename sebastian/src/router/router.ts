import { createRouter, createWebHistory } from 'vue-router';
import TrackerHomeView from '@/views/TrackerHomeView.vue';
import HomeView from '@/views/HomeView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home',
      name: 'Home',
      component: HomeView,
    },
    {
      path: '/tracker',
      name: 'TrackerHome',
      component: TrackerHomeView,
    },
  ],
});

export default router;
