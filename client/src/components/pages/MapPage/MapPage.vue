<template>
  <div>
    <h1>People Map! <b-spinner v-if="!loaded"></b-spinner></h1>
    <leaflet-map id="leaflet-map" v-bind:people="persons" :key="persons.length"></leaflet-map>
  </div>
</template>

<script>
  import LeafletMap from "./LeafletMap";
  import {FETCH_ALL_PEOPLE} from "../../../store/actions.type";

  const API_URL = "http://localhost:3000/person/id/000000000000000000000384";

  export default {
    name: "MapPage",
    components: {LeafletMap},
    data() {
      return {
        persons: [],
        loaded: false
      }
    },
    created() {
      if (this.$store.getters.allPeopleFetched) {
        this.persons = this.$store.getters.people;
        this.loaded = true;
      } else {
        this.$store.dispatch(FETCH_ALL_PEOPLE)
          .then(data => {
            this.persons = data;
            this.loaded = true;
          });
      }
    }
  }
</script>

<style scoped>

  /*Important import to make the leaflet map work*/
  @import "../../../../node_modules/leaflet/dist/leaflet.css";

  #leaflet-map {
    position: fixed;
    align-self: center;
    left: 5%;
    width: 90%;
    height: 70%;
  }


</style>
