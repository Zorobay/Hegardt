<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';

interface Props {
  label: string;
  options: string[];
  selected?: string[];
  placeholder?: string;
  multiselect?: boolean;
}

const props = defineProps<Props>();
const emit = defineEmits(['selection-change']);
let checkboxesDisplayStyle = ref('none');
let selected = ref<string[]>(props.selected ?? []);

const placeholderTextComp = computed(() => {
  console.log('recomputed');
  if (selected.value) {
    return selected.value.join(', ');
  }
  return props.placeholder;
});

function onMultiselectClick(): void {
  checkboxesDisplayStyle.value = checkboxesDisplayStyle.value === 'none' ? 'block' : 'none';
}

function onFocusLost(): void {
  checkboxesDisplayStyle.value = 'none';
}

function onCheckboxChange(e: Event): void {
  const target = e.target as HTMLInputElement;
  if (target.checked) {
    selected.value.push(target.value);
  } else {
    selected.value = selected.value.filter((s) => s !== target.value);
  }

  emit('selection-change', selected.value);
}

onMounted(() => {
  if (props.selected) {
    emit('selection-change', selected.value);
  }
});
</script>

<template>
  <div v-if="multiselect" class="input-group">
    <span class="input-group-text">{{ label }}</span>

    <div class="multiselect" tabindex="0" @click="onMultiselectClick" @focusout="onFocusLost">
      <div class="select-box">
        <select class="form-select">
          <option>{{ placeholderTextComp }}</option>
        </select>
        <div class="over-select"></div>
      </div>
      <div id="checkboxes">
        <label v-for="opt in options" :key="opt" :for="opt">
          <input
            :id="opt"
            type="checkbox"
            :value="opt"
            :checked="selected ? selected.includes(opt) : false"
            @change="onCheckboxChange"
          />{{ opt }}
        </label>
      </div>
    </div>
  </div>
</template>

<style scoped>
.multiselect {
  position: relative;
  flex: 1 1 auto;
  width: 1%;
  min-width: 0;
  overflow: visible;
}

.select-box {
  position: relative;
}

.select-box select {
  width: 100%;
}

.over-select {
  position: absolute;
  inset: 0;
}

#checkboxes {
  display: v-bind(checkboxesDisplayStyle);
  position: absolute;
  width: 100%;
  z-index: 1;
  background: var(--bs-white);
  border: 1px #dadada solid;
  line-height: 2;
}

#checkboxes input {
  margin-right: 0.5em;
  margin-left: 0.2em;
}

#checkboxes label {
  display: block;
}

#checkboxes label:hover {
  background-color: var(--bs-blue);
  color: white;
}
</style>
