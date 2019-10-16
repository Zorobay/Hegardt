<template>
  <b-col>
    <b-row>
      <b-form @submit="onSubmit" inline>
        <b-form-input
          @input="searchCallback()"
          @blur="exit()"
          id="globalSearchBar"
          placeholder="Sök"
          required
          v-model="search"
        ></b-form-input>
        <b-button type="submit" variant="primary">Search</b-button>
      </b-form>
    </b-row>
    <b-row>
      <div class="search-results" role="menu" v-if="showDropdown">
        <div class="search-item" v-for="(res, i) in results"
             @mousedown="resultClicked(res)"
             :key="i">
          {{res.full_name}}</div>
      </div>
    </b-row>
  </b-col>

</template>

<script>
  import axios from "axios";
  const API_URL = "http://localhost:3000/person/search/";

  export default {
    name: "SearchForm",
    data() {
      return {
        search: "",
        results: [],
        showDropdown: true
      }
    },
    methods: {
      resultClicked(res) {
        this.search = res.full_name;
        this.$router.push({path: "/person/id/" + res._id});
      },
      searchCallback() {
        this.showDropdown = true;
        if (this.search.length > 0) {
          if (this.$store.getters.allPeopleFetched) {

          }
          axios(API_URL + this.search)
            .then(res => this.results = res)
            .catch(err => {
              console.error(err);
              this.results = []
            })
        } else {
          this.results = [];
        }
      },
      onSubmit(evt) {
        evt.preventDefault();  // Prevents reloading the page
      },
      exit() {
        this.showDropdown = false;
      }
    }
  }
</script>

<style scoped>

  #globalSearchBar{
    min-width: 250px;
  }
  .search-results{
    position:absolute;
    z-index: 1;
    background-color: #ffffff;
    border: 1px solid #bbbbbb;
    min-width: 250px;
    max-width: 250px;
  }

  .search-item:hover{
    background-color: #dddddd;
    cursor:pointer;
  }

</style>
