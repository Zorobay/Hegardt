<template>
  <div class="row">
    <div class="col-3">
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
        <Accordion heading="Person Name">
          <input
            class="form-control"
            type="search"
            v-model="personNameFilterText"
            placeholder="Name..."
            @keyup="onPersonNameChange"
          />
        </Accordion>
        <Accordion heading="Marker Size">
          <div class="d-flex gap-2 align-items-center">
            <input
              type="range"
              min="0.02"
              max="0.5"
              step="0.02"
              v-model="markerSize"
              @change="styleMapFeatures"
            />
            <data :value="markerSizeComp">{{ markerSizeComp }}</data>
          </div>
        </Accordion>
      </form>
    </div>
    <div class="col-9">
      <div id="map"></div>
      <div ref="popup" class="ol-popup" v-show="showPopup">
        <div class="ol-popup-header">{{ popupHeader }}</div>
        <div class="ol-popup-event-type">{{ popupEventType }}</div>
        <div class="ol-popup-date">{{ popupDate }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref, useTemplateRef } from 'vue'
import {useRouter} from 'vue-router'
import { formatPersonDate, formatPersonFullName } from '@/helpers/person-helper.js'
import {fuzzyMatch} from '@/helpers/util-helper.js'
import { Map, Overlay, View } from 'ol'
import TileLayer from 'ol/layer/Tile'
import { OSM } from 'ol/source'
import { MousePosition } from 'ol/control'
import Feature from 'ol/Feature.js'
import { defaults as defaultControls } from 'ol/control/defaults.js'
import { format as formatCoordinate } from 'ol/coordinate.js'
import personService from '@/services/PersonService.js'
import { Point } from 'ol/geom.js'
import VectorSource from 'ol/source/Vector.js'
import VectorLayer from 'ol/layer/Vector.js'
import { Icon, Style } from 'ol/style.js'
import Accordion from '@/components/forms/Accordion.vue'
import CheckboxAccordion from '@/components/forms/CheckboxAccordion.vue'

const router = useRouter();

const markerSize = ref(0.1)
const markerSizeComp = computed(() => {
  return numberFormat.format(markerSize.value)
})
const showPopup = ref(false)
const popupRef = useTemplateRef('popup')
const popupHeader = ref('')
const popupEventType = ref('')
const popupDate = ref('')
let prevHoveredFeature = null

let overlay = null
let map = null
let selectedEventTypes = []
let selectedGenders = []
const numberFormat = Intl.NumberFormat('en', { minimumFractionDigits: 2 })
const personNameFilterText = ref('')
const swedenCenterCoordinates = [1730386, 9000000]
const projectionWebMercator = 'EPSG:4326' // Web Mercator
const projectionSphericalMercator = 'EPSG:3857' // Spherical Mercator
const birthFeatures = []
const deathFeatures = []
const burialFeatures = []
let mapView = new View()
const vectorSource = new VectorSource({ features: [] })
const vectorLayer = new VectorLayer({ source: vectorSource })

const coordinateFormatFunc = function (coordinate) {
  return formatCoordinate(coordinate, '{y}, {x}', 4)
}

const mousePositionControl = new MousePosition({
  coordinateFormat: coordinateFormatFunc,
  projection: projectionWebMercator,
})

function onPersonNameChange() {
  updateMapMarkers()
}

function onEventTypeSelectionChanged(selected) {
  selectedEventTypes = selected
  updateMapMarkers()
}

function onGenderSelectionChanged(selected) {
  selectedGenders = selected.map((s) => s.toUpperCase())
  updateMapMarkers()
}

function updateMapMarkers() {
  let allFeatures = []
  vectorSource.clear()
  for (const eventType of selectedEventTypes) {
    if (eventType.toLowerCase() === 'birth') {
      allFeatures = allFeatures.concat(birthFeatures)
    } else if (eventType.toLowerCase() === 'death') {
      allFeatures = allFeatures.concat(deathFeatures)
    } else {
      allFeatures = allFeatures.concat(burialFeatures)
    }
  }
  allFeatures = allFeatures.filter((f) => {
    return selectedGenders.some((g) => g === f.attributes.gender?.toUpperCase())
  })
  allFeatures = allFeatures.filter((f) =>
    f.attributes.fullName
      ? fuzzyMatch(f.attributes.fullName, personNameFilterText.value)
      : false,
  )
  vectorSource.addFeatures(allFeatures)
}

function buildMapFeatures() {
  for (const person of personService.getAllPersonsList()) {
    for (const eventType of ['birth', 'death', 'burial']) {
      const location = person[eventType].location
      const name = formatPersonFullName(person)
      const date = formatPersonDate(person[eventType]?.date)

      if (location) {
        const coordinate = [location.longitude, location.latitude]

        const feature = new Feature({
          geometry: new Point(coordinate),
          labelPoint: new Point(coordinate),
        })
        feature.attributes = {
          fullName: name,
          date: date,
          eventType: eventType,
          gender: person['sex'],
          id: person.id
        }

        if (eventType === 'birth') {
          birthFeatures.push(feature)
        } else if (eventType === 'death') {
          deathFeatures.push(feature)
        } else {
          burialFeatures.push(feature)
        }

        feature.getGeometry().transform(projectionWebMercator, projectionSphericalMercator)
      }
    }
  }
  styleMapFeatures()
}

function styleMapFeatures() {
  let styles = buildMarkerStyles('green')
  birthFeatures.forEach((f) => {
    f.setStyle(styles.normal)
    f.styles = styles
  })
  styles = buildMarkerStyles('red')
  deathFeatures.forEach((f) => {
    f.setStyle(styles.normal)
    f.styles = styles
  })
  styles = buildMarkerStyles('purple')
  burialFeatures.forEach((f) => {
    f.setStyle(styles.normal)
    f.styles = styles
  })
}

function buildMarkerStyles(color) {
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
  }
}

function renderMap() {
  mapView = new View({
    center: swedenCenterCoordinates,
    zoom: 5,
    projection: projectionSphericalMercator,
    constrainResolution: true,
  })

  map = new Map({
    target: 'map',
    controls: defaultControls().extend([mousePositionControl]),
    layers: [
      new TileLayer({
        source: new OSM(),
      }),
      vectorLayer,
    ],
    view: mapView,
    overlays: [overlay],
  })
}

function onPointerLeave() {
  showPopup.value = false
}

function onPointerMove(event) {
  const feature = map.forEachFeatureAtPixel(event.pixel, (feature) => feature)

  if (feature ) {
    map.getTargetElement().style.cursor = 'pointer'

    if (feature !== prevHoveredFeature) {
      // Reset previous feature style
      prevHoveredFeature?.setStyle(prevHoveredFeature?.styles?.normal)
      prevHoveredFeature = feature
      feature.setStyle(feature.styles.hover)

      popupHeader.value = feature.attributes?.fullName
      popupEventType.value = feature.attributes?.eventType
      popupDate.value = feature.attributes?.date

      const coordinates = feature.getGeometry().getCoordinates()
      overlay.setPosition(coordinates)
      showPopup.value = true
    }
  } else {
    // Reset previous feature style
    prevHoveredFeature?.setStyle(prevHoveredFeature?.styles?.normal)

    map.getTargetElement().style.cursor = ''
    prevHoveredFeature = null
    showPopup.value = false
  }

}

function onMapClick(event) {
  const feature = map.forEachFeatureAtPixel(event.pixel, (feature) => feature)
  if (feature) {
    router.push({
      name: 'person',
      params: {id: feature.attributes.id}
    })
  }
}

// Immediately build map features
buildMapFeatures()

onMounted(() => {
  overlay = new Overlay({
    element: popupRef.value,
    autoPan: false,
    positioning: 'bottom-center',
    stopEvent: false,
    offset: [0, -30],
  })
  renderMap()
  map.on('pointermove', onPointerMove)
  map.on('pointerleave', onPointerLeave)
  map.on('click', onMapClick)
})
</script>

<style scoped>
#map {
  width: 100%;
  height: 50rem;
}

form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.ol-popup {
  background-color: var(--color-info-background);
  color: white;
  text-align: center;
  border-radius: 0.5rem;
  width: 130%;

  .ol-popup-header {
    font-weight: bold;
  }

  .ol-popup-event-type {
    text-transform: capitalize;
  }
}
</style>
