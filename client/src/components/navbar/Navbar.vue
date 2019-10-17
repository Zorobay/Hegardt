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
        <b-dropdown variant="primary" text="Language" class="m-md-auto">
          <b-dropdown-item>Swedish <img src="icons/sweden.png" height="22"/></b-dropdown-item>
          <b-dropdown-item active>English <img src="icons/usa.jpg" height="14"/></b-dropdown-item>
        </b-dropdown>
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

  .swedish-flag::before{
    content: '\01F1FA\01F1F8';
  }
</style>
