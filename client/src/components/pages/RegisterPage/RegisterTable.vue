<template>
  <div class="overflow-auto">
    <b-pagination
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
    ></b-pagination>
    <b-table striped hover small head-variant="dark"
             :per-page="perPage"
             :current-page="currentPage"
             id="registerTable"
             :items="items"
             :fields="fields">

      <!-- A custom formatted column -->
      <template v-slot:cell(link)="data">
        <router-link v-bind:to="{name: 'PersonalFile', params: {id: data.item._id}}">GO
        </router-link>
      </template>
    </b-table>
  </div>
</template>

<script>

  export default {
    name: "RegisterTable",
    props: ["items"],
    data() {
      return {
        currentPage: 1,
        perPage: 50,
        fields: [
          "link",
          {
            key: "first_name",
            sortable: true,
          },
          {
            key: "last_name",
            sortable: true
          },
          {
            key: "birth_date",
            sortable: true,
            formatter: "formatDate"
          },
          {key: "death_date", sortable: true, formatter: "formatDate"},
          {key: "occupation", sortable: true, formatter: "formatOccupations"}]
      }
    },
    methods: {
      getIdURL: function (id) {
        return "#/person/id/" + id;
      }
    },
    computed: {
      rows() {
        return this.items.length;
      }
    }
  }
</script>

<style scoped>

</style>
