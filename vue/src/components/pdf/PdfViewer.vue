<script setup lang="ts">
import { onMounted, onUnmounted, ref, shallowRef, watch } from 'vue';
import type { PDFDocumentProxy } from 'pdfjs-dist';
import * as pdfjsLib from 'pdfjs-dist';
import LoadingSpinner from '@/components/async/LoadingSpinner.vue';
import type { PdfReference } from '@/types/pdf-references.type.ts';
import { pdfReferencesApiService } from '@/api/pdfReferencesApiService.ts';

pdfjsLib.GlobalWorkerOptions.workerSrc = '/pdfjs/pdf.worker.min.mjs';

// eslint-disable-next-line vue/define-macros-order
const props = withDefaults(defineProps<{ src: string; initialPage?: number; scale: number }>(), {
  initialPage: 1,
  scale: 1.5,
});
const pdfDoc = shallowRef<PDFDocumentProxy | null>(null);
const numPages = ref<number>(0);
const leftPage = ref<number>(getIntialPage());
const isLoading = ref<boolean>(true);

const leftCanvas = ref<HTMLCanvasElement | null>(null);
const rightCanvas = ref<HTMLCanvasElement | null>(null);

const references = ref<Map<number, PdfReference[]>>(new Map<number, PdfReference[]>());

function getIntialPage(): number {
  const initPage = Number(props.initialPage);
  if (!initPage || initPage <= 0) {
    return 1;
  }
  if (initPage % 2 === 0) {
    return initPage - 1;
  }
  return initPage;
}

function toScreenBox(reference: PdfReference): { left: string; top: string; width: string; height: string } {
  const res = {
    left: `${reference.x0 * props.scale}px`,
    top: `${reference.y0 * props.scale}px`,
    width: `${reference.width * props.scale}px`,
    height: `${reference.height * props.scale}px`,
  };
  return res;
}

async function loadDocument(): Promise<void> {
  pdfDoc.value = await pdfjsLib.getDocument({
    url: props.src,
    wasmUrl: 'pdfjs/wasm/',
  }).promise;
  numPages.value = pdfDoc.value.numPages;
  await renderSpread();
  isLoading.value = false;
}

async function renderSpread(): Promise<void> {
  await renderPageToCanvas(leftPage.value, leftCanvas.value);
  await renderPageToCanvas(leftPage.value + 1, rightCanvas.value);
}

async function renderPageToCanvas(pageNum: number, canvas: HTMLCanvasElement | null): Promise<void> {
  if (!canvas || !pdfDoc.value) return;
  console.log('Rendering page ' + pageNum);

  const page = await pdfDoc.value.getPage(pageNum);
  const viewport = page.getViewport({ scale: props.scale });
  canvas.width = viewport.width;
  canvas.height = viewport.height;

  const context = canvas.getContext('2d');
  if (context) {
    await page.render({ canvas, viewport, canvasContext: context }).promise;
  }
}

function unrenderCanvas(canvas: HTMLCanvasElement | null): void {
  if (canvas) {
    canvas.width = 0;
  }
}

function showNextPage(): void {
  if (leftPage.value + 2 <= numPages.value) {
    leftPage.value += 2;
  }
}
function showPreviousPage(): void {
  if (leftPage.value - 2 >= 1) {
    leftPage.value -= 2;
  }
}

function onKeyDown(e: KeyboardEvent): void {
  if (e.key === 'ArrowLeft') {
    showPreviousPage();
  }
  if (e.key === 'ArrowRight') {
    showNextPage();
  }
}

onMounted(async () => {
  try {
    references.value = await pdfReferencesApiService.getAllReferences();
  } catch (error) {
    console.error(error);
  }
  await loadDocument();
  window.addEventListener('keydown', onKeyDown);
});

onUnmounted(() => window.removeEventListener('keydown', onKeyDown));

watch(leftPage, renderSpread);
</script>

<template>
  <div class="pdf-viewer">
    <div v-if="isLoading">
      <loading-spinner />
    </div>

    <div class="pdf-spread">
      <div class="pdf-page">
        <canvas ref="leftCanvas" class="pdf-page"></canvas>
        <div
          v-for="reference in references.get(leftPage) ?? []"
          :key="reference.id"
          :style="toScreenBox(reference)"
          class="pdf-reference-box"
        ></div>
      </div>

      <div class="pdf-page">
        <canvas ref="rightCanvas" class="pdf-page"></canvas>
      </div>
    </div>

    <div class="pdf-controls">
      <button class="btn btn-primary" :disabled="leftPage <= 1" @click="showPreviousPage">&lt; Prev</button>
      <span>Pages {{ leftPage }} and {{ leftPage + 1 }} of {{ numPages }}</span>
      <button class="btn btn-primary" :disabled="leftPage + 1 >= numPages" @click="showNextPage">Next &gt;</button>
    </div>
  </div>
</template>

<style scoped>
.pdf-viewer {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

.pdf-spread {
  display: flex;
  flex-direction: row;
  gap: 0.5rem;
  justify-content: center;
}

.pdf-page {
  position: relative;
}

.pdf-controls {
  display: flex;
  flex-direction: row;
  gap: 0.5rem;
  align-items: center;
}

.pdf-reference-box {
  position: absolute;
  outline: 2px solid red;
  box-sizing: content-box;
}
</style>
