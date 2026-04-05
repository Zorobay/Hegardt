<script setup lang="ts">
import { onMounted, ref } from 'vue';
import AccordionComponent from '@/components/forms/AccordionComponent.vue';
import CheckboxComponent from '@/components/forms/CheckboxComponent.vue';

const props = defineProps({
  heading: { type: String, default: '' },
  items: { type: Array<string>, default: [] },
  value: { type: String, required: true },
});
const emit = defineEmits(['selection-changed']);
const checkedStates = ref<Record<string, boolean>>(Object.fromEntries(props.items.map((item) => [item, true])));

function onCheckboxChange(label: string, checked: boolean): void {
  checkedStates.value[label] = checked;
  emit('selection-changed', getSelectedItems());
}

function getSelectedItems(): string[] {
  const items = props.items;
  return items.filter((item) => checkedStates.value[item]);
}

onMounted(() => {
  emit('selection-changed', getSelectedItems());
});
</script>

<template>
  <AccordionComponent :heading="heading" :value="value">
    <CheckboxComponent
      v-for="item in items"
      :key="item"
      :label="item"
      :checked="checkedStates[item]"
      @selection-changed="
        (checked) => {
          onCheckboxChange(item, checked);
        }
      "
    />
  </AccordionComponent>
</template>

<style scoped></style>
