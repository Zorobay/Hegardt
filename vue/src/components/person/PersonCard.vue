<script setup lang="ts">
import SexIcon from '@/components/person/SexIcon.vue';

import { formatPersonDate, formatPersonFullName } from '@/helpers/person-helper.ts';
import type { Person } from '@/types/person.type.ts';

const props = defineProps<{ person: Person }>();
const id = props.person.id;
</script>

<template>
  <div class="card heg-person-card">
    <div class="card-body">
      <h5 class="card-title">
        {{ formatPersonFullName(person) }}
        <SexIcon :sex="person.sex" />
      </h5>
      <h6 class="card-subtitle mb-2 text-body-secondary">
        {{ formatPersonDate(person.birth.date) }}
      </h6>
      <router-link
        class="stretched-link"
        :to="{ name: 'person', params: { id: id } }"
      ></router-link>
    </div>
  </div>
</template>

<style scoped>
.heg-person-card {
  display: inline-block;
  margin: 0.2em;
}

.heg-person-card:hover {
  background: rgb(0 0 0 / 5%);
}
</style>
