<template>
  <i v-if="sex" :class="iconClass"></i>
</template>

<script setup lang="ts">
import PersonSexEnum from "@/enums/PersonSexEnum.ts";
const props = defineProps({sex: {type: String, required: true}});
function sexIconClass(sex: string) {
  if (sex.toUpperCase() === PersonSexEnum.MAN) {
    return 'fa-solid fa-mars';
  } else if (sex.toUpperCase() === PersonSexEnum.WOMAN) {
    return 'fa-solid fa-venus';
  } else {
    return '';
  }
}

const iconClass = sexIconClass(props.sex);

</script>

<style scoped>

</style>
