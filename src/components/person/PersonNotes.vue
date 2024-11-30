<template>
  <ReadonlyText title="Notes">
    <p class="heg-rich-text">{{notes}}</p>
  </ReadonlyText>
</template>

<script setup>
import ReadonlyText from "@/components/person/PersonTextProperty.vue";

defineProps(['notes']);

</script>

<style scoped>

</style>
