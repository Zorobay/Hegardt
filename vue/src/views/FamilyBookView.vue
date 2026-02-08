<script setup lang="ts">
const props = defineProps({ page: { type: Number, required: false, default: 0 } });
</script>

<template>
  <div id="family-book-container">
    <div id="family-book-buttons-container">
      <ButtonPrime
        label="Download 300 DPI"
        as="a"
        target="_blank"
        href="/pdf/hegardt_300dpi_searchable_compressed.pdf"
      />
      <ButtonPrime
        label="Download 600 DPI"
        as="a"
        target="_blank"
        href="https://battis.quickconnect.to/d/s/16jIW6md5JyDxVAulzEizBjz2UjHND5X/o5smoSSzhjElVUywo61WgOCoar4kP-Rs-frvAF7ng6Qw"
      />
    </div>

    <iframe
      id="family-book-pdf-viewer"
      src="/pdf/hegardt_300dpi_searchable_compressed.pdf"
      width="100%"
      type="application/pdf"
    ></iframe>
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
  height: 100vh;
}
</style>
