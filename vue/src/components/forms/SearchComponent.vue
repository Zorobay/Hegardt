<script setup lang="ts">
import { onMounted, ref } from 'vue';
import type { Person, PersonSummary } from '@/types/person.type.ts';
import { formatPersonFullName } from '@/helpers/person-helper.ts';
import { personsApiService } from '@/api/personsApiService.ts';
import PersonCard from '@/components/person/PersonCard.vue';

const props = withDefaults(
  defineProps<{ defaultId?: number; placeholderText?: string; customNavigation?: boolean }>(),
  {
    defaultId: 0,
    placeholderText: 'Search',
    customNavigation: false,
  },
);
const emit = defineEmits<{ onPersonClicked: [number] }>();

const showDropdown = ref(false);
const searchQuery = ref('');
const matchingPersons = ref<Person[]>([]);

onMounted(async () => {
  if (props.defaultId) {
    const res = await personsApiService.getSummaryById(props.defaultId);
    searchQuery.value = formatPersonFullName(res.data);
  }
});
async function onKeyup(event: KeyboardEvent): Promise<void> {
  const query = (event.target as HTMLInputElement)?.value;
  searchQuery.value = query;
  if (query) {
    const res = await personsApiService.findByName(query);
    matchingPersons.value = res.data;
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

function onPersonClick(person: Person | PersonSummary): void {
  showDropdown.value = false;
  searchQuery.value = formatPersonFullName(person);
  if (props.customNavigation) {
    emit('onPersonClicked', person.id);
  }
}
</script>

<template>
  <form role="search" class="heg-search-component">
    <div class="position-relative d-flex flex-row">
      <input
        v-model="searchQuery"
        class="form-control me-2"
        type="search"
        :placeholder="placeholderText"
        aria-label="Search"
        @keyup="onKeyup"
        @blur="onBlur"
        @focus="onFocus"
      />

      <span v-if="matchingPersons.length > 0 && showDropdown" class="badge bg-primary results-badge">
        {{ matchingPersons.length }}
      </span>

      <div v-if="showDropdown" class="dropdown-menu show w-100">
        <person-card
          v-for="person in matchingPersons"
          :key="person.id"
          :custom-navigation="customNavigation"
          compact
          :person="person"
          :navigate="false"
          class="person-card"
          @on-card-clicked="onPersonClick"
        />
      </div>
      <ButtonPrime type="submit"> Search </ButtonPrime>
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
  max-height: 20rem;
  overflow: hidden auto;
}

.person-card {
  height: 4rem;
  width: 98%;
}
</style>
