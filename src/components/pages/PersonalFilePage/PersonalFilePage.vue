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
          <name-link :person="father"></name-link>
        </b-col>
        <b-col>
          <h4>Moder</h4>
          <name-link :person="mother"/>
        </b-col>
      </b-row>
    </b-container>

    <h4 v-if="siblings.length > 0">Syskon</h4>
    <ul class="person-list">
      <li v-for="sib in siblings" :key="sib.id">
        <name-link :person="sib"></name-link>
      </li>
    </ul>

    <h4 v-if="children.length > 0">Barn</h4>
    <ul class="person-list">
      <li v-for="child in children" :key="child.id">
        <name-link :person="child"></name-link>
      </li>
    </ul>
    <h4>Anteckningar</h4>
    <p>{{person.notes}}</p>

  </div>
</template>

<script>
  import WellCell from './WellCell';
  import {FETCH_PERSON_BY_ID} from '../../../store/actions.type';
  import NameLink from '../../person/NameLink';

  export default {
    name: 'PersonalFilePage',
    components: {NameLink, WellCell},
    data() {
      return {
        person: null,
        father: null,
        mother: null,
        siblings: [],
        children: [],
      };
    },
    created() {
      const id = this.$route.params.id;
      this.$store.dispatch(FETCH_PERSON_BY_ID, id)
        .then(data => {
          this.person = data;

          if (this.person.father) {
            this.$store.dispatch(FETCH_PERSON_BY_ID, this.person.father)
              .then(data => {
                this.father = data;
                if (this.person.mother) {
                  this.$store.dispatch(FETCH_PERSON_BY_ID, this.person.mother)
                    .then(data => {
                      this.mother = data;
                    });
                }
              });
          }

          for (const child of this.person.children) {
            this.$store.dispatch(FETCH_PERSON_BY_ID, child)
              .then(data => {
                this.children.push(data);
              })
              .catch(err => console.log(err));
          }

          for (const sib of this.person.siblings) {
            this.$store.dispatch(FETCH_PERSON_BY_ID, sib)
              .then(data => {
                this.siblings.push(data);
              })
              .catch(err => console.log(err));
          }
        })
        .catch(err => {
          console.log(err);
          this.$router.replace({name: 'MissingPage'});
        });
    },
  };
</script>

<style scoped>

  .person-list {
    list-style-type: none;
  }

</style>
