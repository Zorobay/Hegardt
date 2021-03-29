<template>

  <div v-if="this.person">
    <b-avatar size="200px">

    </b-avatar>
    <collapsible-text :text="person" id-prefix="person-json"/>

    <h1>
      {{ this.person.full_name }}
      <font-awesome-icon v-if="person.sex !== 'UNKNOWN'" :icon="person.sex === 'MAN' ? 'mars' : 'venus'" size="lg"/>
    </h1>
    <b-row>
      <b-col cols="5">
        <info-side-bar :person="this.person"/>
      </b-col>
      <b-col cols="7">
        <close-family-tree2
          :person="person"
          :mother="mother"
          :father="father"
          :children="children"
          :spouses="spouses"
          :marriages="marriages"
        />
      </b-col>
    </b-row>

  </div>
</template>

<script>
  import {FETCH_COMPLETE_PERSON_BY_ID} from '@/store/actions.type';
  import JSONPerson from '@/common/JSONPerson';
  import InfoSideBar from '@/components/pages/PersonalFilePage/InfoSideBar/InfoSideBar';
  import CollapsibleText from '@/components/common/CollapsibleText';
  import CloseFamilyTree2 from '@/components/pages/PersonalFilePage/FamilyTree/CloseFamilyTree2';

  export default {
    name: 'PersonalFilePage',
    components: {CollapsibleText, InfoSideBar, CloseFamilyTree2},
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
    computed: {
      marriages() {
        return this.person.spouses;
      },
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
