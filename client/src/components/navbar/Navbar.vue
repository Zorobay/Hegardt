<template>
  <b-navbar toggleable="lg" type="dark" variant="primary">
    <b-navbar-brand href="#">Sebastian.hegardt.se</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>

      <!--Left aligned nav items-->
      <b-navbar-nav>
        <b-nav-item href="/#">Home</b-nav-item>

        <b-nav-item-dropdown text="Hegardt.se" right>
          <b-dropdown-item href="#/hegardt">Hem</b-dropdown-item>
          <b-dropdown-item href="#/hegardt/register">Register</b-dropdown-item>
          <b-dropdown-item href="#/hegardt/map">Karta</b-dropdown-item>
        </b-nav-item-dropdown>

        <b-nav-item-dropdown text="Other Projects">
          <b-dropdown-item href="#/recipes">Recipes</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <search-form></search-form>
      </b-navbar-nav>

    </b-collapse>
  </b-navbar>
</template>

<script>
  import SearchForm from "./SearchForm";

  export default {
    name: "Navbar",
    components: {SearchForm},

  }
</script>

<style scoped>

</style>
