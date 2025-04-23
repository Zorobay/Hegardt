<template>
  <form>
    <div class="input-group">
      <span class="input-group-text">Filter people</span>
      <input type="text" v-model="filterText" @keyup="onFilterPeopleChange"/>
    </div>
    <Dropdown label="Show markers for" :options="['Birth', 'Death', 'Burial']" :selected="['Birth', 'Death']" multiselect="true"
              @selection-change="onShowMarkersSelectionChange"/>
    <div class="input-group">
      <span class="input-group-text">Marker size: {{ numberFormat.format(markerSize) }}</span>
      <input type="range" min="0.02" max="1" step="0.02" v-model="markerSize" @change="styleMapFeatures"/>
    </div>
  </form>
  <div id="map"></div>
</template>

<script setup>
import {onMounted, ref} from 'vue';
import {formatPersonFullName} from "@/helpers/person-helper.js";
import {Map, View} from 'ol';
import TileLayer from 'ol/layer/Tile';
import {OSM} from 'ol/source';
import {MousePosition} from 'ol/control';
import Feature from 'ol/Feature.js';
import {defaults as defaultControls} from 'ol/control/defaults.js';
import {format as formatCoordinate} from 'ol/coordinate.js';
import personService from '@/services/PersonService.js'
import Dropdown from '@/components/forms/Dropdown.vue'
import {Point} from 'ol/geom.js'
import VectorSource from 'ol/source/Vector.js'
import VectorLayer from 'ol/layer/Vector.js'
import {Icon, Style} from 'ol/style.js'

const markerSize = ref(0.10);
let selectedMarkerCategories = [];
const numberFormat = Intl.NumberFormat('en', {minimumFractionDigits: 2});
const filterText = ref('');
const swedenCenterCoordinates = [1730386, 9000000];
const projectionWebMercator = 'EPSG:4326'; // Web Mercator
const projectionSphericalMercator = 'EPSG:3857'; // Spherical Mercator
const birthFeatures = [];
const deathFeatures = [];
const burialFeatures = [];
let mapView = new View();
const vectorSource = new VectorSource({features: []});
const vectorLayer = new VectorLayer({source: vectorSource});
const coordinateFormatFunc = function (coordinate) {
  return formatCoordinate(coordinate, '{y}, {x}', 4);
}
const mousePositionControl = new MousePosition({
  coordinateFormat: coordinateFormatFunc,
  projection: projectionWebMercator,
})

function onFilterPeopleChange() {
  updateMapMarkers();
}

function onShowMarkersSelectionChange(selected) {
  selectedMarkerCategories = selected
  updateMapMarkers();
}

function updateMapMarkers() {
  let allFeatures = [];
  vectorSource.clear();
  for (const markerCategory of selectedMarkerCategories) {
    if (markerCategory.toLowerCase() === 'birth') {
      allFeatures = allFeatures.concat(birthFeatures);
    } else if (markerCategory.toLowerCase() === 'death') {
      allFeatures = allFeatures.concat(deathFeatures);
    } else {
      allFeatures = allFeatures.concat(burialFeatures);
    }
  }
  debugger;
  allFeatures = allFeatures.filter(f => f.attributes.fullName ? f.attributes.fullName.toLowerCase().includes(filterText.value.toLowerCase()) : false)
  debugger;
  vectorSource.addFeatures(allFeatures);
}

function buildMapFeatures() {
  for (const person of personService.getAllPersonsList()) {
    for (const markerCategory of ['birth', 'death', 'burial']) {
      const location = person[markerCategory].location;
      const name = formatPersonFullName(person);

      if (location) {
        const coordinate = [location.longitude, location.latitude];

        const feature = new Feature({
          geometry: new Point(coordinate),
          labelPoint: new Point(coordinate)
        });
        feature.attributes = {'fullName': name}

        if (markerCategory === 'birth') {
          birthFeatures.push(feature);
        } else if (markerCategory === 'death') {
          deathFeatures.push(feature);
        } else {
          burialFeatures.push(feature);
        }

        feature.getGeometry().transform(projectionWebMercator, projectionSphericalMercator);
      }
    }
  }
  styleMapFeatures();
}

function styleMapFeatures() {
  let style = buildMarkerStyle('green');
  birthFeatures.forEach(f => f.setStyle([style]));
  style = buildMarkerStyle('red');
  deathFeatures.forEach(f => f.setStyle([style]))
  style = buildMarkerStyle('purple');
  burialFeatures.forEach(f => f.setStyle([style]));
}

function buildMarkerStyle(color) {
  return new Style({
    image: new Icon({
      color: color,
      src: 'svg/map-marker.svg',
      scale: markerSize.value
    })
  });
}

function renderMap() {
  mapView = new View({
    center: swedenCenterCoordinates,
    zoom: 5,
    projection: projectionSphericalMercator,
    constrainResolution: true,
  });

  new Map({
    target: 'map',
    controls: defaultControls().extend([mousePositionControl]),
    layers: [
      new TileLayer({
        source: new OSM(),
      }),
      vectorLayer
    ],
    view: mapView,
  });
}

// Immediately build map features
buildMapFeatures();

onMounted(() => {
  renderMap();
})

</script>

<style scoped>
#map {
  width: 100%;
  height: 50rem;
  margin-top: 1rem;
  margin-bottom: 1rem;
}

.ol-mouse-position {
}

</style>
