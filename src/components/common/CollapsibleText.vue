<template>
  <div>
    <b-collapse :id="collapsibleId" class="collapsible-text">
      <p> {{ text }} </p>
    </b-collapse>

    <span v-b-toggle="collapsibleId" role="button" @click="toggleIcon" ><font-awesome-icon :icon="icon"/></span>
  </div>
</template>

<script>
  export default {
    name: 'CollapsibleText',
    props: ['idPrefix', 'text'],
    data() {
      return {
        collapsibleId: 'collapsible-text-' + this.idPrefix,
        iconDown: 'chevron-down',
        iconUp: 'chevron-up',
        icon: 'chevron-down',
      };
    },
    methods: {
      toggleIcon() {
        this.icon = this.icon === this.iconDown ? this.iconUp : this.iconDown;
      },
    },
  };
</script>

<style scoped>

.collapsible-text.collapse:not(.show) {
  display: block !important;
  height: 200px !important;
  overflow: hidden;
}
</style>
