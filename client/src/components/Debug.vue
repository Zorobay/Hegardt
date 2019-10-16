<template>
  <div>
    <input placeholder="Search term" v-model="searchTerm">
    <button v-on:click="search">Search</button>
    <p>{{response}}</p>
    <leaflet-map :key="markers" id="leaflet-map" ref="map" v-bind:markers="markers"></leaflet-map>
  </div>
</template>

<script>
  import LeafletMap from "./pages/MapPage/LeafletMap";
  import GeoSearcher from "../common/GeoSearcher"
    let geo = new GeoSearcher();

  export default {
    name: "Debug",
    components: {LeafletMap},
    data() {
      return {
        markers: [],
        searchTerm: "",
        response: ""
      }
    },
    methods: {
      search(event) {
        geo.search("New York, NY").then(res => this.response = res);
        console.log("Searched for " + this.searchTerm);
      }
    }
  }
</script>

<style scoped>
    /*Important import to make the leaflet map work*/
    @import "~leaflet/dist/leaflet.css";

    #leaflet-map {
        position: fixed;
        align-self: center;
        left: 5%;
        width: 90%;
        height: 70%;
    }
</style>
