<script setup lang="ts">
import { Input } from '@/components/ui/input';
import { ref } from 'vue';
import { timeAsString } from '../../../shared/src/helpers/time-helpers.ts';

const pickedTime = ref<string>(timeAsString(new Date()));
</script>

<template>
  <Input v-model="pickedTime" type="time" class="appearance-none bg-background"> {{ pickedTime }}</Input>
</template>

<style scoped></style>
