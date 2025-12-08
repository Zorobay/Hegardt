<template>
  <label class="d-flex gap-2 align-items-center" :for="label">
    <input
      :id="label"
      type="checkbox"
      :value="label"
      :checked="checked"
      @change="(event) => $emit('selection-changed', (event.target as HTMLInputElement)?.checked)"
    />
    {{ label }}
  </label>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';

const props = defineProps(['label', 'checked']);
const emit = defineEmits(['selection-changed']);

onMounted(() => {
  if (props.checked) {
    emit('selection-changed', props.checked.value);
  }
});
</script>

<style scoped></style>
