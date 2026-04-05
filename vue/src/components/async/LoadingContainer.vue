<script setup lang="ts">
import LoadingSpinner from '@/components/async/LoadingSpinner.vue';

const {
  isLoading = false,
  message = '',
  overlay = true,
} = defineProps<{
  isLoading: boolean;
  message?: string;
  overlay?: boolean;
}>();
</script>

<template>
  <div class="container">
    <div v-if="isLoading" class="spinner">
      <LoadingSpinner :size="'5rem'" />
      <p>{{ message }}</p>
    </div>
    <div v-if="overlay" :class="{ 'loading-slot': isLoading }">
      <slot></slot>
    </div>
  </div>
</template>

<style scoped>
.container {
  position: relative;
}

.spinner {
  position: absolute;
  display: flex;
  flex-direction: column;
  align-items: center;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 9999;
}

.loading-slot {
  opacity: 0.2;
}
</style>
