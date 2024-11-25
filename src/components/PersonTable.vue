<script setup>
import DataTable from 'datatables.net-vue3';
import DataTablesCore from 'datatables.net-bs5';
import personService from "@/services/PersonService.js";

DataTable.use(DataTablesCore);

const data = personService.getAllPersonsList()
const columns = [
  {data: 'firstName', title: 'FirstName'},
  {data: 'lastName', title: 'LastName'},
  {data: 'id', title: 'Link', render: function(data, type, row, meta) {
      return `<a href="/person/${data}">Details</a>`
    }}
]
</script>

<template>
    <DataTable :data="data" :columns="columns" class="display table table-striped">
    </DataTable>
</template>

<style scoped>
@import 'datatables.net-dt';

</style>
