<script setup lang="ts">
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import type { MenuItem } from 'primevue/menuitem';
import SearchComponent from '@/components/forms/SearchComponent.vue';

const router = useRouter();
const languageMenu = ref();

const menuItems = ref<MenuItem[]>([
  {
    label: 'Home',
    icon: 'pi pi-home',
    command: () => router.push({ name: 'home' }),
  },
  {
    label: 'Table',
    icon: 'pi pi-table',
    command: () => router.push({ name: 'table' }),
  },
  {
    label: 'Map',
    icon: 'pi pi-map',
    command: () => router.push({ name: 'map' }),
  },
  {
    label: 'Tree',
    icon: 'pi pi-sitemap',
    command: () => router.push({ name: 'tree' }),
  },
  {
    label: 'Family Book',
    icon: 'pi pi-book',
    command: () => router.push({ name: 'family-book' }),
  },
]);

const languageItems = ref<MenuItem[]>([
  { label: 'English', icon: 'pi pi-globe' },
  { label: 'Swedish', icon: 'pi pi-globe' },
  { label: 'Spanish', icon: 'pi pi-globe' },
]);

function onPersonClicked(personId: number): void {
  router.push({ name: 'person', params: { id: personId } });
}
function toggleLanguageMenu(event: Event): void {
  languageMenu.value.toggle(event);
}
</script>

<template>
  <nav id="main-nav">
    <MenubarPrime :model="menuItems">
      <template #start>
        <span class="navbar-brand">Navbar</span>
      </template>

      <template #end>
        <div class="d-flex align-items-center gap-2">
          <SearchComponent @on-person-clicked="onPersonClicked" />

          <ButtonPrime icon="pi pi-language" text rounded aria-label="Language" @click="toggleLanguageMenu" />
          <MenuPrime ref="languageMenu" :model="languageItems" popup />
        </div>
      </template>
    </MenubarPrime>
  </nav>
</template>

<style scoped>
#main-nav {
  margin-bottom: 2rem;
}

.p-menubar {
  width: 100%;
  padding-right: 10rem;
  padding-left: 10rem;
}

.navbar-brand {
  font-size: 1.25rem;
  font-weight: 500;
  cursor: pointer;
}
</style>
