<template>
  <div>
    <h5>{{title}}</h5>
    <hr>
  </div>
  <slot/>
</template>

<script setup lang="ts">
  defineProps(['title'])
</script>

<style scoped>
div {
  margin-top: 2em;
}
hr {
  margin-top: 0.5em;
}
</style>
