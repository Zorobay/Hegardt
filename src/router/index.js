import Vue from 'vue';
import VueRouter from 'vue-router';
import Homepage from '../components/pages/Homepage.vue';
import MissingPage from '../components/pages/MissingPage.vue';
import RegisterPage from '../components/pages/RegisterPage/RegisterPage.vue';
import MapPage from '../components/pages/MapPage/MapPage.vue';
import CreditPage from '../components/pages/CreditPage/CreditPage.vue';
import HegardtPage from '../components/pages/HegardtPage/HegardtPage.vue';
import SignupPage from '../components/pages/SignupPage/SignupPage.vue';
import PersonalFilePage from '../components/pages/PersonalFilePage/PersonalFilePage.vue';
import LoginPage from '../components/pages/LoginPage/LoginPage.vue';
import FamilyTreePage from '../components/pages/FamilyTreePage/FamilyTreePage.vue';

Vue.use(VueRouter);

const router = new VueRouter({
  routes: [
    {
      path: '/',
      name: 'Homepage',
      component: Homepage,
    },
    {
      path: '/hegardt',
      name: 'HegardtPage',
      component: HegardtPage,
    },
    {
      path: '/hegardt/register',
      name: 'Register',
      component: RegisterPage,
    },
    {
      path: '/hegardt/familytree',
      name: 'FamilyTreePage',
      component: FamilyTreePage,
    },
    {
      path: '/hegardt/person/id/:id',
      name: 'PersonalFile',
      component: PersonalFilePage,
    },
    {
      path: '/hegardt/map',
      name: 'Map',
      component: MapPage,
    },
    {
      path: '/credit',
      name: 'Credit',
      component: CreditPage,
    },
    {
      path: '/signup',
      name: 'SignupPage',
      component: SignupPage,
    },
    {
      path: '/login',
      name: 'LoginPage',
      component: LoginPage,
    },
    {
      path: '/404',
      alias: '*',
      name: 'MissingPage',
      component: MissingPage,
    }],
});

export default router;
