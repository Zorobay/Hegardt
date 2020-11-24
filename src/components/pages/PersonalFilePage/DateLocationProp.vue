<template>
  <div>
    <h4>
      {{heading}}
      <a v-if="notes" :id="notesId">
        <font-awesome-icon icon="sticky-note" size="xs" fixed-width/>
        <b-popover :target="notesId" :title="Lang('ppage.note')" triggers="hover">
          {{notes}}
        </b-popover>
      </a>
    </h4>
    <p>{{ formatDate(this.date) }}</p>
    <p>
      {{ formatLocation(this.location) }}
      <a v-if="elvis(this.location, 'notes')" :id="locNotesId">
        <font-awesome-icon icon="sticky-note" size="xs" fixed-width/>
        <b-popover :target="locNotesId" :title="Lang('ppage.note')" triggers="hover">
          {{elvis(location, 'notes')}}
        </b-popover>
      </a>
    </p>
  </div>

</template>

<script>
  export default {
    name: 'DateLocationProp',
    props: ['heading', 'date', 'location', 'notes', 'type'],
    computed: {
      locNotesId() {
        return this.type + 'loc-notes';
      },
      notesId() {
        return this.type + 'notes';
      },
    },
  };
</script>

<style scoped>

</style>
