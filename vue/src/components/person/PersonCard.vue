<script setup lang="ts">
import SexIcon from '@/components/person/SexIcon.vue';

import { formatPartialDate, formatPersonFullName } from '@/helpers/person-helper.ts';
import type { Person, PersonSummary } from '@/types/person.type.ts';
import PortraitComponent from '@/components/person/PortraitComponent.vue';

const props = withDefaults(
  defineProps<{ person: Person | PersonSummary; compact?: boolean; customNavigation?: boolean }>(),
  {
    compact: false,
    customNavigation: false,
  },
);
const emit = defineEmits<{ onCardClicked: [person: Person | PersonSummary] }>();
const id = props.person.id;

function onLinkClick(event: MouseEvent): void {
  if (props.customNavigation) {
    event.preventDefault();
    emit('onCardClicked', props.person);
  }
}
</script>

<template>
  <div class="card heg-person-card">
    <PortraitComponent :id="id" />
    <div class="heg-info">
      <h5 :class="{ 'compact-title': compact }">
        {{ formatPersonFullName(person) }}
        <SexIcon :sex="person.sex" />
      </h5>
      <h6 class="card-subtitle mb-2 text-body-secondary">
        {{ formatPartialDate(person.birth.date) }}
      </h6>
      <router-link v-slot="{ href }" custom :to="{ name: 'person', params: { id: id } }">
        <a :href="href" class="stretched-link" @click="onLinkClick"></a>
      </router-link>
    </div>
  </div>
</template>

<style scoped>
.heg-person-card {
  display: flex;
  flex-direction: row;
  align-items: stretch;
  gap: 0.5rem;
  margin: 0.2rem;
  padding: 0.2rem;
}

.heg-info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  flex: 1 1 auto;
  min-width: 0;
}

.heg-person-card:hover {
  background-color: var(--warm-sand);
}

.heg-person-card .heg-person-card:hover {
  background: rgb(0 0 0 / 5%);
}

.compact-title {
  font-size: 1rem;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
</style>
