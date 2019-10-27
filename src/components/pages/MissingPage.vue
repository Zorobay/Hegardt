<template>
  <div>
    <p>Page does not exist!</p>
    <button class="btn btn-primary" v-on:click="goBack">Go back</button>
  </div>

</template>

<script>
  export default {
    data: {name: "MissingPage"},
    methods: {
      goBack() {
        this.$router.go(-1);
      }
    }
  }
</script>

<style scoped>

</style>
