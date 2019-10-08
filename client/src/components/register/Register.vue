<template>
  <div>
    <div class="ui container">
      <register-table></register-table>
    </div>
    <h1>Personregister</h1>
    <table class="table-striped" id="registerTable" data-page-length="50">
      <thead class="thead-light">
      <tr>
        <th>Ansedel</th>
        <th>Förnamn</th>
        <th>Mellannamn</th>
        <th>Efternamn</th>
        <th>Födelsedatum</th>
        <th>Födelseplats</th>
        <th>Yrke</th>
      </tr>
      </thead>

      <tbody>
      <div v-for="person in persons">
        <tr>
          <td>{{person.first_name}}</td>
        </tr>
      </div>
      </tbody>
    </table>
  </div>
</template>

<script>
  import RegisterTable from "./RegisterTable";
  const API_URL = "http://localhost:3000/person/all";

  export default {
    name: "Register",
    components: {RegisterTable},
    data: () => ({
      persons: []
    }),
    mounted() {
      fetch(API_URL)
        .then(res => res.json())
        .then(res => {
          $(document).ready(function () {
            const registerTable = $('#registerTable').DataTable({

            });

          })
          console.log(res);
          this.persons = res;
        })
    }
  }
</script>

<style scoped>

</style>
