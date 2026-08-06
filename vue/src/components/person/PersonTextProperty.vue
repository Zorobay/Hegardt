<script setup lang="ts">
const { text, title } = defineProps<{
  text?: string;
  title: string;
  emptyCheck?: string;
}>();
</script>

<template>
  <div class="heg-person-text-property">
    <h5>{{ title }}</h5>
    <p v-if="text">{{ text }}</p>
    <span v-else-if="!emptyCheck" id="empty-text-emdash">—</span>
    <slot></slot>
  </div>
</template>

<style scoped>
.heg-person-text-property {
  margin-bottom: 2em;
}

#empty-text-emdash {
  opacity: 0.4;
  font-weight: bold;
}

h6 {
  margin-bottom: 0.2em;
}
</style>
