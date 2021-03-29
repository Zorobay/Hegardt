<template>
  <div class="footer">
    <b-col>
      <p>Author: Sebastian Hegardt</p>
      <p><a href="mailto:se.hegardt@gmail.com">se.hegardt@gmail.com</a></p>
    </b-col>
    <b-col>
      <router-link :to="{name: 'CreditPage'}">Credit</router-link>
    </b-col>
  </div>
</template>

<script>
  export default {
    name: 'MyFooter',
  };
</script>

<style scoped>
  .footer {
    margin-top: 5vh;
    padding: 1em;
    text-align: center;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: aliceblue;
  }
</style>
