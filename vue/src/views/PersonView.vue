<script setup lang="ts">
import { onMounted, ref } from 'vue';
import ReadonlyText from '@/components/person/PersonTextProperty.vue';
import PortraitComponent from '@/components/person/PortraitComponent.vue';
import { formatPersonAge, formatPersonFullName } from '@/helpers/person-helper.ts';
import SexIcon from '@/components/person/SexIcon.vue';
import InfoGroup from '@/components/person/InfoGroup.vue';
import PersonCard from '@/components/person/PersonCard.vue';
import PersonLifeEvent from '@/components/person/PersonLifeEvent.vue';
import { filterNullOrUndefined } from '@/helpers/util-helper.ts';
import PersonNotes from '@/components/person/PersonNotes.vue';
import PersonIconLinks from '@/components/person/PersonCardIconLinks.vue';
import { personsApiService } from '@/api/personsApiService.ts';
import type { EntityId, Person, PersonSummary } from '@/types/person.type.ts';
import LoadingContainer from '@/components/async/LoadingContainer.vue';

const { id } = defineProps<{ id: EntityId }>();
const loading = ref(true);
const person = ref<Person | null>(null);
const parents = ref<PersonSummary[]>([]);

onMounted(async () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });

  try {
    const res = await personsApiService.getCompleteById(id);
    person.value = res.data;
    parents.value = filterNullOrUndefined([person.value.father, person.value.mother]);
  } catch (e) {
    console.error(e);
  } finally {
    loading.value = false;
  }
});
</script>

<template>
  <LoadingContainer :is-loading="loading" message="Fetching...">
    <div class="heg-person-view">
      <div v-if="person">
        <div class="row">
          <div class="col-12 col-lg-2 mb-3 mb-lg-0 text-center text-lg-start">
            <PortraitComponent :id="id" />
          </div>

          <div class="col-9">
            <div class="d-flex flex-row">
              <h2 id="person-full-name">
                {{ formatPersonFullName(person) }}
                <SexIcon :sex="person.sex" />
              </h2>
              <PersonIconLinks :id="id" />
            </div>
            <InfoGroup title="Personal details">
              <div class="row">
                <div class="col">
                  <PersonLifeEvent :event="person.birth" title="Born" />
                </div>
                <div class="col">
                  <ReadonlyText :text="formatPersonAge(person)" title="Age" />
                </div>
              </div>
              <PersonLifeEvent :event="person.death" title="Died" />
              <PersonLifeEvent :event="person.burial" title="Buried" />

              <PersonNotes :notes="person.notes" />

              <ReadonlyText title="Occupations">
                <ul>
                  <li v-for="occupation in person.occupations" :key="occupation.id">{{ occupation }}</li>
                </ul>
              </ReadonlyText>
            </InfoGroup>

            <InfoGroup title="Parents">
              <PersonCard v-for="parent in parents" :key="parent.id" :person="parent" />
            </InfoGroup>

            <InfoGroup title="Siblings">
              <PersonCard v-for="sibling in person.siblings" :key="sibling.id" :person="sibling" />
            </InfoGroup>

            <InfoGroup title="Children">
              <PersonCard v-for="child in person.children" :key="child.id" :person="child" />
            </InfoGroup>
          </div>
        </div>
      </div>
    </div>
  </LoadingContainer>
</template>

<style scoped>
.heg-portrait {
  width: 100%;
}

.heg-person-view {
  margin-top: 5em;
  margin-bottom: 5em;

  .row {
    display: flex;
    justify-content: center;
  }
}

#person-full-name {
  display: inline-block;
}

.heg-info-group {
  .heg-person-card {
    width: 100%;
  }
}
</style>
