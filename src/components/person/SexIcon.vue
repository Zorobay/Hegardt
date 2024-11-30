<template>
  <i v-if="sex" :class="iconClass"></i>
</template>

<script setup>
import PersonSexEnum from "@/enums/PersonSexEnum.js";
const props = defineProps(['sex']);
function sexIconClass(sex) {
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
