<template>
  <g>
    <ellipse
      :rx="nodeWidth/2" :ry="nodeHeight/2"
      :cx="x" :cy="y" class="node marriage-node"
    />
<!--    <rect-->
<!--      :height="nodeHeight" :width="nodeWidth"-->
<!--      :transform="rectCenterTransform"-->
<!--      :x="x"-->
<!--      :y="y"-->
<!--      rx="20" ry="20"/>-->
    <slot/>
      <foreignObject
        :height="textBoxHeight"
        :transform="textCenterTransform" :width="textBoxWidth"
        :x="x"
        :y="y" class="name">
        <p>marriage date</p>
      </foreignObject>
  </g>
</template>

<script>
  import NodeMixin from '@/components/pages/PersonalFilePage/FamilyTree/mixins/NodeMixin';

  export default {
    name: 'MarriageNode',
    props: ['marriage'],
    mixins: [NodeMixin],
    data() {
      return {
      };
    },
  };
</script>

<style scoped>

</style>
