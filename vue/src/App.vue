<script setup lang="ts">
import { RouterView } from 'vue-router';
import NavbarComponentComponent from '@/components/NavbarComponent.vue';
</script>

<template>
  <header>
    <NavbarComponentComponent></NavbarComponentComponent>
  </header>

  <div class="container">
    <!--
      Custom :key so most routes still remount on every navigation
      (the default: keyed by route.fullPath). Routes that need to KEEP
      their component instance across param changes — e.g. family-book,
      which changes its :page param on every Next/Prev click and shouldn't
      re-fetch/re-render the PDF each time — opt OUT of remounting by
      setting meta: { noRemount: true }.
    -->
    <RouterView v-slot="{ Component, route }">
      <component :is="Component" :key="route.meta.noRemount ? undefined : route.fullPath"></component>
    </RouterView>
  </div>
</template>

<style scoped></style>
