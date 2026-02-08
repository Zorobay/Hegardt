<script setup lang="ts">
import personService from '@/services/PersonService.ts';
import type { VNodeRef } from 'vue';
import { computed, reactive, ref, watch } from 'vue';
import FamilyTreePersonCardComponent from '@/components/tree/FamilyTreePersonCardComponent.vue';
import ParentChildConnectionSvgComponent from '@/components/tree/ParentChildConnectionSvgComponent.vue';
import { Coordinates } from '@/models/coordinates.model.ts';
import { FamilyTree } from '@/models/family-tree.model.ts';

const props = defineProps({
  personId: { type: Number, required: false, default: null },
  maxDepth: { type: Number, required: false, default: 3 },
});
defineExpose({ center });

// ========== View constants ==========
const aspectRatio = 0.7;
const viewBoxWidth = 1000;
const viewBoxHeight = viewBoxWidth * aspectRatio;
const viewBoxX = ref(viewBoxWidth / 2);
const viewBoxY = ref(viewBoxHeight / 2);
const viewBox = computed(() => {
  const width = viewBoxWidth / zoomLevel.value;
  const height = viewBoxHeight / zoomLevel.value;
  return `${viewBoxX.value} ${viewBoxY.value} ${width} ${height}`;
});
let isPanning = ref(false);
let panStartPoint = new Coordinates();
let zoomLevel = ref(1);
const minZoom = 0.1;
const maxZoom = 3;
const zoomSpeed = 0.001;

const familyTree = reactive(new FamilyTree());
const svgRef = ref<VNodeRef | null>(null);

const rawPersonsData = personService.getAllPersons();

watch(
  () => props.personId,
  (newValue) => {
    if (newValue) {
      familyTree.rebuild(props.personId, rawPersonsData);
      center();
    }
  },
  { immediate: true },
);

watch(
  () => props.maxDepth,
  (newValue) => {
    if (newValue != null) {
      familyTree.setMaxRenderDepth(newValue);
      center();
    }
  },
);

function zoom(event: WheelEvent): void {
  event.preventDefault();

  // Get mouse position relative to SVG
  const svgElement = svgRef.value;
  if (!svgElement) return;

  const rect = svgElement.getBoundingClientRect();
  const mouseX = event.clientX - rect.left;
  const mouseY = event.clientY - rect.top;

  // Convert mouse position to SVG coordinates
  const svgX = viewBoxX.value + (mouseX / rect.width) * viewBoxWidth;
  const svgY = viewBoxY.value + (mouseY / rect.height) * viewBoxHeight;

  // Calculate zoom change
  const delta = -event.deltaY;
  const zoomFactor = 1 + delta * zoomSpeed;
  const newZoom = Math.min(Math.max(zoomLevel.value * zoomFactor, minZoom), maxZoom);

  // Calculate new viewBox dimensions
  const newViewBoxWidth = viewBoxWidth / newZoom;
  //const newViewBoxHeight = viewBoxHeight / newZoom;

  // Adjust viewBox position to zoom towards mouse cursor
  const scaleChange = newViewBoxWidth / (viewBoxWidth / zoomLevel.value);
  viewBoxX.value = svgX - (svgX - viewBoxX.value) * scaleChange;
  viewBoxY.value = svgY - (svgY - viewBoxY.value) * scaleChange;

  zoomLevel.value = newZoom;
}
function centerOnCoordinate(coordinates: Coordinates): void {
  const zoomedViewBoxWidth = viewBoxWidth / zoomLevel.value;
  const zoomedViewBoxHeight = viewBoxHeight / zoomLevel.value;
  viewBoxX.value = coordinates.x - zoomedViewBoxWidth / 2;
  viewBoxY.value = coordinates.y - zoomedViewBoxHeight / 2;
}

function center(): void {
  centerOnCoordinate(familyTree.getCenterCoordinates());
}

function setStartPointForPan(event: MouseEvent): void {
  isPanning.value = true;
  panStartPoint = new Coordinates(event.clientX, event.clientY);
}

function pan(event: MouseEvent): void {
  if (!isPanning.value || !svgRef.value) return;

  const dx = (event.clientX - panStartPoint.x) / zoomLevel.value;
  const dy = (event.clientY - panStartPoint.y) / zoomLevel.value;

  // Get the SVG elements bounding box
  const svgRect = svgRef.value.getBoundingClientRect();

  // Scale the movement based on viewBox size relative to svg bounding box
  const scaleX = viewBoxWidth / svgRect.width;
  const scaleY = viewBoxHeight / svgRect.height;

  viewBoxX.value -= dx * scaleX;
  viewBoxY.value -= dy * scaleY;
  panStartPoint = new Coordinates(event.clientX, event.clientY);
}

function endPanning(): void {
  isPanning.value = false;
}
</script>

<template>
  <div class="card">
    <div class="card-body">
      <svg
        ref="svgRef"
        :viewBox="viewBox"
        class="heg-family-tree"
        :style="{ cursor: isPanning ? 'grabbing' : 'default' }"
        @mousedown.prevent="setStartPointForPan"
        @mousemove="pan"
        @mouseup="endPanning"
        @mouseleave="endPanning"
        @wheel.prevent="zoom"
      >
        <g v-for="node in familyTree.getNodesToRender()" :key="node.id">
          <FamilyTreePersonCardComponent
            :node="node"
            :card-width="familyTree.config.personCardWidth"
            :card-height="familyTree.config.personCardHeight"
            :focus="node.id == personId"
          />
        </g>
        <g v-for="connection in familyTree.straightConnections" :key="connection.id">
          <line
            :x1="connection.startCoordinates.x"
            :y1="connection.startCoordinates.y"
            :x2="connection.endCoordinates.x"
            :y2="connection.endCoordinates.y"
            stroke-width="2"
            stroke="black"
          />
        </g>
        <g v-for="connection in familyTree.parentChildConnections" :key="connection.id">
          <ParentChildConnectionSvgComponent
            :horizontal-spacing="familyTree.config.horizontalSpacing"
            :connection="connection"
          />
        </g>
      </svg>
    </div>
  </div>
</template>

<style scoped>
svg {
  user-select: none;
}

.heg-family-tree {
  width: 100%;
  aspect-ratio: 1 / v-bind(aspectRatio);
}
</style>
