<template>

  <div v-if="this.person">
    <b-avatar size="200px">

    </b-avatar>
    <p>{{ person }}</p>

    <h1>
      {{ this.person.full_name }}
      <font-awesome-icon v-if="person.sex !== 'UNKNOWN'" :icon="person.sex === 'MAN' ? 'mars' : 'venus'" size="lg"/>
    </h1>
    <b-row>
      <b-col cols="4">
        <info-side-bar :person="this.person"/>
      </b-col>
      <b-col cols="7">
        <close-family-tree
          :person="json_person"
        />
      </b-col>
    </b-row>

  </div>
</template>

<script>
  import {FETCH_COMPLETE_PERSON_BY_ID} from '@/store/actions.type';
  import CloseFamilyTree from '@/components/pages/PersonalFilePage/CloseFamilyTree';
  import JSONPerson from '@/common/JSONPerson';
  import InfoSideBar from '@/components/pages/PersonalFilePage/InfoSideBar/InfoSideBar';

  export default {
    name: 'PersonalFilePage',
    components: {InfoSideBar, CloseFamilyTree},
    data() {
      return {
        person: null,
        json_person: null,
        father: null,
        mother: null,
        siblings: [],
        children: [],
        spouses: [],
      };
    },
    created() {
      const id = this.$route.params.id;
      this.$store.dispatch(FETCH_COMPLETE_PERSON_BY_ID, id)
        .then(data => {
          this.person = data.person;
          this.father = data.father;
          this.mother = data.mother;
          this.children = data.children;
          this.siblings = data.siblings;
          this.spouses = data.spouses;
          this.setJsonPerson();
        })
        //   this.person_json.setPerson(data);
        //
        //   if (this.person.father) {
        //     this.$store.dispatch(FETCH_PERSON_BY_ID, this.person.father)
        //       .then(data => {
        //         this.father = data;
        //         this.person_json.father = this.toJson(data);
        //
        //         if (this.person.mother) {
        //           this.$store.dispatch(FETCH_PERSON_BY_ID, this.person.mother)
        //             .then(data => {
        //               this.mother = data;
        //               this.person_json.mother = this.toJson(data);
        //             });
        //         }
        //       });
        //   }
        //
        //   for (const child of this.person.children) {
        //     this.$store.dispatch(FETCH_PERSON_BY_ID, child)
        //       .then(data => {
        //         this.children.push(data);
        //         this.person_json.children.push(data);
        //       })
        //       .catch(err => console.log(err));
        //   }
        //
        //   for (const sib of this.person.siblings) {
        //     this.$store.dispatch(FETCH_PERSON_BY_ID, sib)
        //       .then(data => {
        //         this.siblings.push(data);
        //         this.person_json.siblings.push(data);
        //       })
        //       .catch(err => console.log(err));
        //   }
        // })
        .catch(err => {
          console.log(err);
          this.$router.replace({name: 'MissingPage'});
        });
    },
    methods: {
      setJsonPerson() {
        this.json_person = new JSONPerson(this.person);
        this.json_person.setMother(this.mother);
        this.json_person.setFather(this.father);
      },
    },
  };
</script>

<style scoped>

</style>
