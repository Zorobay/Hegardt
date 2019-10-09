<template>
  <div>
    <h1>People Map!</h1>
    <leaflet-map id="leaflet-map"></leaflet-map>
  </div>
</template>

<script>
  import LeafletMap from "./LeafletMap";

  export default {
    name: "MapPage",
    components: {LeafletMap}
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
    height: 400px;
  }



</style>
