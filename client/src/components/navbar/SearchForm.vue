<template>
  <b-col>
    <b-row>
      <b-form @submit="onSubmit" inline>
        <b-form-input
          @blur="exit()"
          @input="searchCallback()"
          id="globalSearchBar"
          placeholder="Sök"
          required
          v-model="query"
        ></b-form-input>
        <b-button type="submit" variant="primary">Search</b-button>
      </b-form>
    </b-row>
    <b-row>
      <div class="search-results" role="menu" v-if="showDropdown">
        <div :key="i" @mousedown="resultClicked(res)"
             class="search-item"
             v-for="(res, i) in results">
          {{res.full_name}}
        </div>
      </div>
    </b-row>
  </b-col>

</template>

<script>
  import {FETCH_PEOPLE_BY_NAME} from "../../store/actions.type";

  const API_URL = "http://localhost:3000/person/search/";

  export default {
    name: "SearchForm",
    data() {
      return {
        query: "",
        results: [],
        showDropdown: true
      }
    },
    methods: {
      resultClicked(res) {
        this.query = res.full_name;
        this.$router.push({name: "PersonalFile", params: {id: res._id}});
      },
      searchCallback() {
        this.showDropdown = true;
        if (this.query.length > 0) {
          this.$store.dispatch(FETCH_PEOPLE_BY_NAME, this.query)
            .then(data => {
              console.log(this.query);
              this.results = data;
            })
            .catch(err => this.results = []);
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

  #globalSearchBar {
    min-width: 250px;
  }

  .search-results {
    position: absolute;
    z-index: 1;
    background-color: #ffffff;
    border: 1px solid #bbbbbb;
    min-width: 250px;
    max-width: 250px;
  }

  .search-item:hover {
    background-color: #dddddd;
    cursor: pointer;
  }

</style>
