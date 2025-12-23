<script setup lang="ts">
defineProps({ title: { type: String, required: false, default: '' } });
</script>

<template>
  <div class="heg-info-group card card-body">
    <h4 class="heg-info-group-title">{{ title }}</h4>
    <hr />
    <div class="heg-info-group-content">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.heg-info-group {
  margin-top: 2em;
}

hr {
  margin-top: 0.5em;
}

.heg-info-group-title {
  font-weight: bold;
}
</style>
