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
        href="/pdf/Hegardt_300dpi_sökbar_adobe_komprimerad.pdf"
      />
      <ButtonPrime
        label="Download 600 DPI"
        as="a"
        target="_blank"
        href="http://battis.quickconnect.to/d/s/16jIW6md5JyDxVAulzEizBjz2UjHND5X/o5smoSSzhjElVUywo61WgOCoar4kP-Rs-frvAF7ng6Qw"
      />
    </div>

    <iframe
      id="family-book-pdf-viewer"
      src="/public/pdf/Hegardt_300dpi_sökbar_adobe_komprimerad.pdf"
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
