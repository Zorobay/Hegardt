<template>
  <div>
    <p>Welcome to the personal page of
      <router-link :to="{name: 'PersonalFile',
       params: {id: '000000000000000000000635'}}">Sebastian Hegardt</router-link>.
    </p>
    <router-link :to="{name: 'PersonalFile', params: {id: '603fdf72d89e5fbf22f635e3'}}">Mc Persson</router-link>
  </div>
</template>

<script>
  export default {
    name: 'Homepage',
  };
</script>

<style scoped>

</style>
