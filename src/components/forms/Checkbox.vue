<template>
  <label class="d-flex gap-2 align-items-center" :for="label">
    <input type="checkbox" :id="label" :value="label" :checked="checked" @change="(event) => $emit('selection-changed', event.target.checked)"/>
    {{label}}
  </label>
</template>

<script setup>
import {onMounted} from "vue";

const props = defineProps(['label', 'checked']);
const emit = defineEmits(['selection-changed']);

onMounted(() => {
  if (props.checked) {
    emit('selection-change', props.checked.value);
  }
})
</script>

<style scoped>

</style>
