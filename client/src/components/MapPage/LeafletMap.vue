<template>
  <div>
    <div id="map"></div>
  </div>
</template>

<script>
  import * as L from "leaflet";
  export default {
    data() {
      return {
        map: null,
        tileLayer: null,
        layers: [],
      }
    },
    mounted() {
      this.initMap();
      this.initLayers();
    },
    name: "LeafletMap",
    methods: {
      initMap() {
        this.map = L.map('map').setView([38.63, -90.23], 12);
        this.tileLayer = L.tileLayer(
          'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
          {
            maxZoom: 18,
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attribution">CARTO</a>',
          }
        );
        this.tileLayer.addTo(this.map);
      },
      initLayers() {

      }
    }
  }
</script>

<style scoped>
  #map {
    height: 100%
  }

</style>
