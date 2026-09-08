<script setup lang="ts">
import PdfViewer from '@/components/pdf/PdfViewer.vue';

const props = defineProps({ page: { type: Number, required: false, default: 1 } });
</script>

<template>
  <div id="family-book-container">
    <div id="family-book-buttons-container">
      <ButtonPrime
        label="Download 300 DPI"
        as="a"
        target="_blank"
        href="/static_media/pdfs/hegardt_300dpi_compressed.pdf"
      />
      <ButtonPrime label="Download 600 DPI" as="a" target="_blank" href="/static_media/pdfs/Hegardt_600dpi.pdf" />
    </div>

    <PdfViewer src="/static_media/pdfs/hegardt_300dpi_compressed.pdf" :initial-page="props.page" />
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
