<template>
  <div>
    <Navbar></Navbar>
    <b-container id="app">
      <router-view/>
    </b-container>
  </div>
</template>

<script>
  import Homepage from './components/Homepage.vue';
  import Navbar from "./components/Navbar";

  export default {
    name: 'app',
    components: {
      Navbar,
      Homepage,
    },
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
