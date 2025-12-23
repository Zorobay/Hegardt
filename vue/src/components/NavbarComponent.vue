<script setup lang="ts">
import SearchComponent from '@/components/forms/SearchComponent.vue';
</script>

<template>
  <nav id="main-nav" class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Navbar</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div id="navbarSupportedContent" class="collapse navbar-collapse">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'home' }">Home</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'table' }">Table</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'map' }">Map</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink v-show="true" class="nav-link" :to="{ name: 'tree' }">Tree</RouterLink>
          </li>

        </ul>

        <SearchComponent />

        <div class="dropdown">
          <button
            class="btn dropdown-toggle"
            type="button"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            <i class="fa-solid fa-language"></i>
          </button>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#"></a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>

<style scoped>
#main-nav .container-fluid {
  alignment: center;
  max-width: 80%;
}
</style>
