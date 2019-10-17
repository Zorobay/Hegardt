import {OpenStreetMapProvider} from "leaflet-geosearch";

export default class GeoSearcher {
  constructor() {
    this.provider = new OpenStreetMapProvider();
  }

  async search(phrase, callback) {
    return this.provider.query({query: phrase});
  }
}
