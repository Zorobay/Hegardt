<template>
  <ReadonlyText :text="text" :title="props.title"/>
</template>

<script setup>
import ReadonlyText from "@/components/person/PersonTextProperty.vue";
import {formatPersonDate, formatPersonLocation} from "@/helpers/person-helper.js";

const props = defineProps(['event', 'title']);
const event = props.event;
const date = formatPersonDate(event.date);
const location = formatPersonLocation(event.location);
const text = `${date}${location ? ` in ${location}` : ''}`;
</script>


<style scoped>

</style>
