<script setup lang="ts">
import PortraitComponent from '@/components/person/PortraitComponent.vue';
import SexEnum from '@/enums/PersonSexEnum.ts';
import PersonCardIconLinks from '@/components/person/PersonCardIconLinks.vue';
import type { FamilyTreeNode } from '@/models/family-tree.model.ts';

const {
  node,
  cardWidth,
  cardHeight,
  focus = false,
} = defineProps<{ node: FamilyTreeNode; cardWidth: number; cardHeight: number; focus: boolean }>();
const rectWidth = cardWidth;
const rectHeight = cardHeight;
const portraitWidth = rectWidth * 0.2;
const innerHeightWithMargin = rectHeight - 10;
const colorVarMap = {
  [SexEnum.MAN]: 'var(--heg-male-color)',
  [SexEnum.WOMAN]: 'var(--heg-female-color)',
  [SexEnum.UNKNOWN]: 'var(--heg-unknown-color)',
};
const strokeColor = colorVarMap[node.sex];
</script>

<template>
  <rect
    class="background-rect-male"
    ry="5"
    rx="5"
    :width="rectWidth"
    :height="rectHeight"
    :x="node.x"
    :y="node.y"
    :class="{ 'pulse-focus': focus }"
  ></rect>

  <foreignObject :x="node.x + 5" :y="node.y + 5" :width="portraitWidth" :height="innerHeightWithMargin">
    <div :style="{ height: innerHeightWithMargin + 'px' }">
      <PortraitComponent :id="node.id" />
    </div>
  </foreignObject>
  <foreignObject :x="node.x + 50" :y="node.y + 5" :width="rectWidth - portraitWidth" :height="innerHeightWithMargin">
    <div class="person-info-div">
      <div class="scrolling-text-container">
        <h6 class="small-text mb-1 scrolling-text">
          {{ node.fullName }}
        </h6>
      </div>
      <p class="small-text text-secondary mb-1">{{ node.lifespan }}</p>
      <div class="icon-links-row" style="flex-grow: 1">
        <PersonCardIconLinks :id="node.id" />
      </div>
    </div>
  </foreignObject>
</template>

<style scoped>
.background-rect-male {
  stroke-width: 3;
  stroke: v-bind(strokeColor);
}

.heg-portrait {
  height: 100%;
  width: 100%;
}

.person-info-div {
  display: flex;
  flex-direction: column;
  height: 100%;
  justify-content: space-between;
}

.icon-links-row {
  bottom: 0;
  max-height: 1rem;
}

.small-text {
  font-size: 8pt;
  color: white;
}
</style>
