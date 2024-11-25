<template>
  <div class="form-floating mb-3">
  <input type="text" readonly class="form-control-plaintext" id="floatingPlaintextInput" :value="text">
  <label for="floatingPlaintextInput">{{title}}</label>
</div>
</template>

<script setup>
 defineProps(['text', 'title'])
</script>

<style scoped>

input {
  background: #2c3e50;
}
</style>
