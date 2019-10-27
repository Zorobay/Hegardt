<template>
  <b-container>
    <b-row>
      <b-col cols="1">
        <font-awesome-icon icon="calendar-alt"/>
      </b-col>
      <b-col cols="8">
        <p>{{this.date}}</p>
      </b-col>
    </b-row>
    <b-row>
      <b-col cols="1">
        <font-awesome-icon icon="map-marked-alt"/>
      </b-col>
      <b-col cols="8"><p>{{this.location}}</p></b-col>
    </b-row>
  </b-container>
</template>

<script>
  export default {
    props: ["date", "location"],
    name: "WellCell"
  }
</script>

<style scoped>

</style>
