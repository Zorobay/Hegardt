<template>
  <div>
    <h1>Personregister
      <b-spinner v-if="!loaded"></b-spinner>
    </h1>
    <p>{{people.length}}/1273</p>
    <register-table
      v-bind:items="people">
    </register-table>
  </div>
</template>

<script>
  import {FETCH_ALL_PEOPLE} from '@/store/actions.type';
  import RegisterTable from '@/components/pages/RegisterPage/RegisterTable';

  export default {
    name: 'RegisterPage',
    components: {RegisterTable},
    data: () => ({
      loaded: false,
    }),
    computed: {
      people() {
        return this.$store.getters.people;
      },
    },
    created() {
      if (!this.$store.getters.allPeopleFetched) {
        this.$store.dispatch(FETCH_ALL_PEOPLE)
          .then(res => {
            this.loaded = true;
          });
      } else {
        this.loaded = true;
      }
    },
  };
</script>

<style scoped>

</style>
