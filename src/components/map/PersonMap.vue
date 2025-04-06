<template>
  <form>
    <LabelledDropdown label="Show markers for" :options="['Birth', 'Death', 'Burial']"/>
  </form>
  <div id="map"></div>
</template>

<script setup>
import {onMounted} from 'vue';
import { Map, View } from 'ol';
import TileLayer from 'ol/layer/Tile';
import { OSM } from 'ol/source';
import {MousePosition} from 'ol/control';
import Feature from 'ol/Feature.js';
import {defaults as defaultControls} from 'ol/control/defaults.js';
import {format as formatCoordinate} from 'ol/coordinate.js';
import personService from '@/services/PersonService.js'
import LabelledDropdown from '@/components/forms/LabelledDropdown.vue'
import { Point } from 'ol/geom.js'
import VectorSource from 'ol/source/Vector.js'
import VectorLayer from 'ol/layer/Vector.js'
import { Style, Circle, Fill, Stroke, Icon } from 'ol/style.js'

onMounted(() => {
  const swedenCenterCoordinates = [1730386, 9000000];
  const projectionWebMercator = 'EPSG:4326'; // Web Mercator
  const projectionSphericalMercator = 'EPSG:3857'; // Spherical Mercator


  const coordinateFormatFunc = function(coordinate) {
    return formatCoordinate(coordinate, '{y}, {x}', 4);
  }
  const mousePositionControl = new MousePosition({
    coordinateFormat: coordinateFormatFunc,
    projection: projectionWebMercator,
  })

  const pointStyle = new Style({
    image: new Circle({
      radius: 7,
      fill: new Fill({
        color: 'black',
      }),
      stroke: new Stroke({
        color: 'white',
        width: 2,
      }),
    }),
  });

  const svg = '<svg width="120" height="120" version="1.1" xmlns="http://www.w3.org/2000/svg">'
    + '<circle cx="60" cy="60" r="60"/>'
    + '</svg>';

  const style = new Style({
    image: new Icon({
      opacity: 1,
      src: 'svg/map-marker-2-svgrepo-com.svg',
      scale: 0.04
    })
  });

  const features = [];

  for (const person of personService.getAllPersonsList()) {
    const location = person.birth.location;
    if (location) {
      const coordinate = [location.longitude, location.latitude];

      const feature = new Feature({
        geometry: new Point(coordinate),
        labelPoint: new Point(coordinate),
        name: 'yo'
      });
      feature.setStyle([style]);

      feature.getGeometry().transform(projectionWebMercator, projectionSphericalMercator);
      features.push(feature);
    }
  }

  const vectorSource = new VectorSource({features: features});
  const vectorLayer = new VectorLayer({source: vectorSource});

  new Map({
    target: 'map',
    controls: defaultControls().extend([mousePositionControl]),
    layers: [
      new TileLayer({
        source: new OSM(),
      }),
      vectorLayer
    ],
    view: new View({
      center: swedenCenterCoordinates,
      zoom: 5,
      projection: projectionSphericalMercator,
      constrainResolution: true,
    }),
  });
})

</script>

<style scoped>
#map {
  width: 100%;
  height: 50rem;
  margin-top: 1rem;
  margin-bottom: 1rem;
}
.ol-mouse-position {}

</style>
