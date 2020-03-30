<template>
  <b-form inline>
    <b-form-checkbox-group @change="update" v-model="settings.checked">
      <b-form-checkbox value="dead">Show dead</b-form-checkbox>
    </b-form-checkbox-group>
    <b-form-group @update="update" label="Gender">
      <b-form-select :options="settings.gender.options" v-model="settings.gender.selected">
      </b-form-select>
    </b-form-group>
    <b-form-group @update="update" label="Location by">
      <b-form-select :options="settings.location.options"
                     v-model="settings.location.selected"></b-form-select>
    </b-form-group>
  </b-form>
</template>

<script>
  import {CHANGE_MAP_SETTINGS} from '../../../store/actions.type';

  export default {
    name: 'MapControls',
    data() {
      return {
        settings: {
          checked: ['dead'],
          gender: {
            options: ['male', 'female', 'both'],
            selected: 'both',
          },
          location: {
            options: ['Birth Location', 'Death Location', 'Bury Location'],
            selected: 'Birth Location',
          },
        },
      };
    },
    computed: {
      mapSettings() {
        return this.$store.getters.mapSettings;
      },
    },
    methods: {
      update() {
        this.$store.dispatch(CHANGE_MAP_SETTINGS, this.settings);
      },
    },
  };
</script>

<style scoped>

</style>
