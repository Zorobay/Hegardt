<script setup lang="ts">
import type { GpxRoute } from '@/types/gpx-route.type.ts';
import { getLength } from 'ol/sphere';
import { PROJECTION_WEB_MERCATOR } from '@/constants/geo.constants.ts';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import { ref } from 'vue';

const props = defineProps({ data: { type: Array<GpxRoute>, default: [] } });
const emit = defineEmits<{
  'selection-changed': [{ route: GpxRoute; show: boolean }];
}>();

const selected = ref<GpxRoute[]>(props.data);

function onSelectionChange(newSelection: GpxRoute[]): void {
  props.data.forEach((route) => {
    emit('selection-changed', { route, show: newSelection.includes(route) });
  });
}

function getDistance(route: GpxRoute): string {
  const geometry = route.source.getFeatures()[0]?.getGeometry();
  if (geometry) {
    const len = getLength(geometry, { projection: PROJECTION_WEB_MERCATOR });
    return `${(len / 1000).toFixed(2)} km`;
  }
  return '?';
}
</script>

<template>
  <DataTable v-model:selection="selected" :value="data" @update:selection="onSelectionChange">
    <Column selection-mode="multiple" header-style="width: 8%" />
    <Column field="name" header="Name" />
    <Column header="Distance">
      <template #body="{ data: route }">
        {{ getDistance(route) }}
      </template>
    </Column>
    <Column field="description" header="Description">
      <template #body="{ data: route }">
        {{ route.description ?? '' }}
      </template>
    </Column>
  </DataTable>
</template>
