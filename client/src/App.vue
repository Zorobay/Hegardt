<template>
  <div>
    <Navbar></Navbar>
    <p>{{msg}}</p>
    <b-container id="app">
      <router-view :key="$route.fullPath"/>
    </b-container>
  </div>
</template>

<script>
  import Homepage from './components/pages/Homepage.vue';
  import Navbar from "./components/navbar/Navbar";

  export default {
    name: 'app',
    components: {
      Navbar,
      Homepage,
    },
    computed: {
      msg() {
        return this.$store.getters.globalMsg;
      }
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
