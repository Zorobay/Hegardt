<template>
  <b-row>
    <b-col cols="4">
      <p class="heading">{{ Text(`ppage.${prop}.heading`) }}</p>
    </b-col>
    <b-col cols="8">
      <p class="date">{{ prettyDate(elvis(person, `${prop}.date`)) }}</p>
      <p class="location">{{ formatLocation(elvis(person, `${prop}.location`)) }}</p>
    </b-col>
  </b-row>

</template>

<script>
  export default {
    name: 'DateLocation',
    props: ['person', 'prop'],
  };
</script>

<style scoped>
</style>
