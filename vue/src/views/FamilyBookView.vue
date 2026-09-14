<script setup lang="ts">
import HegardtPdfViewer from '@/components/pdf/HegardtPdfViewer.vue';
import type { EntityId } from '@/types/person.type.ts';

const props = withDefaults(defineProps<{ page?: number; personId?: EntityId }>(), {
  page: 1,
  personId: undefined,
});
</script>

<template>
  <div id="family-book-container">
    <div id="family-book-buttons-container">
      <ButtonPrime label="Download 300 DPI" as="a" target="_blank" href="/static_media/pdfs/hegardt_300dpi.pdf" />
      <ButtonPrime label="Download 600 DPI" as="a" target="_blank" href="/static_media/pdfs/hegardt_600dpi.pdf" />
    </div>

    <HegardtPdfViewer
      src="/static_media/pdfs/hegardt_300dpi.pdf"
      :initial-page="Number(props.page)"
      :person-id="Number(props.personId)"
    />
  </div>
</template>

<style scoped>
#family-book-buttons-container {
  display: flex;
  flex-direction: row;
  gap: 1rem;
}

#family-book-container {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

#family-book-pdf-viewer {
  height: 88vh;
}
</style>
