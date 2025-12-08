<template>
  <div class="heg-person-view">
    <div v-if="person">
      <div class="row">
        <div class="col-2">
          <ProfilePicture />
        </div>
        <div class="col-9">
          <h3 id="person-full-name">
            {{ formatPersonFullName(person) }}
            <SexIcon :sex="person.sex" />
          </h3>
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
              <li v-for="occupation in person.occupations" :key="occupation">{{ occupation }}</li>
            </ul>
          </ReadonlyText>

          <ReadonlyText title="References">
            <ul>
              <li v-for="reference in person.references" :key="reference">{{ reference }}</li>
            </ul>
          </ReadonlyText>

          <InfoGroup title="Parents">
            <PersonCard v-for="parent in parents" :key="parent.id" :person="parent" />
          </InfoGroup>

          <InfoGroup title="Siblings">
            <PersonCard v-for="sibling in siblings" :key="sibling.id" :person="sibling" />
          </InfoGroup>

          <InfoGroup title="Children">
            <PersonCard v-for="child in children" :key="child.id" :person="child" />
          </InfoGroup>
        </div>
      </div>
    </div>
    <div v-else>
      <p>Person with id {{id}} not found!</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import personService from '@/services/PersonService.ts';
import ReadonlyText from '@/components/person/PersonTextProperty.vue';
import ProfilePicture from '@/components/person/ProfilePicture.vue';
import { formatPersonAge, formatPersonFullName, personBirthDate } from '@/helpers/person-helper.ts';
import SexIcon from '@/components/person/SexIcon.vue';
import InfoGroup from '@/components/person/InfoGroup.vue';
import PersonCard from '@/components/person/PersonCard.vue';
import PersonLifeEvent from '@/components/person/PersonLifeEvent.vue';
import { filterNullOrUndefined } from '@/helpers/util-helper.ts';
import PersonNotes from '@/components/person/PersonNotes.vue';

const { id } = defineProps({ id: {type: String, required: true} });
const person = personService.getPersonById(id);
const mother = personService.getPersonById(person?.mother);
const father = personService.getPersonById(person?.father);
const parents = filterNullOrUndefined([mother, father]);
const siblings = personService.getSiblingsOfPersonById(id);
const children = personService.getChilrenOfPersonById(id);
children.sort((a, b) => {
  return (
    (personBirthDate(a) ?? new Date()).getTime() - (personBirthDate(b) ?? new Date()).getTime()
  );
});
</script>

<style scoped>
.heg-person-view {
  margin-top: 5em;
  margin-bottom: 5em;
}

#person-full-name {
  display: inline-block;
}
</style>
