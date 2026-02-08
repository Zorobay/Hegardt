<script setup lang="ts">
defineProps({ title: { type: String, required: false, default: '' } });
</script>

<template>
  <CardPrime class="heg-info-group">
    <template #title>
      {{ title }}
      <hr />
    </template>
    <template #content>
      <div class="heg-info-group-content">
        <slot />
      </div>
    </template>
  </CardPrime>
</template>

<style scoped>
.heg-info-group {
  margin-bottom: 1.5rem;
}
hr {
  margin-top: 0.5em;
}

.heg-info-group-title {
  font-weight: bold;
}
</style>
