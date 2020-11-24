<template>
  <div>
    <Navbar></Navbar>
    <b-container class="app">
      <router-view :key="$route.fullPath"/>
    </b-container>
  </div>
</template>

<script>
  import {CHANGE_LANGUAGE} from './store/actions.type';
  import Navbar from '@/components/navbar/Navbar';

  export default {
    name: 'app',
    components: {
      Navbar,
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

</style>
