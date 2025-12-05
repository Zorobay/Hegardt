<template>
  <Accordion :heading="heading">
    <Checkbox v-for="item in items" :key="item" :label="item" :checked="checkedStates[item]" @change="onCheckboxChange"/>
  </Accordion>
</template>


<script setup>
import { onMounted, reactive} from 'vue';
import Accordion from '@/components/forms/Accordion.vue'
import Checkbox from '@/components/forms/Checkbox.vue'

const props = defineProps(['heading', 'items']);
const emit = defineEmits(['selection-changed']);
const checkedStates = reactive({});

function onCheckboxChange(e) {
  const target = e.target;
  checkedStates[target.value] = target.checked;
  emit('selection-changed', getSelectedItems());
}

function getSelectedItems() {
  const items = props.items;
  const out = [];
  items.forEach(item => {
    if (checkedStates[item]) {
      out.push(item);
    }
  })
  return out;
}

onMounted(() => {
  props.items.forEach(i => {
    checkedStates[i] = true;
  })

  emit('selection-changed', getSelectedItems());
})
</script>

<style scoped>

</style>
