<script setup lang="ts">
import {RouterView} from 'vue-router'
import NavbarComponentComponent from "@/components/NavbarComponent.vue";
</script>

<template>
  <header>
    <NavbarComponentComponent></NavbarComponentComponent>
  </header>

  <div class="container">
    <RouterView :key="$route.path"/>
  </div>
</template>

<style scoped>

</style>
