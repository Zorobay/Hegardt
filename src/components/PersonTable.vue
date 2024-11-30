<script setup>
import DataTable from 'datatables.net-vue3';
import DataTablesCore from 'datatables.net-bs5';
import personService from "@/services/PersonService.js";
import {formatPersonDate} from "@/helpers/person-helper.js";

DataTable.use(DataTablesCore);

const data = personService.getAllPersonsList()
const columns = [
  {
    data: 'firstName', title: 'First Name'
  },
  {
    data: 'middleNames', title: 'Middle Names',
    render: function (data, type, row, meta) {
      return data ? data.join(' ') : '';
    }
  },
  {
    data: 'lastName', title: 'Last Name'
  },
  {
    data: 'birth', title: 'Birth date',
    render: function (data, type, row, meta) {
        return formatPersonDate(data.date);
    }
  },
  {
    data: 'id', title: 'Link',
    render: function (data, type, row, meta) {
      return `<a href="/person/${data}">Details</a>`
    }
  }
]
</script>

<template>
  <DataTable :data="data" :columns="columns" id="persons-table" class="display table table-striped">
  </DataTable>
</template>

<style scoped>
@import 'datatables.net-dt';

</style>
