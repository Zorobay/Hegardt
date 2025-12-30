<script setup lang="ts">
import FamilyTreeComponent from '@/components/tree/FamilyTreeComponent.vue';
import SearchComponent from '@/components/forms/SearchComponent.vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { useRouter } from 'vue-router';

const props = defineProps({ personId: { type: Number, required: true } });

const router = useRouter();

function onSearchedPersonClicked(personId: number): void {
  router.push({
    name: 'tree',
    params: { personId: personId },
  });
}
</script>

<template>
  <h1>Tree</h1>
  <div style="display: flex; flex-direction: row; gap: 1rem; align-items: flex-start">
    <SearchComponent :default-id="personId" @on-person-clicked="onSearchedPersonClicked" />
    <button class="btn btn-primary"><font-awesome-icon icon="fa-solid fa-arrows-to-circle" />Center</button>
  </div>
  <FamilyTreeComponent :person-id="personId" />
</template>
<style scoped>
.heg-search-component {
  margin-bottom: 0.5rem;
  width: 40%;
}
</style>
