<script setup>
import {RouterView} from 'vue-router'
import Navbar from "@/components/Navbar.vue";
</script>

<template>
  <header>
    <Navbar></Navbar>
  </header>

  <div class="container">
    <RouterView :key="$route.path"/>
  </div>
</template>

<style scoped>

</style>
