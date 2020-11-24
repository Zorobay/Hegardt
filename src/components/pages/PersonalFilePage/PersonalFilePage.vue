<template>

  <div v-if="this.person">
    <b-avatar size="200px">

    </b-avatar>

    <h1>
      {{ this.person.full_name }}
      <font-awesome-icon v-if="person.sex !== 'UNKNOWN'" :icon="person.sex === 'MAN' ? 'mars' : 'venus'" size="lg"/>
    </h1>
    <b-row>
      <b-col cols="4" class="person-info-column">
        <p>Född {{ this.person.age }} år sedan</p>

        <DateLocationProp
          :heading="Lang('ppage.birth.heading')"
          type="birth"
          :date="elvis(person, 'birth.date')"
          :location="elvis(person, 'birth.location')"
          :notes="elvis(person, 'birth.notes')"/>

        <DateLocationProp
          :heading="Lang('ppage.death.heading')"
          type="death"
          :date="elvis(person, 'death.date')"
          :location="elvis(person, 'death.location')"
          :notes="elvis(person, 'death.notes')"
        />

        <DateLocationProp
          :heading="Lang('ppage.burial.heading')"
          type="burial"
          :date="elvis(person, 'burial.date')"
          :location="elvis(person, 'burial.location')"
          :notes="elvis(person, 'burial.notes')"
        />

        <h4>{{ Lang('ppage.note') }}</h4>
        <p>{{ this.person.notes }}</p>
      </b-col>
      <b-col cols="7">
        <h1>HO!</h1>
      </b-col>
    </b-row>

  </div>
</template>

<script>
  import {FETCH_PERSON_BY_ID} from '@/store/actions.type';
  import DateLocationProp from '@/components/pages/PersonalFilePage/DateLocationProp';

  export default {
    name: 'PersonalFilePage',
    components: {DateLocationProp},
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
