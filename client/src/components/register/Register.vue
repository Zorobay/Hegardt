<template>
  <div>
    <h1>Personregister</h1>
    <register-table
      v-bind:items="persons">
    </register-table>
  </div>
</template>

<script>
  import RegisterTable from "./RegisterTable";

  const API_URL = "http://localhost:3000/person/all";

  export default {
    name: "Register",
    components: {RegisterTable},
    data: () => ({
      persons: [],
      headings: ["First Name", "Last Name"]
    }),
    mounted() {
      fetch(API_URL)
        .then(res => res.json())
        .then(res => this.persons = res);
    }
  }
</script>

<style scoped>

</style>
