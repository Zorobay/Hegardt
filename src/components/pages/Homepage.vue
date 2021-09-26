<template>
  <div>
    <p>Welcome to the personal page of
      <router-link :to="{name: 'PersonalFile',
       params: {id: '000000000000000000000635'}}">Sebastian Hegardt</router-link>.
    </p>
    <router-link :to="{name: 'PersonalFile', params: {id: '100000000000000000000000'}}">Mc Persson</router-link>
  </div>
</template>

<script>
  export default {
    name: 'Homepage',
  };
</script>

<style scoped>

</style>
