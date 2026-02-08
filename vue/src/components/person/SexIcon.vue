<script setup lang="ts">
import SexEnum from '@/enums/PersonSexEnum.ts';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

const props = defineProps({ sex: { type: String, required: true } });
function sexIconClass(sex: string): string {
  if (sex.toUpperCase() === SexEnum.MAN) {
    return 'fa-solid fa-mars';
  } else if (sex.toUpperCase() === SexEnum.WOMAN) {
    return 'fa-solid fa-venus';
  } else {
    return '';
  }
}

const iconClass = sexIconClass(props.sex);
</script>

<template>
  <font-awesome-icon :icon="iconClass" />
</template>

<style scoped></style>
