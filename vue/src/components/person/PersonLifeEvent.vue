<script setup lang="ts">
import ReadonlyText from "@/components/person/PersonTextProperty.vue";
import {formatPersonDate, formatPersonLocation} from "@/helpers/person-helper.ts";

const props = defineProps(['event', 'title']);
const event = props.event;
const date = formatPersonDate(event.date);
const location = formatPersonLocation(event.location);
const text = `${date}${location ? ` in ${location}` : ''}`;
</script>

<template>
  <ReadonlyText :text="text" :title="props.title"/>
</template>


<style scoped>

</style>
