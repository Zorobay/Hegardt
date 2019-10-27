<template>
  <div>
    <h1>People Map!
      <b-spinner v-if="!loaded"></b-spinner>
    </h1>
    <map-controls></map-controls>
    <p>{{mapSettings}}</p>
    <leaflet-map :key="fPeople.length" id="leaflet-map" v-bind:people="fPeople"></leaflet-map>
  </div>
</template>

<script>
  import LeafletMap from "./LeafletMap";
  import {FETCH_ALL_PEOPLE} from "../../../store/actions.type";
  import MapControls from "./MapControls";
  import ConditionModel from "../../../common/ConditionModel";

  export default {
    name: "MapPage",
    components: {MapControls, LeafletMap},
    data() {
      return {
        people: [],
        fPeople: [],
        loaded: false,
      }
    },
    computed: {
      mapSettings() {
        return this.$store.getters.mapSettings;
      }
    },
    watch: {
      mapSettings: {
        deep: true,
        handler(newVal, oldVal) {
          this.filterPeople();
        }
      }
    },
    methods: {
      filterPeople() {
        let cm = new ConditionModel();

        if (!this.mapSettings.checked.includes("dead"))
          cm.addCondition("is_dead", false);

        console.log(this.fPeople.length);
        this.fPeople = this.people.filter(p => {
          cm.evalutate(p);
        });

        console.log(this.fPeople.length);
      }
    },
    created() {
      if (this.$store.getters.allPeopleFetched) {
        this.people = this.$store.getters.people;
        this.fPeople = this.people;
        this.loaded = true;
      } else {
        this.$store.dispatch(FETCH_ALL_PEOPLE)
          .then(data => {
            this.people = data;
            this.fPeople = data;
            this.loaded = true;
          });
      }
    }
  }
</script>

<style scoped>

  /*Important import to make the leaflet map work*/
  @import "../../../../node_modules/leaflet/dist/leaflet.css";

  #leaflet-map {
    position: fixed;
    align-self: center;
    left: 5%;
    width: 90%;
    height: 70%;
  }


</style>
