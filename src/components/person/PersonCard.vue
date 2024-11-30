<template>

  <div class="card heg-person-card">
    <div class="card-body">
      <h5 class="card-title">{{ formatPersonFullName(person) }}
          <SexIcon :sex="person.sex"/>
        </h5>
      <h6 class="card-subtitle mb-2 text-body-secondary">{{ formatPersonDate(person.birth.date) }}</h6>
      <router-link class="stretched-link" :to="{name: 'person', params: {id: id}}"></router-link>
    </div>
  </div>
</template>

<script setup>
import SexIcon from "@/components/person/SexIcon.vue";

import {formatPersonFullName, formatPersonDate} from "@/helpers/person-helper.js";

const props = defineProps(['person']);
const id = props.person.id;
</script>

<style scoped>
.heg-person-card {
  display: inline-block;
  margin: 0.2em;
}

.heg-person-card:hover {
  background: linear-gradient(
          rgba(0, 0, 0, 0.1),
          rgba(0, 0, 0, 0.0)
        )
}
</style>
