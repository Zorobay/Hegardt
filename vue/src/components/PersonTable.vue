<script setup lang="ts">
import DataTable from 'datatables.net-vue3';
import DataTablesCore from 'datatables.net-dt';
import { formatPersonDate } from '@/helpers/person-helper.ts';
import type { LifeEvent, PersonSummary } from '@/types/person.type.ts';
import { personsApiService } from '@/api/personsApiService.ts';
import { onMounted, ref } from 'vue';
import LoadingContainer from '@/components/async/LoadingContainer.vue';

const data = ref<PersonSummary[]>([]);
const loading = ref(true);

DataTable.use(DataTablesCore);

onMounted(async () => {
  try {
    const res = await personsApiService.getAll();
    data.value = res.data ?? [];
  } finally {
    loading.value = false;
  }
});

const columns = [
  {
    data: 'firstName',
    title: 'First Name',
  },
  {
    data: 'middleNames',
    title: 'Middle Names',
    render: function (data: string) {
      return data ?? '';
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
      if (!data) return '';
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
  <LoadingContainer :is-loading="loading" message="Fetching...">
    <DataTable id="persons-table" :data="data" :columns="columns" class="display table table-striped" />
  </LoadingContainer>
</template>

<style scoped>
@import url('datatables.net-dt');
</style>
