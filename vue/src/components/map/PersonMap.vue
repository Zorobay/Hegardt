<script setup lang="ts">
import type { PersonFeature, Styles } from '@/types/open-layers-feature.type.ts';
import { computed, onMounted, ref, shallowRef, useTemplateRef } from 'vue';
import { useRouter } from 'vue-router';
import { formatPersonDate, formatPersonFullName } from '@/helpers/person-helper.ts';
import { fuzzyMatch } from '@/helpers/util-helper.ts';
import OLMap from 'ol/Map';
import type MapBrowserEvent from 'ol/MapBrowserEvent';
import View from 'ol/View';
import Overlay from 'ol/Overlay';
import TileLayer from 'ol/layer/Tile';
import { OSM } from 'ol/source';
import { MousePosition } from 'ol/control';
import Feature from 'ol/Feature.js';
import { defaults as defaultControls } from 'ol/control/defaults.js';
import type { Coordinate } from 'ol/coordinate.js';
import { format as formatCoordinate } from 'ol/coordinate.js';
import { Point } from 'ol/geom.js';
import VectorSource from 'ol/source/Vector.js';
import VectorLayer from 'ol/layer/Vector.js';
import { Icon, Style } from 'ol/style.js';
import AccordionComponent from '@/components/forms/AccordionComponent.vue';
import type BaseEvent from 'ol/events/Event';
import _ from 'lodash';
import CheckboxAccordion from '@/components/forms/CheckboxAccordion.vue';
import type { PersonSummary } from '@/types/person.type.ts';
import { personsApiService } from '@/api/personsApiService.ts';

const allPersonsList = ref<PersonSummary[]>([]);
const router = useRouter();

const isMobile = ref(false);
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
const toggleControlsButtonClass = computed(() => {
  if (isMobile.value) {
    return isMinimized.value ? 'pi pi-angle-double-down' : 'pi pi-angle-double-up';
  }
  return isMinimized.value ? 'pi pi-angle-double-right' : 'pi pi-angle-double-left';
});

// OpenLayers Map setup
let overlay: Overlay | null = null;
let map: OLMap | null = null;
let selectedEventTypes: string[] = [];
let selectedGenders: string[] = [];
const numberFormat = Intl.NumberFormat('en', { minimumFractionDigits: 2 });
const personNameFilterText = ref('');
const swedenCenterCoordinates = [1730386, 9000000];
const projectionWebMercator = 'EPSG:4326'; // Web Mercator
const projectionSphericalMercator = 'EPSG:3857'; // Spherical Mercator
const birthFeatures = shallowRef<PersonFeature[]>([]);
const deathFeatures = shallowRef<PersonFeature[]>([]);
const burialFeatures = shallowRef<PersonFeature[]>([]);
let mapView = new View();
const vectorSource = new VectorSource({ features: [] as PersonFeature[] });
const vectorLayer = new VectorLayer({
  source: vectorSource,
  renderBuffer: 100, // Renders features outside the visible viewport by N pixels
  updateWhileAnimating: false,
  updateWhileInteracting: false,
});

onMounted(async () => {
  try {
    const res = await personsApiService.getAll();
    allPersonsList.value = res.data;
    buildMapFeatures();
    updateMapMarkers();
  } catch (error) {
    console.error(error);
  }
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

  calculateIsMobile();
  window.addEventListener('resize', calculateIsMobile);
});

function getAllFeatures(): PersonFeature[] {
  return [...birthFeatures.value, ...deathFeatures.value, ...burialFeatures.value] as PersonFeature[];
}

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

function onPersonNameChange(): void {
  updateMapMarkers();
}

function onEventTypeSelectionChanged(selected: string[]): void {
  selectedEventTypes = selected;
  updateMapMarkers();
}

function onGenderSelectionChanged(selected: string[]): void {
  selectedGenders = selected.map((s) => s.toUpperCase());
  updateMapMarkers();
}

function updateMapMarkers(): void {
  let features: PersonFeature[] = [];
  vectorSource.clear();
  for (const eventType of selectedEventTypes) {
    if (eventType.toLowerCase() === 'birth') {
      features = features.concat(birthFeatures.value);
    } else if (eventType.toLowerCase() === 'death') {
      features = features.concat(deathFeatures.value);
    } else {
      features = features.concat(burialFeatures.value);
    }
  }
  features = features.filter((f: PersonFeature) => {
    return selectedGenders.some((g) => g === f.attributes?.gender?.toUpperCase());
  });
  features = features.filter((f) =>
    f.attributes?.fullName ? fuzzyMatch(f.attributes.fullName, personNameFilterText.value) : false,
  );
  vectorSource.addFeatures(features);
}

function buildMapFeatures(): void {
  for (const person of allPersonsList.value) {
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
          birthFeatures.value.push(feature);
        } else if (eventType === 'death') {
          deathFeatures.value.push(feature);
        } else {
          burialFeatures.value.push(feature);
        }

        feature.getGeometry()?.transform(projectionWebMercator, projectionSphericalMercator);
      }
    }
  }
  // TODO for each group of features, if group has more than 1 element (same coordinates)
  // Distribute them in an expanding fan pattern
  const groupedFeatures = _.groupBy(getAllFeatures(), (feature: PersonFeature) => {
    return (feature.getGeometry() as Point).getCoordinates().join(','); // also fix this — see note below
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

function styleMapFeatures(): void {
  let styles = buildMarkerStyles('green');
  birthFeatures.value.forEach((f) => {
    f.setStyle(styles.normal);
    f.styles = styles;
  });
  styles = buildMarkerStyles('red');
  deathFeatures.value.forEach((f) => {
    f.setStyle(styles.normal);
    f.styles = styles;
  });
  styles = buildMarkerStyles('purple');
  burialFeatures.value.forEach((f) => {
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

function renderMap(): void {
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

function calculateIsMobile(): void {
  isMobile.value = window.innerWidth <= 992;
}
</script>

<template>
  <div id="main-div">
    <CardPrime id="map-controls" :class="{ minimized: isMinimized }">
      <template #content>
        <div class="accordion-div">
          <AccordionPrime :value="['0']" multiple>
            <CheckboxAccordion
              value="0"
              heading="Event Type"
              :items="['Birth', 'Death', 'Burial']"
              @selection-changed="onEventTypeSelectionChanged"
            />
            <CheckboxAccordion
              value="1"
              heading="Gender"
              :items="['Man', 'Woman', 'Unknown']"
              @selection-changed="onGenderSelectionChanged"
            />
            <AccordionComponent heading="Person Name" value="2">
              <input
                v-model="personNameFilterText"
                class="form-control"
                type="search"
                placeholder="Name..."
                @keyup="onPersonNameChange"
              />
            </AccordionComponent>
            <AccordionComponent heading="Marker Size" value="3">
              <div id="marker-size-input" class="d-flex gap-2 align-items-center w-100">
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
          </AccordionPrime>
        </div>
        <ButtonPrime
          id="collapse-button"
          :icon="toggleControlsButtonClass"
          aria-label="Toggle Controls"
          @click="isMinimized = !isMinimized"
        />
      </template>
    </CardPrime>
    <CardPrime id="map-card">
      <template #content>
        <div id="map"></div>
        <div v-show="showPopup" ref="popup" class="ol-popup">
          <div class="ol-popup-header">{{ popupHeader }}</div>
          <div class="ol-popup-event-type">{{ popupEventType }}</div>
          <div class="ol-popup-date">{{ popupDate }}</div>
        </div>
      </template>
    </CardPrime>
  </div>
</template>

<style scoped>
#main-div {
  display: flex;
  gap: 1rem; /* Space between elements */
}

#map-controls {
  flex-shrink: 0; /* Don't shrink below content width */
  width: 20rem;
  transition: width 0.3s ease;
  overflow: hidden;
}

#map-controls.minimized {
  width: 4rem;
}

#map-card {
  flex: 1; /* Take up remaining space */
  overflow: hidden;
}

#map-card :deep(.p-card-body) {
  padding: 0;
  overflow: hidden;
  border-radius: inherit;
}

#map {
  width: 100%;
  height: 50rem;
  border-radius: inherit;
}

#map-controls .accordion-div {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  opacity: 1;
  transition: opacity 0.35s ease;
  overflow: hidden;
}

#map-controls.minimized .accordion-div {
  opacity: 0;
}

#collapse-button {
  margin-top: auto;
  padding: 0;
  width: 100%;
  height: 2rem;
  flex-shrink: 0;
}

.ol-popup {
  background-color: var(--jet-black);
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

/* Mobile-specific styles */
@media (width <= 991px) {
  #map-controls {
    width: 100%;
    margin-bottom: 1rem;
  }

  #map-controls.minimized {
    width: 100%;
    height: 4rem;
  }

  #map {
    height: 60vh;
    min-height: 400px;
  }

  .ol-popup {
    width: auto;
    min-width: 150px;
  }
}

/* Very small screens */
@media (width <= 576px) {
  #map {
    height: 50vh;
    min-height: 300px;
  }
}
</style>
