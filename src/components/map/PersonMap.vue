<template>
  <div class="row" id="main-div">
    <div class="col-auto">
      <div class="card card-body" :class="{ minimized: isMinimized }" id="map-controls">
        <form>
          <CheckboxAccordion
            heading="Event Type"
            :items="['Birth', 'Death', 'Burial']"
            @selection-changed="onEventTypeSelectionChanged"
          />
          <CheckboxAccordion
            heading="Gender"
            :items="['Man', 'Woman', 'Unknown']"
            @selection-changed="onGenderSelectionChanged"
          />
          <AccordionComponent heading="Person Name">
            <input
              v-model="personNameFilterText"
              class="form-control"
              type="search"
              placeholder="Name..."
              @keyup="onPersonNameChange"
            />
          </AccordionComponent>
          <AccordionComponent heading="Marker Size">
            <div class="d-flex gap-2 align-items-center w-100" id="marker-size-input">
              <input
                v-model="markerSize"
                type="range"
                min="0.1"
                max="1"
                step="0.05"
                class="flex-grow-1"
                @change="styleMapFeatures"
              />
              <data :value="markerSizeComp" class="float-end">{{ markerSizeComp }}</data>
            </div>
          </AccordionComponent>
        </form>
        <button
          id="collapse-button"
          class="btn btn-primary"
          role="button"
          @click="isMinimized = !isMinimized"
        >
          <font-awesome-icon icon="fa-solid fa-angles-up" :rotation="isMinimized ? 90 : 270" />
        </button>
      </div>
    </div>
    <div class="col">
      <div id="map"></div>
      <div v-show="showPopup" ref="popup" class="ol-popup">
        <div class="ol-popup-header">{{ popupHeader }}</div>
        <div class="ol-popup-event-type">{{ popupEventType }}</div>
        <div class="ol-popup-date">{{ popupDate }}</div>
      </div>
    </div>
  </div>
  <p>{{ isMinimized }}</p>
</template>

<script setup lang="ts">
import { PersonFeature, Styles } from '@/types/open-layers-feature.type.ts';
import { computed, onMounted, ref, useTemplateRef } from 'vue';
import { useRouter } from 'vue-router';
import { formatPersonDate, formatPersonFullName } from '@/helpers/person-helper.ts';
import { fuzzyMatch } from '@/helpers/util-helper.ts';
import OLMap from 'ol/Map';
import type MapBrowserEvent from 'ol/MapBrowserEvent'; // Import as type from correct path
import View from 'ol/View';
import Overlay from 'ol/Overlay';
import TileLayer from 'ol/layer/Tile';
import { OSM } from 'ol/source';
import { MousePosition } from 'ol/control';
import Feature from 'ol/Feature.js';
import { defaults as defaultControls } from 'ol/control/defaults.js';
import { Coordinate, format as formatCoordinate } from 'ol/coordinate.js';
import personService from '@/services/PersonService.ts';
import { Point } from 'ol/geom.js';
import VectorSource from 'ol/source/Vector.js';
import VectorLayer from 'ol/layer/Vector.js';
import { Icon, Style } from 'ol/style.js';
import AccordionComponent from '@/components/forms/AccordionComponent.vue';
import CheckboxAccordion from '@/components/forms/CheckboxAccordion.vue';
import BaseEvent from 'ol/events/Event';
import _ from 'lodash';

const router = useRouter();

const isMinimized = ref(false);
const markerSize = ref(0.4);
const markerSizeComp = computed(() => {
  return numberFormat.format(markerSize.value);
});
const showPopup = ref(false);
const popupRef = useTemplateRef('popup');
const popupHeader = ref<string | undefined>('');
const popupEventType = ref<string | undefined>('');
const popupDate = ref<string | undefined>('');
let prevHoveredFeature: PersonFeature | null = null;

let overlay: Overlay | null = null;
let map: OLMap | null = null;
let selectedEventTypes: string[] = [];
let selectedGenders: string[] = [];
const numberFormat = Intl.NumberFormat('en', { minimumFractionDigits: 2 });
const personNameFilterText = ref('');
const swedenCenterCoordinates = [1730386, 9000000];
const projectionWebMercator = 'EPSG:4326'; // Web Mercator
const projectionSphericalMercator = 'EPSG:3857'; // Spherical Mercator
const birthFeatures: PersonFeature[] = [];
const deathFeatures: PersonFeature[] = [];
const burialFeatures: PersonFeature[] = [];
let mapView = new View();
const vectorSource = new VectorSource({ features: [] as PersonFeature[] });
const vectorLayer = new VectorLayer({ source: vectorSource });

const allFeatures = function (): PersonFeature[] {
  return [...birthFeatures, ...deathFeatures, ...burialFeatures];
};
const coordinateFormatFunc = function (coordinate: Coordinate | undefined): string {
  if (coordinate) {
    return formatCoordinate(coordinate, '{y}, {x}', 4);
  }
  return '';
};

const mousePositionControl = new MousePosition({
  coordinateFormat: coordinateFormatFunc,
  projection: projectionWebMercator,
});

function onPersonNameChange() {
  updateMapMarkers();
}

function onEventTypeSelectionChanged(selected: string[]) {
  selectedEventTypes = selected;
  updateMapMarkers();
}

function onGenderSelectionChanged(selected: string[]) {
  selectedGenders = selected.map((s) => s.toUpperCase());
  updateMapMarkers();
}

function updateMapMarkers() {
  let allFeatures: PersonFeature[] = [];
  vectorSource.clear();
  for (const eventType of selectedEventTypes) {
    if (eventType.toLowerCase() === 'birth') {
      allFeatures = allFeatures.concat(birthFeatures);
    } else if (eventType.toLowerCase() === 'death') {
      allFeatures = allFeatures.concat(deathFeatures);
    } else {
      allFeatures = allFeatures.concat(burialFeatures);
    }
  }
  allFeatures = allFeatures.filter((f: PersonFeature) => {
    return selectedGenders.some((g) => g === f.attributes?.gender?.toUpperCase());
  });
  allFeatures = allFeatures.filter((f) =>
    f.attributes?.fullName
      ? fuzzyMatch(f.attributes?.fullName ?? '', personNameFilterText.value)
      : false,
  );
  vectorSource.addFeatures(allFeatures);
}

function buildMapFeatures() {
  for (const person of personService.getAllPersonsList()) {
    for (const eventType of ['birth', 'death', 'burial'] as const) {
      const location = person[eventType].location;
      const name = formatPersonFullName(person);
      const date = formatPersonDate(person[eventType]?.date);

      if (location) {
        const coordinate = [location.longitude ?? 0, location.latitude ?? 0];

        const feature: PersonFeature = new Feature({
          geometry: new Point(coordinate),
          labelPoint: new Point(coordinate),
        });
        feature.attributes = {
          fullName: name,
          date: date,
          eventType: eventType,
          gender: person['sex'],
          id: person.id,
        };

        if (eventType === 'birth') {
          birthFeatures.push(feature);
        } else if (eventType === 'death') {
          deathFeatures.push(feature);
        } else {
          burialFeatures.push(feature);
        }

        feature.getGeometry()?.transform(projectionWebMercator, projectionSphericalMercator);
      }
    }
  }
  // TODO for each group of features, if group has more than 1 element (same coordinates)
  // Distribute them in an expanding fan pattern
  const groupedFeatures = _.groupBy(allFeatures(), (feature: PersonFeature) => {
    return (feature.getGeometry() as Point).getCoordinates();
  });
  for (const groupKey in groupedFeatures) {
    const group = groupedFeatures[groupKey];
    let i = 0;

    for (const feature of group) {
      const coordinates = (feature.getGeometry() as Point).getCoordinates();
      const theta = 20 * i;
      const r = 5 * i;
      const h = coordinates[0];
      const k = coordinates[1];
      const x = h + r * Math.cos(theta);
      const y = k + r * Math.sin(theta);
      feature.setGeometry(new Point([x, y]));
      i += 1;
    }
  }
  styleMapFeatures();
}

function styleMapFeatures() {
  let styles = buildMarkerStyles('green');
  birthFeatures.forEach((f) => {
    f.setStyle(styles.normal);
    f.styles = styles;
  });
  styles = buildMarkerStyles('red');
  deathFeatures.forEach((f) => {
    f.setStyle(styles.normal);
    f.styles = styles;
  });
  styles = buildMarkerStyles('purple');
  burialFeatures.forEach((f) => {
    f.setStyle(styles.normal);
    f.styles = styles;
  });
}

function buildMarkerStyles(color: string): Styles {
  return {
    normal: new Style({
      image: new Icon({
        color: color,
        src: 'svg/map-marker.svg',
        scale: markerSize.value,
      }),
    }),
    hover: new Style({
      image: new Icon({
        color: color,
        src: 'svg/map-marker.svg',
        scale: markerSize.value * 1.5,
      }),
    }),
  };
}

function renderMap() {
  mapView = new View({
    center: swedenCenterCoordinates,
    zoom: 5,
    projection: projectionSphericalMercator,
    constrainResolution: true,
  });

  map = new OLMap({
    target: 'map',
    controls: defaultControls().extend([mousePositionControl]),
    layers: [
      new TileLayer({
        source: new OSM(),
      }),
      vectorLayer,
    ],
    view: mapView,
    overlays: [overlay!],
  });
}

function onPointerMove(evt: BaseEvent | Event): void {
  const event = evt as MapBrowserEvent<PointerEvent>;
  const feature = map?.forEachFeatureAtPixel(event.pixel, (feature) => feature) as PersonFeature;

  if (feature) {
    map?.getTargetElement()?.style?.setProperty('cursor', 'pointer');

    if (feature !== prevHoveredFeature) {
      // Reset previous feature style
      prevHoveredFeature?.setStyle(prevHoveredFeature?.styles?.normal);
      prevHoveredFeature = feature;
      feature.setStyle(feature.styles?.hover);

      popupHeader.value = feature.attributes?.fullName;
      popupEventType.value = feature.attributes?.eventType;
      popupDate.value = feature.attributes?.date;

      const coordinates = (feature.getGeometry() as Point)?.getCoordinates();
      overlay?.setPosition(coordinates);
      showPopup.value = true;
    }
  } else {
    // Reset previous feature style
    prevHoveredFeature?.setStyle(prevHoveredFeature?.styles?.normal);

    map?.getTargetElement()?.style?.setProperty('cursor', '');
    prevHoveredFeature = null;
    showPopup.value = false;
  }
}

function onMapClick(evt: BaseEvent | Event): void {
  const event = evt as MapBrowserEvent<PointerEvent>;
  const feature = map?.forEachFeatureAtPixel(event.pixel, (feature) => feature) as PersonFeature;
  if (feature) {
    router.push({
      name: 'person',
      params: { id: feature.attributes?.id },
    });
  }
}

// Immediately build map features
buildMapFeatures();

onMounted(() => {
  overlay = new Overlay({
    element: popupRef.value ?? undefined,
    autoPan: false,
    positioning: 'bottom-center',
    stopEvent: false,
    offset: [0, -30],
  });
  renderMap();
  map?.on('pointermove', onPointerMove);
  map?.on('singleclick', onMapClick);
});
</script>

<style scoped>
#main-div > * {
  padding-right: 0.5rem;
  padding-left: 0.5rem;
}

#map-controls {
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 20rem; /* Add fixed width */
  transition: width 0.3s ease;
  overflow: hidden;
}

#map-controls form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  opacity: 1;
  transition: opacity 0.35s ease;
  overflow: hidden;
}

#map-controls.minimized {
  width: 4rem; /* Animate to button width */
}

#map-controls.minimized form {
  opacity: 0;
  /* Remove max-width animation since we're animating the parent width */
}

#collapse-button {
  margin-top: auto;
  padding: 0;
  width: 100%;
  height: 2rem;
  flex-shrink: 0;
}

#map {
  width: 100%;
  height: 50rem;
}

.ol-popup {
  background-color: var(--color-info-background);
  color: white;
  text-align: center;
  border-radius: 0.5rem;
  width: 130%;
}

.ol-popup-header {
  font-weight: bold;
}

.ol-popup-event-type {
  text-transform: capitalize;
}
</style>
