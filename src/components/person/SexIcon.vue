<template>
  <font-awesome-icon :icon="iconClass" />
</template>

<script setup lang="ts">
import PersonSexEnum from '@/enums/PersonSexEnum.ts';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

const props = defineProps({ sex: { type: String, required: true } });
function sexIconClass(sex: string): string {
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

<style scoped></style>
