<template>
  <div>
    <h2>{{this.person.full_name}}</h2>
    <h4>Ansedel</h4>

    <p>Född {{this.person.age}} år sedan</p>
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

    <h4>Fader</h4>
    <p>{{person.father}}</p>
  </div>
</template>

<script>
  import WellCell from "./WellCell";

  export default {
    name: "PersonalFile",
    components: {WellCell},
    data: function () {
      return {
        person: {},
      }
    },
    methods: {
      findPersonById: async function (id) {
      const API_URL = "http://localhost:3000/person/id/";

      await fetch(API_URL + id)
        .then(res => {
          return res.json();
        })
        .then(res => {
          if (res.status >= 400) {
            this.$router.push({name: "MissingPage"});
          } else {
            this.person = res;
          }
        });
    }
    },
    mounted() {
      const id = this.$route.params.id;
      this.findPersonById(id);
    }
  }
</script>

<style scoped>

</style>
