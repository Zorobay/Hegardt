<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light"><a class="navbar-brand" href="#">Hegardt.se</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarContent"><span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarContent">
        <ul class="navbar-nav mr-auto" id="navList">
          <li class="nav-item active"><a class="nav-link" id="navItemHome" href="/">Hem</a></li>
          <li class="nav-item"><a class="nav-link" id="navItemRegister" href="/#/register">
            Personregister</a></li>
          <li class="nav-item"><a class="nav-link" id="navItemMap" href="/#/karta">Karta</a></li>
        </ul>
        <div class="dropdown"><input class="form-control mr-sm-2" id="globalSearchBar" type="search" onkeyup="showResults(this.value)" role="combobox"
                                     placeholder="sök">
          <ul class="dropdown-menu" id="searchResults" role="menu"></ul>
        </div>
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Sök</button>
      </div>
    </nav>
</template>

<script>
    export default {
        name: "Navbar"
    }
</script>

<style scoped>

</style>
