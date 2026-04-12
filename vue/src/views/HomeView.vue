<script setup lang="ts">
const shieldUrl = '/assets/images/shield_high_res_cleaned.png';
</script>

<template>
  <p>Welcome to my website!</p>
  <p>
    This is a website I, <router-link :to="{ name: 'person', params: { id: 619 } }">Sebastian Hegardt</router-link>, am
    developing for my family. The research is mostly based on the work conducted by
    <router-link :to="{ name: 'person', params: { id: 592 } }">Peter Hegardt</router-link>.
  </p>

  <div id="family-shield">
    <img :src="shieldUrl" alt="Family shield" />
  </div>
</template>

<style scoped>
#family-shield {
  display: flex;
  align-items: center;
  flex-direction: column;

  img {
    width: 50%;
  }
}
</style>
