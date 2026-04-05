<script setup lang="ts"></script>

<template>
  <p>Welcome to my website!</p>
  <p>
    This is a website I, <router-link :to="{ name: 'person', params: { id: 619 } }">Sebastian Hegardt</router-link>, am
    developing for my family. The research is mostly based on the work conducted by
    <router-link :to="{ name: 'person', params: { id: 592 } }">Peter Hegardt</router-link>.
  </p>
  <p>😎</p>
</template>
