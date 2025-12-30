<script setup lang="ts">
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

const props = defineProps({ id: { type: Number, required: true } });
</script>

<template>
  <div class="d-flex flex-row gap-1">
    <router-link class="icon-link" :to="{ name: 'tree', params: { personId: id } }">
      <font-awesome-icon icon="sitemap"></font-awesome-icon>
    </router-link>
    <router-link class="icon-link" :to="{ name: 'person', params: { id: id } }">
      <font-awesome-icon icon="user"></font-awesome-icon>
    </router-link>
  </div>
</template>

<style scoped></style>
