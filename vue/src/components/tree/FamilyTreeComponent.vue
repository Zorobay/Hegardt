<script setup lang="ts">
import personService from '@/services/PersonService.ts';
import type { VNodeRef } from 'vue';
import { computed, ref, watch } from 'vue';
import type { Person } from '@/types/person.type.ts';
import { Coordinate, FamilyTreeNode } from '@/types/family-tree.types.ts';
import FamilyTreePersonCardComponent from '@/components/tree/FamilyTreePersonCardComponent.vue';
import SexEnum from '@/enums/PersonSexEnum.ts';

const props = defineProps({
  personId: { type: Number, required: false, default: null },
});
const nodesToRender = ref<FamilyTreeNode[]>([]);
const svgRef = ref<VNodeRef | null>(null);
const originCoordinates = new Coordinate();
const personCardWidth = 200;
const personCardHeight = 68;
const horizontalSpacing = 20;
const verticalSpacing = 60;
const aspectRatio = 0.7;
const viewBoxWidth = 1000;
const viewBoxHeight = viewBoxWidth * aspectRatio;
const viewBoxX = ref(personCardWidth / 2 - viewBoxWidth / 2);
const viewBoxY = ref(personCardHeight / 2 - viewBoxHeight / 2);
const viewBox = computed(() => {
  return `${viewBoxX.value} ${viewBoxY.value} ${viewBoxWidth} ${viewBoxHeight}`;
});
let isPanning = ref(false);
let panStartPoint = new Coordinate();

const rawPersonsData = personService.getAllPersons();

console.log(`personId: ${props.personId}`);
watch(
  () => props.personId,
  (newValue) => {
    if (newValue) {
      const rootPerson = rawPersonsData[props.personId];
      const nodes = buildFamilyTreeNode(rootPerson, originCoordinates);
      nodesToRender.value = nodes;
    }
  },
  { immediate: true },
);

function setStartPointForPan(event: MouseEvent): void {
  isPanning.value = true;
  panStartPoint = new Coordinate(event.clientX, event.clientY);
}

function pan(event: MouseEvent): void {
  if (!isPanning.value || !svgRef.value) return;

  const dx = event.clientX - panStartPoint.x;
  const dy = event.clientY - panStartPoint.y;

  // Get the SVG elements bounding box
  const svgRect = svgRef.value.getBoundingClientRect();

  // Scale the movement based on viewBox size relative to svg bounding box
  const scaleX = viewBoxWidth / svgRect.width;
  const scaleY = viewBoxHeight / svgRect.height;

  viewBoxX.value -= dx * scaleX;
  viewBoxY.value -= dy * scaleY;
  panStartPoint = new Coordinate(event.clientX, event.clientY);
}

function endPanning(event: MouseEvent): void {
  isPanning.value = false;
}

function buildFamilyTreeNode(person: Person, origin: Coordinate): FamilyTreeNode[] {
  const meAndParentNodes = buildParentNodes(person.id, origin);
  const childNodes = buildChildNodes(person.id, origin);
  return [...meAndParentNodes, ...childNodes];
}

function buildParentNodes(personId: number, origin: Coordinate): FamilyTreeNode[] {
  const person = rawPersonsData[personId];
  const node = new FamilyTreeNode(person);
  node.setCoordinates(origin.x, origin.y);
  const fatherOrigin = new Coordinate(
    origin.x - personCardWidth / 2 - horizontalSpacing,
    origin.y - personCardHeight - verticalSpacing,
  );
  const motherOrigin = new Coordinate(
    origin.x + personCardWidth / 2 + horizontalSpacing,
    origin.y - personCardHeight - verticalSpacing,
  );
  const fatherNodes = person.father ? buildParentNodes(person.father, fatherOrigin) : [];
  const motherNodes = person.mother ? buildParentNodes(person.mother, motherOrigin) : [];
  const siblingNodes = buildSiblingNodes(person, origin);
  return [node, ...fatherNodes, ...motherNodes];
}

function buildSiblingNodes(person: Person, origin: Coordinate): FamilyTreeNode[] {
  const siblings = personService.getSiblingsOfPersonById(person.id);
  let index = 1;
  return siblings.map((sibling) => {
    const node = new FamilyTreeNode(sibling);
    const horizontalShift = (personCardWidth + horizontalSpacing) * index;
    node.x = person.sex === SexEnum.WOMAN ? origin.x + horizontalShift : origin.x - horizontalShift;
    node.y = origin.y;
    index += 1;
    return node;
  });
}

function buildChildNodes(personId: number, origin: Coordinate): FamilyTreeNode[] {
  const person = rawPersonsData[personId];
  const childIds = person.children;
  const numChildren = childIds.length;
  let index = 0;
  return childIds.flatMap((childId) => {
    const child = rawPersonsData[childId];
    const node = new FamilyTreeNode(child);
    const horizontalShift = (personCardWidth + horizontalSpacing) * index;
    node.x = origin.x - horizontalShift;
    node.y = origin.y + personCardHeight + verticalSpacing;
    index += 1;
    return [node];
  });
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
      >
        <g v-for="node in nodesToRender" :key="node.id">
          <FamilyTreePersonCardComponent
            :node="node"
            :card-width="personCardWidth"
            :card-height="personCardHeight"
            :focus="node.id == personId"
          />
          <p>{{ node.id == personId }}</p>
        </g>
      </svg>
    </div>
  </div>
</template>

<style scoped>
svg {
  user-select: none;
  -webkit-user-select: none;
}

.heg-family-tree {
  width: 100%;
  aspect-ratio: 1 / v-bind(aspectRatio);
}
</style>
