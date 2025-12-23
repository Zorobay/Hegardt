<script setup lang="ts">
import personService from '@/services/PersonService.ts';
import { formatPersonFullName } from '@/helpers/person-helper.ts';
import { onMounted, ref } from 'vue';
import { Person } from '@/types/person.type.ts';
import {EnhancedPerson, FamilyTree, newFamilyTree } from '@/types/family-tree.types.ts';

const { id } = defineProps({ id: { type: String, required: true } });
const visitedPersonIds = new Set<number>();

let rawPersons = personService.getAllPersonsList();
const rawPersonsData = personService.getAllPersons();
const enhancedPersons = ref([]);

onMounted(() => {
  enhancedPersons = enhancePersons(rawPersons);
});

const enhancePersons = (persons: Person[]): EnhancedPerson[] => {
  const firstPerson = rawPersons[0];
  const subTrees: Person[][] = [];
  while (visitedPersonIds.size < rawPersons.length) {
    const familySubTree = enhanceFamilySubTree(firstPerson, newFamilyTree());
    subTrees.push(familySubTree);
    rawPersons = rawPersons.filter((person) => !familySubTree.includes( person));
  }
};

const enhanceFamilySubTree = (person: Person, tree: FamilyTree): FamilyTree => {
  if (visitedPersonIds.has(person.id)) {
    return tree
  }
  const mothersFamilySubTree = person.mother ? enhanceFamilySubTree(rawPersonsData[person.mother], tree) : [];
  const fathersFamilySubTree = person.father ? enhanceFamilySubTree(rawPersonsData[person.father], tree): [];
  const childrensFamilySubTree = person.children.map(childId => {
    return enhanceFamilySubTree(rawPersonsData[childId], tree);
  });
  const enhancedPerson = {...person, x: }
};

enum PushDirection {
  NORTH_WEST = 0,
  NORTH_EAST = 1,

}

const recEnhanceFamilySubTree = (person: Person, tree: FamilyTree): EnhancedPerson[] => {};
</script>

<template>
  <div class="card">
    <div class="card-body">
      <svg width="800" height="600">
        <g v-for="person in rawPersons" :key="person.id">
          <rect width="50" height="50" ry="5" x="0" y="0">
            <text x="auto" y="auto" fill="white">
              {{ formatPersonFullName(person) }}
            </text>
          </rect>
        </g>
      </svg>
    </div>
  </div>
</template>

<style scoped></style>
