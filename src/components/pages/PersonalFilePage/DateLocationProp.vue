<template>
  <div>
    <p>{{ formatDate(this.date) }}</p>
    <p>
      {{ formatLocation(this.location) }}
      <a v-if="elvis(this.location, 'notes')" :id="locNotesId">
        <font-awesome-icon icon="sticky-note"/>
        <b-popover :target="locNotesId" :title="Lang('ppage.note')" triggers="hover">
          "hiiii"
        </b-popover>
      </a>
    </p>
  </div>

</template>

<script>
export default {
  name: 'DateLocationProp',
  props: ['date', 'location', 'notes', 'type'],
  computed: {
    locNotesId() {
      return this.type + 'loc-notes'
    }
  },
};
</script>

<style scoped>

</style>
