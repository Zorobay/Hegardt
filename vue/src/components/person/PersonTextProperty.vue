<script setup lang="ts">
import { useHasSlotContent } from '@/composables/useHasSlotContent.ts';

const { text, title } = defineProps<{
  text?: string;
  title: string;
}>();

function isEmpty(): boolean {
  const hasSlotContent = useHasSlotContent();
  return !!text || !hasSlotContent.value;
}
</script>

<template>
  <div class="heg-person-text-property">
    <h5>{{ title }}</h5>
    <div id="text-div">
      <p v-if="text">{{ text }}</p>
      <span v-else-if="isEmpty()" id="empty-text-emdash">—</span>
      <slot></slot>
    </div>
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

#text-div {
  border: var(--glaucous) solid 0.15rem;
  border-radius: 1rem;
  padding: 0.5rem;
  box-shadow: inset var(--lavender-gray) 0.15rem 0.15rem;

  p {
    margin-bottom: 0 !important;
  }
}

h6 {
  margin-bottom: 0.2em;
}
</style>
