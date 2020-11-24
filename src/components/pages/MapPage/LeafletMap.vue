<template>
  <div>
    <div class="map leaflet-container" id="map"></div>
  </div>
</template>

<script>
  import * as L from 'leaflet';
  import GeoSearcher from '@/common/GeoSearcher';

  export default {
    props: ['people'],
    data() {
      return {
        geosearcher: null,
        map: null,
        tileLayer: null,
        center: [58.3490555, 11.9382855],
        initZoom: 5,
        layers: [],
        mapProviders: {
          openstreet: {
            url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            attrib: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, ' +
              '&copy; <a href="https://carto.com/attribution">CARTO</a>',
          },
          mapc: {
            url: 'http://tiles.mapc.org/basemap/{z}/{x}/{y}.png',
            attrib: 'Tiles by <a href="http://mapc.org">MAPC</a>, Data by <a href="http://mass.gov/mgis">MassGIS</a>',
          },
        },
        markerIcon: L.icon({
          iconUrl: 'icons/standing-up-man.png',
          iconSize: [20, 24],
          iconAnchor: [5, 10],
        }),
      };
    },
    mounted() {
      this.initMap();
      this.addMarkers();
    },
    name: 'LeafletMap',
    methods: {
      initMap() {
        this.geosearcher = new GeoSearcher();
        this.map = L.map('map').setView(this.center, this.initZoom);

        this.tileLayer = L.tileLayer(
          this.mapProviders.openstreet.url,
          {
            maxZoom: 18,
            attribution: this.mapProviders.openstreet.attrib,
          },
        );
        this.tileLayer.addTo(this.map);
      },
      addMarkers() {
        for (const p of this.people) {
          if (!elvis(p, 'birth.location')) {
            continue;
          }

          const longitude = p.birth_location.longitude;
          const latitude = p.birth_location.latitude;

          if (longitude && latitude) {
            const marker = L.marker([latitude, longitude], {icon: this.markerIcon})
              .on('click', function() {
                // TODO Invalid 'this'? this.$router.push({name: 'PersonalFile', params: {id: p._id}});
              })
              .addTo(this.map);
            marker.bindTooltip(p.full_name, {className: 'tooltip', permanent: false, opacity: 0.7});
          }
        }
      },
    },
  };
</script>

<style scoped>
  #map {
    height: 100%
  }

  .leaflet-tooltip-right::before {
    font-size: 100px;
  }

  .tooltip {
    font-size: 1px;
    border: 2px solid cyan;
  }


</style>
