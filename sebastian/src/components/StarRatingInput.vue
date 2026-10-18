<script setup lang="ts">
import { IconStar, IconStarFilled, IconStarHalfFilled } from '@tabler/icons-vue';

const rating = defineModel<number>({ default: 2.5 });
</script>

<template>
  <div class="flex gap-1">
    <div v-for="star in 5" :key="star" class="relative">
      <IconStarFilled v-if="rating >= star"></IconStarFilled>
      <IconStarHalfFilled v-else-if="Math.ceil(rating) === star" />
      <IconStar v-else />

      <button type="button" class="absolute inset-y-0 left-0 w-1/2" @click="rating = star - 0.5" />
      <button type="button" class="absolute inset-y-0 right-0 w-1/2" @click="rating = star" />
    </div>
  </div>
</template>

<style scoped></style>
