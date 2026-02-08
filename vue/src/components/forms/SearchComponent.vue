<script setup lang="ts">
import personService from '@/services/PersonService.ts';
import { onMounted, ref } from 'vue';
import type { Person } from '@/types/person.type.ts';
import { formatPersonFullName, formatPersonLifespan } from '@/helpers/person-helper.ts';
import PortraitComponent from '@/components/person/PortraitComponent.vue';

const props = defineProps<{ defaultId?: number }>();
const emit = defineEmits<{ onPersonClicked: [number] }>();

const showDropdown = ref(false);
const searchQuery = ref('');
const matchingPersons = ref<Person[]>([]);

onMounted(async () => {
  searchQuery.value = formatPersonFullName(personService.getPersonById(props.defaultId));
});
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
  searchQuery.value = formatPersonFullName(person);
  emit('onPersonClicked', person.id);
}
</script>

<template>
  <form role="search" class="heg-search-component">
    <div class="position-relative d-flex flex-row">
      <input
        v-model="searchQuery"
        class="form-control me-2"
        type="search"
        placeholder="Search"
        aria-label="Search"
        @keyup="onKeyup"
        @blur="onBlur"
        @focus="onFocus"
      />

      <span v-if="matchingPersons.length > 0 && showDropdown" class="badge bg-primary results-badge">
        {{ matchingPersons.length }}
      </span>

      <div v-if="showDropdown" class="dropdown-menu show w-100">
        <a v-for="person in matchingPersons" :key="person.id" class="dropdown-item my-1" @click="onPersonClick(person)">
          <PortraitComponent />

          <div class="dropdown-person-info">
            <h6>{{ formatPersonFullName(person) }}</h6>
            <p class="text-body-secondary small m-0">{{ formatPersonLifespan(person) }}</p>
          </div>
        </a>
      </div>
      <ButtonPrime type="submit"> Search </ButtonPrime>
    </div>
  </form>
</template>

<style scoped>
.heg-portrait {
  width: 2rem;
  flex-shrink: 0;
}

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
  display: flex;
  align-items: center;
  gap: 0.75rem;
  width: 100%;
  justify-content: flex-start;
}

.dropdown-person-info {
  flex: 1;
  min-width: 0;
}

.dropdown-item:last-child {
  border-bottom: none;
}
</style>
