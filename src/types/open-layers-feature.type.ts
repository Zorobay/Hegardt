import Feature from 'ol/Feature.js';
import { Style } from 'ol/style.js';

interface PersonAttributes {
  fullName: string;
  date: string;
  eventType: string;
  gender: string;
  id: string | number;
}

export interface Styles {
  normal: Style;
  hover: Style;
}

export interface PersonFeature extends Feature {
  attributes?: PersonAttributes;
  styles?: Styles;
}
