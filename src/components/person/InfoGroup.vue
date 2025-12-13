<template>
  <div class="heg-info-group">
    <h5>{{ title }}</h5>
    <hr />
    <div class="heg-info-group-content">
      <slot />
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps({ title: { type: String, required: false, default: '' } });
</script>

<style scoped>
.heg-info-group {
  margin-top: 2em;
}

hr {
  margin-top: 0.5em;
}
</style>
