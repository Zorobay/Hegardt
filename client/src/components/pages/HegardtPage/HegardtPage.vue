<template>
  <div>
    <p>Välkommen till Hegardt.se, ett släktforskningsprojekt startat av
      <router-link :to="{name: 'PersonalFile', params: {id: '?'}}">Peter Hegardt</router-link>
      och fortsatt av <router-link :to="{name: 'PersonalFile', params: {id: '000000000000000000000635'}}">
        Sebastian Hegardt</router-link>.
    </p>
    <p>{{ladi}}</p>

    <p>{{getLang}}</p>
  </div>
</template>

<script>
  export default {
    name: "HegardtPage",
    computed: {
      ladi() {
        return this.$store.getters.language;
      },
      ladi2() {
        return this.$store.getters.languageDict;
      }
    }
  }
</script>

<style scoped>

</style>
