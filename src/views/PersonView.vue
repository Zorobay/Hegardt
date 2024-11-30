<template>
  <div class="heg-person-view">
    <div class="row">
      <div class="col-2">
        <ProfilePicture/>
      </div>
      <div class="col-9">
        <h3 id="person-full-name">{{ formatPersonFullName(person) }}
          <SexIcon :sex="person.sex"/>
        </h3>
        <div class="row">
          <div class="col">
            <PersonLifeEvent :event="person.birth" title="Born"/>
          </div>
          <div class="col">
            <ReadonlyText :text="formatPersonAge(person)" title="Age"/>
          </div>
        </div>
        <PersonLifeEvent :event="person.death" title="Died"/>
        <PersonLifeEvent :event="person.burial" title="Buried"/>

        <PersonNotes :notes="person.notes"/>

        <ReadonlyText title="Occupations">
          <ul>
            <li v-for="occupation in person.occupations">{{occupation}}</li>
          </ul>
        </ReadonlyText>

        <ReadonlyText title="References">
          <ul>
            <li v-for="reference in person.references">{{reference}}</li>
          </ul>
        </ReadonlyText>

        <InfoGroup title="Parents">
          <PersonCard v-for="parent in parents" :person="parent"/>
        </InfoGroup>

        <InfoGroup title="Siblings">
          <PersonCard v-for="sibling in siblings" :person="sibling"/>
        </InfoGroup>

        <InfoGroup title="Children">
          <PersonCard v-for="child in children" :person="child"/>
        </InfoGroup>
      </div>
    </div>
  </div>
</template>

<script setup>
import personService from "@/services/PersonService.js";
import {useRoute} from 'vue-router';
import ReadonlyText from "@/components/person/PersonTextProperty.vue";
import ProfilePicture from "@/components/person/ProfilePicture.vue";
import {formatPersonFullName, formatPersonAge, personBirthDate} from '@/helpers/person-helper.js';
import SexIcon from "@/components/person/SexIcon.vue";
import InfoGroup from "@/components/person/InfoGroup.vue";
import PersonCard from "@/components/person/PersonCard.vue";
import PersonLifeEvent from "@/components/person/PersonLifeEvent.vue";
import {filterNullOrUndefined} from "@/helpers/util-helper.js";
import PersonNotes from "@/components/person/PersonNotes.vue";

const route = useRoute();
const id = route.params.id;
const person = personService.getPersonById(id);
const mother = personService.getPersonById(person.mother);
const father = personService.getPersonById(person.father);
const parents = filterNullOrUndefined([mother, father]);
const siblings = personService.getSiblingsOfPersonById(id);
const children = personService.getChilrenOfPersonById(id);
children.sort((a, b) => {
  return personBirthDate(a) - personBirthDate(b)
})
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
