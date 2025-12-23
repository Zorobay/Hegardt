<script setup lang="ts">
import FamilyTreeComponent from '@/components/tree/FamilyTreeComponent.vue';

const { id } = defineProps({ id: { type: String, required: true } });
</script>

<template>
  <h1>Tree</h1>
  <FamilyTreeComponent :id="id"/>
</template>
<style scoped></style>
