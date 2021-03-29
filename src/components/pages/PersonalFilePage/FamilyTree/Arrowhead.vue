<template>
  <defs>
    <marker id="arrowhead" :markerWidth="length" :markerHeight="width"
    :refX="refX" :refY="refY" orient="auto" class="arrowhead">
      <polygon :points="points" />
    </marker>
  </defs>
</template>

<script>
  export default {
    name: 'Arrowhead',
    props: ['width', 'length', 'scale'],
    computed: {
      refY() {
        return this.width / 2;
      },
      refX() {
        return this.length;
      },
      points() {
        return `0 0, ${this.length} ${this.width / 2}, 0 ${this.width}`;
      },
    },
  };
</script>

<style scoped>

</style>
