import type VectorSource from 'ol/source/Vector.js';
import type { Geometry } from 'ol/geom';
import type Feature from 'ol/Feature.js';
import type VectorLayer from 'ol/layer/Vector.js';

export interface GpxRouteConfig {
  id: number;
  name: string;
  path: string;
  description?: string;
}

export interface GpxRoute {
  id: number;
  name: string;
  description?: string;
  source: VectorSource<Feature<Geometry>>;
  layer: VectorLayer;
  markerLayer: VectorLayer;
}
