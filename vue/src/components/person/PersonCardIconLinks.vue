<script setup lang="ts">
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import type { EntityId, Person } from '@/types/person.type.ts';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const props = withDefaults(defineProps<{ person?: Person; personId?: EntityId }>(), {
  person: undefined,
  personId: undefined,
});

const router = useRouter();
const dialogVisible = ref(false);
const pageReferences = ref<number[]>(props.person ? props.person?.pdfReferences?.map((p) => p.pdfPage) : []);

function onFamilyBookIconClicked(): void {
  if (!props.person) {
    return;
  }
  if (props.person.pdfReferences.length === 1) {
    goToFamilyBook(props.person.pdfReferences[0].pdfPage);
  }
  if (props.person.pdfReferences.length > 1) {
    dialogVisible.value = true;
  }
}

function goToFamilyBook(page: number): void {
  router.push({
    name: 'family-book',
    params: { personId: props.person?.id, page: page },
  });
}
</script>

<template>
  <div class="d-flex flex-row gap-1">
    <router-link class="icon-link" :to="{ name: 'tree', params: { personId: person ? person.id : personId } }">
      <font-awesome-icon icon="sitemap"></font-awesome-icon>
    </router-link>
    <router-link class="icon-link" :to="{ name: 'person', params: { id: person ? person.id : personId } }">
      <font-awesome-icon icon="user"></font-awesome-icon>
    </router-link>
    <template v-if="person && person.pdfReferences.length > 0">
      <a id="family-book-icon" class="icon-link" @click="onFamilyBookIconClicked">
        <font-awesome-icon icon="book"></font-awesome-icon>
      </a>
    </template>
  </div>
  <DialogPrime
    v-model:visible="dialogVisible"
    modal
    dismissable-mask
    header="Family Book References"
    :style="{ width: '20rem' }"
  >
    <span class="text-surface-500"
      >This person is referenced in more than one place in the family book. Select the page reference to go to
      below.</span
    >
    <ListboxPrime :options="pageReferences" @update:model-value="goToFamilyBook"></ListboxPrime>
    <!--    <ButtonPrime v-for="reference in person.pdfReferences">-->
    <!--      {{ reference.pdfPage }}-->
    <!--    </ButtonPrime>-->
  </DialogPrime>
</template>

<style scoped>
#family-book-icon {
  cursor: pointer;
}
</style>
