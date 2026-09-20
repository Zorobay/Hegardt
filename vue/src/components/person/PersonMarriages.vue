<script setup lang="ts">
import type { EntityId, Marriage, PersonSummary } from '@/types/person.type.ts';
import ReadonlyText from '@/components/person/PersonTextProperty.vue';
import { formatLocation, formatPartialDate, formatPersonFullName } from '@/helpers/person-helper.ts';

const props = defineProps<{ personId: EntityId; marriages: Marriage[] }>();

function getSpouseName(marriage: Marriage): string {
  const spouse = getSpouse(marriage);
  return formatPersonFullName(spouse);
}

function getSpouse(marriage: Marriage): PersonSummary {
  if (marriage.spouse1.id == props.personId) {
    return marriage.spouse2;
  }
  return marriage.spouse1;
}
</script>

<template>
  <ReadonlyText title="Marriages">
    <ul>
      <li v-for="marriage in marriages" :key="getSpouse(marriage).id">
        Married
        <router-link :to="{ name: 'person', params: { id: getSpouse(marriage).id } }">{{
          getSpouseName(marriage)
        }}</router-link>
        on {{ formatPartialDate(marriage.date) }} in {{ formatLocation(marriage.location) }}
      </li>
    </ul>
  </ReadonlyText>
</template>

<style scoped></style>
