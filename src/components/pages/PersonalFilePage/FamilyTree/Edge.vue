<template>
<g>
  <arrowhead width="5" length="5"/>
  <polyline :points="points" class="edge" fill="none" marker-end="url(#arrowhead)"/>
</g>
</template>

<script>
  import Arrowhead from '@/components/pages/PersonalFilePage/FamilyTree/Arrowhead';

  export default {
    name: 'Edge',
    components: {Arrowhead},
    props: ['startNodeId', 'endNodeId', 'startAnchor', 'endAnchor'],
    data() {
      return {
        startX: 0,
        startY: 0,
        endX: 0,
        endY: 0,
      };
    },
    computed: {
      points() {
        if (this.startAnchor === 'bottom' && this.endAnchor === 'right' && this.startX > this.endX && this.startY < this.endY) {
          return `${this.startX},${this.startY} ${this.startX},${this.endY} ${this.endX},${this.endY}`;
        } else if (this.startAnchor === 'bottom' && this.endAnchor === 'left' && this.startX < this.endX && this.startY < this.endY) {
          return `${this.startX},${this.startY} ${this.startX},${this.endY} ${this.endX},${this.endY}`;
        } else {
          const halfY = this.startY + (Math.abs(this.endY - this.startY) / 2);
          return `${this.startX},${this.startY} ${this.startX},${halfY} ${this.endX},${halfY} ${this.endX},${this.endY}`;
        }
      },
    },
    methods: {
      extractDomPosition(id, pos) {
        const dom = document.getElementById(id);
        if (dom) {
          const vue = dom.__vue__;

          switch (pos) {
          case 'bottom':
            return vue.getBottomEdgePos();
          case 'top':
            return vue.getTopEdgePos();
          case 'left':
            return vue.getLeftEdgePos();
          case 'right':
            return vue.getRightEdgePos();
          default:
            return new Error('NOT IMPLEMENTED!');
          }
        }
        return new Error(`ID: ${id} could not be found by id in the DOM.`);
      },
    },
    mounted() {
      this.startAnchor = this.startAnchor ? this.startAnchor : 'bottom';
      this.endAnchor = this.endAnchor ? this.endAnchor : 'top';

      const startPos = this.extractDomPosition(this.startNodeId, this.startAnchor);
      const endPos = this.extractDomPosition(this.endNodeId, this.endAnchor);
      this.startX = startPos.x;
      this.startY = startPos.y;
      this.endX = endPos.x;
      this.endY = endPos.y;
    },
  };
</script>

<style scoped>

</style>
