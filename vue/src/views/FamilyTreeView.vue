<script setup lang="ts">
import FamilyTreeComponent from '@/components/tree/FamilyTreeComponent.vue';
import SearchComponent from '@/components/forms/SearchComponent.vue';
import { useRouter } from 'vue-router';
import { ref } from 'vue';

const props = defineProps({ personId: { type: String, required: true } });
const familyTreeRef = ref();
const familyTreeDepth = ref(3);

const router = useRouter();

function onSearchedPersonClicked(personId: number): void {
  router.push({
    name: 'tree',
    params: { personId: personId },
  });
}

function onCenterButtonClicked(): void {
  familyTreeRef.value?.center();
}
</script>

<template>
  <h1>Tree</h1>
  <div class="tree-controls">
    <SearchComponent :default-id="Number.parseInt(personId)" @on-person-clicked="onSearchedPersonClicked" />
    <ButtonPrime @click="onCenterButtonClicked">
      <font-awesome-icon icon="fa-solid fa-arrows-to-circle" />
      Center
    </ButtonPrime>
    <InputNumberPrime
      v-model="familyTreeDepth"
      input-id="horizontal-buttons"
      show-buttons
      button-layout="horizontal"
      :step="1"
      :min="1"
      :max="20"
      mode="decimal"
      fluid
    >
      <template #incrementbuttonicon>
        <span class="pi pi-plus" />
      </template>
      <template #decrementbuttonicon>
        <span class="pi pi-minus" />
      </template>
    </InputNumberPrime>
  </div>
  <FamilyTreeComponent ref="familyTreeRef" :person-id="Number.parseInt(personId)" :max-depth="familyTreeDepth" />
</template>
<style scoped>
.tree-controls {
  display: flex;
  flex-direction: row;
  gap: 1rem;
  align-items: flex-start;
}

.heg-search-component {
  margin-bottom: 0.5rem;
  width: 40%;
}
</style>
