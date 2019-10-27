<template>
  <div>
    <Navbar></Navbar>
    <b-container id="app">
      <router-view :key="$route.fullPath"/>
    </b-container>
  </div>
</template>

<script>
  import Homepage from './components/pages/Homepage.vue';
  import Navbar from "./components/navbar/Navbar";
  import {CHANGE_LANGUAGE} from "./store/actions.type";

  export default {
    name: 'app',
    components: {
      Navbar,
      Homepage,
    },
    data() {
      return {
        defaultLang: 'en'
      }
    },
    created() {
      // Load default language English
      this.$store.dispatch(CHANGE_LANGUAGE, this.defaultLang)
        .then(res => console.log(`Loaded language file for default language code [${this.defaultLang}]`));
    }
  };
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
