<script setup lang="ts">
import personService from '@/services/PersonService.ts';
import { ref } from 'vue';
import type { Person } from '@/types/person.type.ts';
import { formatPersonFullName } from '@/helpers/person-helper.ts';
import { useRouter } from 'vue-router';

const router = useRouter();

const showDropdown = ref(false);
const searchQuery = ref('');
const matchingPersons = ref<Person[]>([]);

function onKeyup(event: KeyboardEvent): void {
  const query = (event.target as HTMLInputElement)?.value;
  searchQuery.value = query;
  if (query) {
    matchingPersons.value = personService.getPersonsByName(query);
    if (matchingPersons.value.length > 0) {
      showDropdown.value = true;
    }
  } else {
    matchingPersons.value = [];
  }
}

function onBlur(): void {
  setTimeout(() => {
    showDropdown.value = false;
  }, 100);
}

function onFocus(): void {
  if (matchingPersons.value?.length > 0 && searchQuery.value?.length > 0) {
    showDropdown.value = true;
  }
}

function onPersonClick(person: Person): void {
  showDropdown.value = false;
  const id = person.id;
  router.push({ name: 'person', params: { id: id } });
}

function formatPersonDates(person: Person): string {
  const birthYear = person.birth?.date?.year ?? '';
  const deathYear = person.death?.date?.year ?? '';
  return `${birthYear}${deathYear ? ' - ' : ''}${deathYear}`;
}
</script>

<template>
  <form role="search">
    <div class="position-relative d-flex flex-row">
      <input
        class="form-control me-2"
        type="search"
        placeholder="Search"
        aria-label="Search"
        @keyup="onKeyup"
        @blur="onBlur"
        @focus="onFocus"
      />

      <span
        v-if="matchingPersons.length > 0 && showDropdown"
        class="badge bg-primary results-badge"
      >
        {{ matchingPersons.length }}
      </span>

      <div v-if="showDropdown" class="dropdown-menu show w-100">
        <a
          v-for="person in matchingPersons"
          :key="person.id"
          class="dropdown-item my-1"
          @click="onPersonClick(person)"
        >
          <h6>{{ formatPersonFullName(person) }}</h6>
          <p class="text-body-secondary m-0">{{ formatPersonDates(person) }}</p>
        </a>
      </div>
      <button class="btn btn-primary" type="submit">Search</button>
    </div>
  </form>
</template>

<style scoped>
.results-badge {
  position: absolute;
  right: 7.75rem;
  top: 50%;
  transform: translateY(-50%);
  pointer-events: none;
}

.dropdown-menu {
  top: 100%;
  max-height: 12rem;
  overflow-y: auto;
}

.dropdown-item {
  cursor: pointer;
  border-bottom: 1px solid #e9ecef;
}

.dropdown-item:last-child {
  border-bottom: none;
}
</style>
