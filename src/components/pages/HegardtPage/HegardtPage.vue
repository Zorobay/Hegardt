<template>
  <div>
    <p>Välkommen till Hegardt.se, ett släktforskningsprojekt startat av
      <router-link :to="{name: 'PersonalFile', params: {id: '?'}}">Peter Hegardt</router-link>
      och fortsatt av
      <router-link :to="{name: 'PersonalFile', params: {id: '000000000000000000000635'}}">
        Sebastian Hegardt
      </router-link>.
    </p>
    <h3>Family Stats</h3>
    <b-table-simple small stacked>
    <b-tbody>
      <b-tr>
        <b-td stacked-heading="Antal personer">{{stats.count}}</b-td>
        <b-td stacked-heading="Storlek (Mb)">{{stats.size / 1024 / 1024}}</b-td>
      </b-tr>
    </b-tbody>
    </b-table-simple>
  </div>
</template>

<script>
  import PeopleService from "../../../common/api.service";

  export default {
    name: "HegardtPage",
    data() {
      return {
        stats: {},
      }
    },
    created() {
      PeopleService.getStats()
        .then(stats => this.stats = stats);
    }
  }
</script>

<style scoped>

</style>
