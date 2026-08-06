<script setup lang="ts">
import { onMounted, ref, shallowRef } from 'vue';
import OLMap from 'ol/Map';
import View from 'ol/View';
import TileLayer from 'ol/layer/Tile';
import { OSM } from 'ol/source';
import { MousePosition } from 'ol/control';
import { defaults as defaultControls } from 'ol/control/defaults.js';
import type { Coordinate } from 'ol/coordinate.js';
import { format as formatCoordinate } from 'ol/coordinate.js';
import VectorSource from 'ol/source/Vector.js';
import VectorLayer from 'ol/layer/Vector.js';
import { Style } from 'ol/style.js';
import { Fill, Stroke, Text } from 'ol/style';
import CircleStyle from 'ol/style/Circle';
import { GPX } from 'ol/format';
import type { GpxRoute, GpxRouteConfig } from '@/types/gpx-route.type.ts';
import Feature from 'ol/Feature.js';
import { Point } from 'ol/geom.js';
import { LineString, MultiLineString } from 'ol/geom';
import { getLength } from 'ol/sphere';
import RunningRoutesTable from '@/components/running-routes/RunningRoutesTable.vue';
import { getDistributedHslColor } from '@/helpers/color-helper.ts';
import { PROJECTION_WEB_MERCATOR, PROJECTION_WGS84, SWEDEN_CENTER_COORDINATES } from '@/constants/geo.constants.ts';

const isMobile = ref(false);

// OpenLayers Map setup
let map: OLMap | null = null;
let mapView = new View();

// GPX Related stuff
const gpxRoutes = shallowRef<GpxRoute[]>([]);
const GPX_ROUTES: GpxRouteConfig[] = [
  { id: 1, name: 'Amager 14.1km', path: '/gpx/onthegomap-14.1-km-route.gpx' },
  { id: 2, name: 'Amager Fælled 10.5km - The Classic', path: '/gpx/Amager Fælled 10.5km - The Classic.gpx' },
];

function getGpxRouteStyle(index: number, total: number): Style {
  return new Style({
    stroke: new Stroke({ color: getDistributedHslColor(index, total), width: 3 }),
  });
}

onMounted(async () => {
  renderMap();
  calculateIsMobile();
  window.addEventListener('resize', calculateIsMobile);

  let i = 0;
  const total = GPX_ROUTES.length;
  for (const route of GPX_ROUTES) {
    const loadedRoute = await loadGpxRoute(route, i, total);
    if (loadedRoute) {
      gpxRoutes.value.push(loadedRoute);
    }
    i++;
  }
});

const coordinateFormatFunc = function (coordinate: Coordinate | undefined): string {
  if (coordinate) {
    return formatCoordinate(coordinate, '{y}, {x}', 4);
  }
  return '';
};

const mousePositionControl = new MousePosition({
  coordinateFormat: coordinateFormatFunc,
  projection: PROJECTION_WGS84,
});

function renderMap(): void {
  mapView = new View({
    center: SWEDEN_CENTER_COORDINATES,
    zoom: 5,
    projection: PROJECTION_WEB_MERCATOR,
    constrainResolution: true,
  });

  map = new OLMap({
    target: 'map',
    controls: defaultControls().extend([mousePositionControl]),
    layers: [
      new TileLayer({
        source: new OSM(),
      }),
    ],
    view: mapView,
  });
}

async function loadGpxRoute(route: GpxRouteConfig, index: number, total: number): Promise<GpxRoute | undefined> {
  const res = await fetch(route.path);
  if (!res.ok) {
    console.error(`Failed to load GPX file from ${route.path}`);
    return;
  }
  const trackLayerSource = new VectorSource();
  const trackLayer = new VectorLayer({
    source: trackLayerSource,
    style: getGpxRouteStyle(index, total),
  });
  const markerLayerSource = new VectorSource();
  const markerLayer = new VectorLayer({
    source: markerLayerSource,
    style: new Style({}),
  });
  map?.addLayer(trackLayer);
  map?.addLayer(markerLayer);

  const text = await res.text();
  const features = new GPX().readFeatures(text, {
    dataProjection: PROJECTION_WGS84, // GPX is always WGS84
    featureProjection: PROJECTION_WEB_MERCATOR, // Your map projection
  });
  trackLayerSource.addFeatures(features);
  addRouteMarkers(features, markerLayerSource);

  //  Fit the map view to the track extent
  const extent = trackLayerSource.getExtent();
  mapView.fit(extent, { padding: [40, 40, 40, 40], duration: 800 });

  return {
    id: route.id,
    name: route.name,
    description: route.description,
    source: trackLayerSource,
    layer: trackLayer,
    markerLayer: markerLayer,
  };
}

function addRouteMarkers(features: Feature[], markerSource: VectorSource): void {
  markerSource.clear();

  const lineFeature = features.find(
    (f) => f.getGeometry()?.getType() === 'LineString' || f.getGeometry()?.getType() === 'MultiLineString',
  );

  if (!lineFeature) return;

  const geom = lineFeature.getGeometry();
  let coords = [] as Coordinate[];
  if (geom instanceof LineString) {
    coords = geom.getCoordinates();
  } else if (geom instanceof MultiLineString) {
    coords = geom.getCoordinates().flatMap((cs) => cs);
  }

  markerSource.addFeature(createTextMarker(coords[0], '🟢'));
  markerSource.addFeature(createTextMarker(coords[coords.length - 1], '🏁'));

  let distanceCovered = 0;
  let kmCount = 1;

  for (let i = 1; i < coords.length; i++) {
    const segment = new LineString([coords[i - 1], coords[i]]);
    distanceCovered += getLength(segment, { projection: PROJECTION_WEB_MERCATOR });

    if (distanceCovered >= kmCount * 1000) {
      markerSource.addFeature(createKmMarker(coords[i], kmCount));
      kmCount++;
    }
  }
}

function createTextMarker(coordinate: number[], label: string, fontSize: number = 1.7): Feature {
  const feature = new Feature({ geometry: new Point(coordinate) });
  feature.setStyle(
    new Style({
      text: new Text({
        text: label,
        scale: fontSize,
        stroke: new Stroke({ color: '#fff', width: 3 }),
      }),
    }),
  );
  return feature;
}

function createKmMarker(coordinate: Coordinate, km: number, fontSize: number = 1.1): Feature {
  const feature = new Feature({ geometry: new Point(coordinate) });
  feature.setStyle(
    new Style({
      image: new CircleStyle({
        radius: 10,
        fill: new Fill({ color: 'white' }),
        stroke: new Stroke({ color: 'black' }),
      }),
      text: new Text({
        text: String(km),
        scale: fontSize,
      }),
    }),
  );
  return feature;
}

function calculateIsMobile(): void {
  isMobile.value = window.innerWidth <= 992;
}

function onTableSelectionChanged({ route, show }: { route: GpxRoute; show: boolean }): void {
  route.layer.setVisible(show);
  route.markerLayer.setVisible(show);
}
</script>

<template>
  <div id="main-div">
    <CardPrime id="map-card">
      <template #content>
        <div id="map"></div>
      </template>
    </CardPrime>

    <RunningRoutesTable :data="gpxRoutes" @selection-changed="onTableSelectionChanged" />
  </div>
</template>

<style scoped>
#main-div {
  display: flex;
  flex-direction: column;
  gap: 1rem; /* Space between elements */
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

/* Mobile-specific styles */
@media (width <= 991px) {
  #map {
    height: 60vh;
    min-height: 400px;
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
