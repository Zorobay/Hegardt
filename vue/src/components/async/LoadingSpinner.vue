<script setup lang="ts">
defineProps({
  size: { type: String, default: '5rem' },
  dotSize: { type: String, default: '1rem' },
  innerDotSize: { type: String, default: '0.8rem' },
  colorOuter: { type: String, default: 'var(--heg-female-color)' },
  colorInner: { type: String, default: 'var(--heg-male-color)' },
  duration: { type: String, default: '1s' },
  delay: { type: String, default: '0.20s' },
});
</script>

<template>
  <div class="loader"></div>
</template>

<style scoped>
.loader {
  width: v-bind(size);
  aspect-ratio: 1;
  display: grid;
  grid-template-rows: v-bind(size);
  grid-template-columns: v-bind(size);
}

.loader::before,
.loader::after {
  content: '';
  grid-area: 1/1;
  background:
    no-repeat radial-gradient(farthest-side, v-bind(colorOuter) 92%, #0000) 50% 0,
    no-repeat radial-gradient(farthest-side, v-bind(colorOuter) 92%, #0000) 50% 100%,
    no-repeat radial-gradient(farthest-side, v-bind(colorOuter) 92%, #0000) 100% 50%,
    no-repeat radial-gradient(farthest-side, v-bind(colorOuter) 92%, #0000) 0 50%;
  background-size: v-bind(dotSize) v-bind(dotSize);
  animation: spin v-bind(duration) infinite ease;
}

.loader::after {
  margin: 4px;
  background:
    no-repeat radial-gradient(farthest-side, v-bind(colorInner) 92%, #0000) 50% 0,
    no-repeat radial-gradient(farthest-side, v-bind(colorInner) 92%, #0000) 50% 100%,
    no-repeat radial-gradient(farthest-side, v-bind(colorInner) 92%, #0000) 100% 50%,
    no-repeat radial-gradient(farthest-side, v-bind(colorInner) 92%, #0000) 0 50%;
  background-size: v-bind(innerDotSize) v-bind(innerDotSize);
  animation: spin 1s infinite ease;
  animation-delay: v-bind(delay);
}

@keyframes spin {
  100% {
    transform: rotate(0.5turn);
  }
}
</style>
