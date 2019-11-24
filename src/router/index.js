import Vue from 'vue';
import VueRouter from 'vue-router';
import Homepage from '@/components/pages/Homepage.vue';
import MissingPage from '@/components/pages/MissingPage.vue';
import RegisterPage from '@/components/pages/RegisterPage/RegisterPage.vue';
import Map from "../components/pages/MapPage/LeafletMap";
import MapPage from "../components/pages/MapPage/MapPage";
import Debug from "../components/Debug";
import CreditPage from "../components/pages/CreditPage/CreditPage";
import HegardtPage from "../components/pages/HegardtPage/HegardtPage";
import SignupPage from "../components/pages/SignupPage/SignupPage";
import PersonalFilePage from "../components/pages/PersonalFilePage/PersonalFilePage";
import LoginPage from "../components/pages/LoginPage/LoginPage";
import FamilyTreePage from "../components/pages/FamilyTreePage/FamilyTreePage";

Vue.use(VueRouter);

export default new VueRouter({
  routes: [
    {
      path: '/',
      name: 'Homepage',
      component: Homepage
    },
    {
      path: "/hegardt",
      name: "HegardtPage",
      component: HegardtPage
    },
    {
      path: "/hegardt/register",
      name: "Register",
      component: RegisterPage
    },
    {
      path: "/hegardt/familytree",
      name: "FamilyTreePage",
      component: FamilyTreePage
    },
    {
      path: "/hegardt/person/id/:id",
      name: "PersonalFile",
      component: PersonalFilePage
    },
    {
      path: "/debug",
      name: "Debug",
      component: Debug
    },
    {
      path: "/hegardt/map",
      name: "Map",
      component: MapPage
    },
    {
      path: "/credit",
      name: "Credit",
      component: CreditPage
    },
    {
      path: "/signup",
      name: "SignupPage",
      component: SignupPage
    },
    {
      path: "/login",
      name: "LoginPage",
      component: LoginPage
    },
    {
      path: "*",
      name: "MissingPage",
      component: MissingPage
    }]
});
