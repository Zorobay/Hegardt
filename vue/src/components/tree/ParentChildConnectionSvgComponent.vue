<script setup lang="ts">
import { Connection } from '@/models/family-tree.model.ts';

const props = defineProps({
  connection: { type: Connection, required: true },
  horizontalSpacing: { type: Number, required: true },
});
</script>

<template>
  <line
    :x1="connection.startCoordinates.x"
    :y1="connection.startCoordinates.y"
    :x2="connection.startCoordinates.x + horizontalSpacing / 2"
    :y2="connection.startCoordinates.y"
    stroke-width="2"
    stroke="black"
  />
  <line
    :x1="connection.startCoordinates.x + horizontalSpacing / 2"
    :y1="connection.startCoordinates.y"
    :x2="connection.startCoordinates.x + horizontalSpacing / 2"
    :y2="connection.endCoordinates.y"
    stroke-width="2"
    stroke="black"
  />
  <line
    :x1="connection.startCoordinates.x + horizontalSpacing / 2"
    :y1="connection.endCoordinates.y"
    :x2="connection.endCoordinates.x"
    :y2="connection.endCoordinates.y"
    stroke-width="2"
    stroke="black"
  />
</template>

<style scoped></style>
