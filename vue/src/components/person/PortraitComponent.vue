<script setup lang="ts">
import { ref } from 'vue';
import type { EntityId } from '@/types/person.type.ts';

const { id } = defineProps<{ id: EntityId }>();

const portraitUrl = `/static_media/portraits/id${id}.png`;
const hasPortrait = ref(false);
</script>

<template>
  <div class="heg-portrait">
    <span v-if="!hasPortrait" class="placeholder"></span>
    <img
      v-show="hasPortrait"
      :src="portraitUrl"
      :alt="`Portrait ${id}`"
      @load="hasPortrait = true"
      @error="hasPortrait = false"
    />
  </div>
</template>

<style scoped>
img {
  width: 100%;
}

.placeholder {
  width: 100%;
  aspect-ratio: 0.75/1;
  border-radius: 50%;
  border: medium solid var(--jet-black);
  background-color: #bbb;
  cursor: default;
}
</style>
