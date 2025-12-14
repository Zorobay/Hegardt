<template>
  <div class="heg-person-text-property">
    <h5>{{ title }}</h5>
    <p v-if="text">{{ text }}</p>
    <slot></slot>
  </div>
</template>

<script setup lang="ts">
defineProps(['text', 'title']);
</script>

<style scoped>
.heg-person-text-property {
  margin-bottom: 2em;
}
h6 {
  margin-bottom: 0.2em;
}
</style>
