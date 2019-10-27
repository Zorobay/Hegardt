<template>
  <div v-if="this.person">
    <h2>{{this.person.full_name}}</h2>
    <h4>Ansedel</h4>

    <p v-if="this.person.age">Född {{this.person.age}} år sedan</p>
    <p v-else>Född ? år sedan</p>
    <div class="row">
      <div class="col-md-4">
        <p class="text-center font-weight-bold">Född</p>
        <WellCell v-bind:date="formatDate(this.person.birth_date)"
                  v-bind:location="formatLocation(this.person.birth_location)"></WellCell>
      </div>
      <div class="col-md-4">
        <p class="text-center font-weight-bold">Död</p>
        <WellCell v-bind:date="formatDate(this.person.death_date)"
                  v-bind:location="formatLocation(this.person.death_location)"></WellCell>

      </div>
      <div class="col-md-4">
        <p class="text-center font-weight-bold">Begravd</p>
        <WellCell v-bind:date="formatDate(person.bury_date)"
                  v-bind:location="formatLocation(this.person.bury_location)"></WellCell>
      </div>
    </div>

    <b-container>
      <b-row>
        <b-col>
          <h4>Fader</h4>
          <h5 v-if="father">
            <router-link
              :to="{name: 'PersonalFile', params: {id: father._id}}">{{father.full_name}}
            </router-link>
          </h5>
          <h5 v-else>?</h5>
        </b-col>
        <b-col>
          <h4>Moder</h4>
          <h5 v-if="mother">
            <router-link
              :to="{name: 'PersonalFile', params: {id: mother._id}}">{{mother.full_name}}
            </router-link>
          </h5>
          <h5 v-else>?</h5>
        </b-col>
      </b-row>
    </b-container>

    <h4>Syskon</h4>
    <ul>
      <li v-for="sib in person.siblings">
        {{sib}}
      </li>
    </ul>

    <h4>Anteckningar</h4>
    <p>{{person.notes}}</p>

  </div>
</template>

<script>
  import WellCell from "./WellCell";
  import {FETCH_PEOPLE_BY_ID} from "../../../store/actions.type";

  export default {
    name: "PersonalFilePage",
    components: {WellCell},
    data: function () {
      return {
        person: {},
        father: {},
        mother: {}
      }
    },
    created() {
      const id = this.$route.params.id;
      this.$store.dispatch(FETCH_PEOPLE_BY_ID, id)
        .then(data => {
          this.person = data;

          if (this.person.father) {
            this.$store.dispatch(FETCH_PEOPLE_BY_ID, this.person.father)
              .then(data => this.father = data)
          }

          if (this.person.mother) {
            this.$store.dispatch(FETCH_PEOPLE_BY_ID, this.person.mother)
              .then(data => this.mother = data);
          }
        })
        .catch(err => this.$router.replace({name: "MissingPage"}));
    }
  }
</script>

<style scoped>

</style>
