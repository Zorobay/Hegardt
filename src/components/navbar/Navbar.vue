<template>
  <b-navbar toggleable="lg" type="dark" variant="primary">
    <b-navbar-brand href="#/">Sebastian.hegardt.se</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>

      <!--Left aligned nav items-->
      <b-navbar-nav>
        <b-nav-item href="#/">{{ Lang('menu.home') }}</b-nav-item>

        <b-nav-item-dropdown text="Hegardt.se" right>
          <b-dropdown-item href="#/hegardt">{{ Lang('menu.home') }}</b-dropdown-item>
          <b-dropdown-item href="#/hegardt/register">{{ Lang('menu.register') }}</b-dropdown-item>
          <b-dropdown-item href="#/hegardt/map">{{ Lang('menu.map') }}</b-dropdown-item>
          <b-dropdown-item :to="{name: 'FamilyTreePage'}">Family Tree</b-dropdown-item>
        </b-nav-item-dropdown>

        <b-nav-item-dropdown :text="Lang('menu.other_projects')">
          <b-dropdown-item href="#/recipes">{{ Lang('menu.recipes') }}</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-dropdown variant="primary" text="Language" class="m-md-auto">
          <b-dropdown-item value="se" @click="onLanguageChosen('se')">
            Swedish<img src="icons/sweden.png" height="22"/>
          </b-dropdown-item>
          <b-dropdown-item active value="en" @click="onLanguageChosen('en')">
            English<img src="icons/usa.jpg" height="14"/>
          </b-dropdown-item>
        </b-dropdown>
        <search-form></search-form>
        <b-nav-item :to="{name: 'LoginPage'}">Log in</b-nav-item>
        <b-nav-item :to="{name: 'SignupPage'}">Sign up</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
  import SearchForm from './SearchForm';
  import {CHANGE_LANGUAGE} from '@/store/actions.type';

  export default {
    name: 'Navbar',
    components: {SearchForm},
    data() {
      return {
      };
    },
    computed: {
      lang() {
        return this.$store.getters.language;
      },
    },
    methods: {
      onLanguageChosen(lang) {
        this.$store.dispatch(CHANGE_LANGUAGE, lang);
      },
      login() {
        this.$router.push({name: 'LoginPage'});
      },
      signup() {
        this.$router.push({name: 'SignupPage'});
      },
    },
  };
</script>

<style scoped>

  .swedish-flag::before{
    content: '\01F1FA\01F1F8';
  }
</style>
