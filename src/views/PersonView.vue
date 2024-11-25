<template>
  <div class="heg-person-view">
    <div class="row">
      <div class="col-2">
        <ProfilePicture/>
      </div>

      <div class="col-9">
        <h3>{{formatFullName(person.firstName, person.middleNames, person.lastName)}}</h3>
        <ReadonlyText :text="person.firstName" title="First Name"/>
      </div>
    </div>
    <p>Person ID: {{person.id}}</p>
    <p>First Name: {{person.firstName}}</p>
    <p>Middle Names: {{person.middleNames}}</p>
    <p>Last Name: {{person.lastName}}</p>
  </div>
</template>

<script setup>
import personService from "@/services/PersonService.js";
import {useRoute} from 'vue-router';
import ReadonlyText from "@/components/forms/ReadonlyText.vue";
import ProfilePicture from "@/components/person/ProfilePicture.vue";

const route = useRoute();
const id = route.params.id;
const person = personService.getPersonById(id);
</script>

<style scoped>
.heg-person-view {
  margin-top: 5em;
}
</style>
