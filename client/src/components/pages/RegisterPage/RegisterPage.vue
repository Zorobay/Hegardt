<template>
  <div>
    <h1>Personregister</h1>
    <register-table
      v-bind:items="people">
    </register-table>
  </div>
</template>

<script>
  import RegisterTable from "./RegisterTable";
  import {FETCH_ALL_PEOPLE} from "../../../store/actions.type";
  import { mapGetters } from "vuex";

  export default {
    name: "RegisterPage",
    components: {RegisterTable},
    data: () => ({
      persons: [],
      headings: ["First Name", "Last Name"]
    }),
    computed: {
        people() {
          return this.$store.getters.people;
        },
        ...mapGetters(["allPeopleFetched"])
    },
    created() {
      if (!this.$store.getters.allPeopleFetched) {
        this.$store.dispatch(FETCH_ALL_PEOPLE)
        .then(res => {
          this.persons = res;
        });
      } else {
        this.persons = this.$store.getters.people;
      }

    }
  }
</script>

<style scoped>

</style>
