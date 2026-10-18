<script setup lang="ts">
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';

const props = defineProps<{ title: string; value: number }>();
</script>

<template>
  <Card>
    <CardHeader>
      <CardDescription>{{ title }}</CardDescription>
      <CardTitle class="text-3xl"> {{ value }} </CardTitle>
    </CardHeader>
    <CardContent> </CardContent>
  </Card>
</template>

<style scoped></style>
