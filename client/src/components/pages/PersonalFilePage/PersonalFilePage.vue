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

    <b-container>
      <b-row>
        <b-col>
          <h4>Fader</h4>
          <h5 v-if="person.father"><a v-bind:href="getPersonURL(father)">{{father.full_name}}</a></h5>
          <h5 v-else>?</h5>
        </b-col>
        <b-col>
          <h4>Moder</h4>
          <h5 v-if="person.mother"><a v-bind:href="getPersonURL(mother)">{{mother.full_name}}</a></h5>
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

              // Success! Get father!
              if (this.person.father) {
                fetch(API_URL + this.person.father)
                  .then(res => res.json())
                  .then(res => {
                    this.father = res;
                  });
              }

              if (this.person.mother) {
                fetch(API_URL + this.person.mother)
                  .then(res => res.json())
                  .then(res => {
                    this.mother = res;
                  });
              }
            }
          });
      },
      getPersonURL(person) {
        if (person) {
          let id = person._id;
          return "#/person/id/" + id;
        }
      }
    },
    created() {
      const id = this.$route.params.id;
      this.findPersonById(id);
    }
  }
</script>

<style scoped>

</style>
