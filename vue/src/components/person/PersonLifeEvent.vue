<script setup lang="ts">
import ReadonlyText from '@/components/person/PersonTextProperty.vue';
import { formatPersonDate, formatPersonLocation } from '@/helpers/person-helper.ts';
import type { LifeEvent } from '@/types/person.type.ts';

interface Props {
  event: LifeEvent;
  title: string;
}
const props = defineProps<Props>();
const event = props.event;
const date = formatPersonDate(event.date);
const location = formatPersonLocation(event.location);
const text = getText(date, location);
function getText(date: string, location: string): string {
  if (date) {
    return `${date}${location ? ` in ${location}` : ''}`;
  }
  return '';
}
</script>

<template>
  <ReadonlyText :text="text" :title="props.title" />
</template>

<style scoped></style>
