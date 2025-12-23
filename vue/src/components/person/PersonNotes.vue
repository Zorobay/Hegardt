<script setup lang="ts">
import ReadonlyText from "@/components/person/PersonTextProperty.vue";

defineProps(['notes']);

</script>

<template>
  <ReadonlyText title="Notes">
    <p class="heg-rich-text">{{notes}}</p>
  </ReadonlyText>
</template>

<style scoped>

</style>
