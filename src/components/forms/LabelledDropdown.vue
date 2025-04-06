<template>
  <div class="input-group">
    <span class="input-group-text">{{ label }}</span>
    <select class="form-select">
      <option v-for="opt in options" :key="opt">{{ opt }}</option>
    </select>
  </div>
</template>

<script setup>
const props = defineProps(['label', 'options']);
</script>

<style scoped></style>
