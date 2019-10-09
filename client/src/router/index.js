import Vue from 'vue';
import VueRouter from 'vue-router';
import Homepage from '@/components/Homepage.vue';
import MissingPage from '@/components/MissingPage.vue';
import Register from '@/components/register/Register.vue';
import PersonalFile from '@/components/personal_file/PersonalFile';

Vue.use(VueRouter);

export default new VueRouter({
  routes: [
    {
      path: '/',
      name: 'Homepage',
      component: Homepage
    },
    {
      path: "/register",
      name: "Register",
      component: Register
    },
    {
      path: "/person/id/:id",
      name: "PersonalFile",
      component: PersonalFile
    },
    {
      path: "*",
      name: "MissingPage",
      component: MissingPage
    }]
});
