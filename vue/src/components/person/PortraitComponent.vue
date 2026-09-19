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
.heg-portrait {
  aspect-ratio: 0.75 / 1;
  flex-shrink: 0;
  img {
    display: block;
    width: 100%;
    height: 100%;
  }
}

.heg-portrait .placeholder {
  width: 100%;
  height: 100%;
  aspect-ratio: 0.75/1;
  border-radius: 50%;
  border: medium solid var(--jet-black);
  background-color: #bbb;
  cursor: default;
}
</style>
