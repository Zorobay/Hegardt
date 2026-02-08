<script setup lang="ts">
import { onMounted } from 'vue';

const props = defineProps({
  label: { type: String, default: '' },
  checked: { type: Boolean, default: false },
});
const emit = defineEmits(['selection-changed']);

onMounted(() => {
  if (props.checked) {
    emit('selection-changed', props.checked);
  }
});
</script>

<template>
  <div class="checkbox-wrapper">
    <CheckboxPrime
      binary
      :input-id="label"
      @change="(event) => $emit('selection-changed', (event.target as HTMLInputElement)?.checked)"
    >
    </CheckboxPrime>
    <label :for="label">
      {{ label }}
    </label>
  </div>
  <!--  <input :id="label" type="checkbox" :value="label" :checked="checked" />-->
</template>

<style scoped>
.checkbox-wrapper {
  display: flex;
  gap: 0.4rem;
  align-items: center;
}
</style>
