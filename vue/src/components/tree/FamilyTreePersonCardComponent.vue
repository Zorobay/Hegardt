<script setup lang="ts">
import { FamilyTreeNode } from '@/types/family-tree.types.ts';
import PortraitComponent from '@/components/person/PortraitComponent.vue';
import SexEnum from '@/enums/PersonSexEnum.ts';
import PersonCardIconLinks from '@/components/person/PersonCardIconLinks.vue';

const props = defineProps({
  node: { type: FamilyTreeNode, required: true },
  cardWidth: { type: Number, required: true },
  cardHeight: { type: Number, required: true },
  focus: { type: Boolean, required: false, default: false },
});
const rectWidth = props.cardWidth;
const rectHeight = props.cardHeight;
const portraitWidth = rectWidth * 0.3;
const innerHeightWithMargin = rectHeight - 10;
const colorVarMap = {
  [SexEnum.MAN]: 'var(--heg-male-color)',
  [SexEnum.WOMAN]: 'var(--heg-female-color)',
  [SexEnum.UNKNOWN]: 'var(--heg-unknown-color)',
};
const strokeColor = colorVarMap[props.node.sex];
</script>

<template>
  <rect
    class="background-rect-male"
    ry="5"
    rx="5"
    :width="rectWidth"
    :height="rectHeight"
    :x="props.node.x"
    :y="props.node.y"
    :class="{ 'pulse-focus': focus }"
  ></rect>

  <foreignObject :x="props.node.x + 5" :y="props.node.y + 5" :width="portraitWidth" :height="innerHeightWithMargin">
    <div :style="{ height: innerHeightWithMargin + 'px' }">
      <PortraitComponent />
    </div>
  </foreignObject>
  <foreignObject
    :x="props.node.x + 50"
    :y="props.node.y + 5"
    :width="rectWidth - portraitWidth"
    :height="innerHeightWithMargin"
  >
    <div class="person-info-div">
      <div class="scrolling-text-container">
        <h6 class="small-text mb-1 scrolling-text">
          {{ props.node.fullName }}
        </h6>
      </div>
      <p class="small-text text-secondary mb-1">{{ props.node.lifespan }}</p>
      <div class="icon-links-row" style="flex-grow: 1">
        <PersonCardIconLinks :id="props.node.id" />
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
