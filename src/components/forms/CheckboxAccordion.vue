<template>
  <AccordionComponent :heading="heading">
    <CheckboxComponent
      v-for="item in items"
      :key="item"
      :label="item"
      :checked="checkedStates[item]"
      @change="onCheckboxChange"
    />
  </AccordionComponent>
</template>

<script setup lang="ts">
import { onMounted, reactive } from 'vue';
import AccordionComponent from '@/components/forms/AccordionComponent.vue';
import CheckboxComponent from '@/components/forms/CheckboxComponent.vue';

const props = defineProps({
  heading: { type: String, default: '' },
  items: { type: Array<string>, default: [] },
});
const emit = defineEmits(['selection-changed']);
const checkedStates = reactive<Record<string, boolean>>({});

function onCheckboxChange(e: Event) {
  const target = e.target as HTMLInputElement;
  checkedStates[target.value] = target.checked;
  emit('selection-changed', getSelectedItems());
}

function getSelectedItems() {
  const items = props.items;
  return items.filter((item) => checkedStates[item]);
}

onMounted(() => {
  props.items.forEach((i) => {
    checkedStates[i] = true;
  });

  emit('selection-changed', getSelectedItems());
});
</script>

<style scoped></style>
