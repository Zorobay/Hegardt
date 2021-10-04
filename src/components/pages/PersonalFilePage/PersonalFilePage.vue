<template>
  <div v-if="this.person" class="personal-file-page">
    <img src="icons/blank-avatar.svg" width="20%"/>

<!--    <collapsible-text :text="person" id-prefix="person-json"/>-->
    <h1>
      {{ this.person.fullName }}
      <font-awesome-icon v-if="person.sex !== 'UNKNOWN'" :icon="person.sex === 'MAN' ? 'mars' : 'venus'" size="lg"/>
    </h1>

    <p>{{elvis(person, 'notes')}}</p>
    <div>
      <personal-info-table
        :person="person"
      />
    </div>

    <h3>Family Tree</h3>
    <close-family-tree2
          :person="person"
          :mother="mother"
          :father="father"
          :siblings="siblings"
          :children="children"
          :spouses="spouses"
          :marriages="marriages"
        />

  </div>
</template>

<script>
  import {FETCH_COMPLETE_PERSON_BY_ID} from '@/store/actions.type';
  import CollapsibleText from '@/components/common/CollapsibleText';
  import PersonalInfoTable from '@/components/pages/PersonalFilePage/PersonalInfoTable/PersonalInfoTable';
  import CloseFamilyTree2 from '@/components/pages/PersonalFilePage/FamilyTree/CloseFamilyTree2';

  export default {
    name: 'PersonalFilePage',
    components: {PersonalInfoTable, CollapsibleText, CloseFamilyTree2},
    data() {
      return {
        person: null,
        father: null,
        mother: null,
        siblings: [],
        children: [],
        spouses: [],
      };
    },
    computed: {
      marriages() {
        return this.person.marriages;
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
        })
        .catch(err => {
          console.log(err);
          this.$router.replace({name: 'MissingPage'});
        });
    },
  };
</script>

<style scoped>

</style>
