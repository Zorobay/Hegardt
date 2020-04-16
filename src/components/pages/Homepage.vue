<template>
  <div>
    <p>Welcome to the personal page of
      <router-link :to="{name: 'PersonalFile',
       params: {id: '000000000000000000000635'}}">Sebastian Hegardt</router-link>.
    </p>
  </div>
</template>

<script>
  export default {
    name: 'Homepage',
  };
</script>

<style scoped>

</style>
