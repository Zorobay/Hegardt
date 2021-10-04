<template>
  <div>
    <Navbar></Navbar>
    <b-container class="app">
      <router-view :key="$route.fullPath"/>
    </b-container>
    <MyFooter></MyFooter>
  </div>
</template>

<script>
  import {CHANGE_LANGUAGE} from './store/actions.type';
  import Navbar from '@/components/navbar/Navbar';
  import MyFooter from '@/components/footer/MyFooter';

  export default {
    name: 'app',
    components: {
      Navbar,
      MyFooter,
    },
    data() {
      return {
        defaultLang: 'en',
      };
    },
    created() {
      // Load default language English
      this.$store.dispatch(CHANGE_LANGUAGE, this.defaultLang)
        .then(_ => console.log(`Loaded language file for default language code [${this.defaultLang}]`));
    },
  };
</script>

<style>
  .app {
    min-height: 100vh;
  }
</style>
