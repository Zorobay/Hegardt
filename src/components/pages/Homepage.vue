<template>
  <div>
      <p>Hej och välkommen till släktforskningssidan för Hegardt-släkten! Detta är ett projekt som fortsätter på det <router-link :to="{name: 'PersonalFile', params: {}}">Peter
        Hegardt gjort med </router-link><a href="http://www.hegardt.se/disgen/html/"> hegardt.se.</a></p>
      <p>Jag som har utvecklat den här sidan heter Sebastian Hegardt</p>
  </div>
</template>

<script>
  export default {
    name: 'Homepage',
  };
</script>

<style scoped>

</style>
