<script setup lang="ts">
import { onMounted, ref } from 'vue';

const props = defineProps({
  label: { type: String, default: '' },
  checked: { type: Boolean, default: false },
});
const emit = defineEmits<{
  'selection-changed': [selected: boolean];
}>();
const isChecked = ref(false);

onMounted(() => {
  isChecked.value = props.checked;
  if (isChecked.value) {
    emit('selection-changed', isChecked.value);
  }
});

function onChange(): void {
  emit('selection-changed', isChecked.value);
}
</script>

<template>
  <div class="checkbox-wrapper">
    <CheckboxPrime v-model="isChecked" binary :input-id="label" :value="label" @change="onChange"> </CheckboxPrime>
    <label :for="label"> {{ label }} - {{ isChecked }} </label>
  </div>
</template>

<style scoped>
.checkbox-wrapper {
  display: flex;
  gap: 0.4rem;
  align-items: center;
}
</style>
