<script setup lang="ts">
import DataTable from 'datatables.net-vue3';
import DataTablesCore from 'datatables.net-dt';
import personService from '@/services/PersonService.ts';
import { formatPersonDate } from '@/helpers/person-helper.ts';
import type { LifeEvent } from '@/types/person.type.ts';

DataTable.use(DataTablesCore);

const data = personService.getAllPersonsList();
const columns = [
  {
    data: 'firstName',
    title: 'First Name',
  },
  {
    data: 'middleNames',
    title: 'Middle Names',
    render: function (data: string[], _type: string, _row: unknown, _meta: object) {
      return data ? data.join(' ') : '';
    },
  },
  {
    data: 'lastName',
    title: 'Last Name',
  },
  {
    data: 'birth',
    title: 'Birth date',
    render: function (data: LifeEvent, _type: string, _row: unknown, _meta: object) {
      return formatPersonDate(data.date);
    },
  },
  {
    data: 'id',
    title: 'Link',
    render: function (data: string, _type: string, _row: unknown, _meta: object) {
      return `<a href="/person/${data}">Details</a>`;
    },
  },
];
</script>

<template>
  <DataTable id="persons-table" :data="data" :columns="columns" class="display table table-striped"> </DataTable>
</template>

<style scoped>
@import 'datatables.net-dt';
</style>
