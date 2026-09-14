<script setup lang="ts">
import { onMounted, onUnmounted, ref, shallowRef, watch } from 'vue';
import type { PDFDocumentProxy } from 'pdfjs-dist';
import * as pdfjsLib from 'pdfjs-dist';
import LoadingSpinner from '@/components/async/LoadingSpinner.vue';
import type { PdfReference } from '@/types/pdf-references.type.ts';
import { pdfReferencesApiService } from '@/api/pdfReferencesApiService.ts';
import { useRouter } from 'vue-router';
import type { EntityId } from '@/types/person.type.ts';

pdfjsLib.GlobalWorkerOptions.workerSrc = '/pdfjs/pdf.worker.min.mjs';

const router = useRouter();

// eslint-disable-next-line vue/define-macros-order
const props = withDefaults(
  defineProps<{ src: string; initialPage?: number; scale?: number; personId?: EntityId | null }>(),
  {
    initialPage: 1,
    scale: 1.5,
    personId: null,
  },
);
const pdfDoc = shallowRef<PDFDocumentProxy | null>(null);
const numPages = ref<number>(0);
const leftPage = ref<number>(getIntialPage());
const isLoading = ref<boolean>(true);
const leftPageRendered = ref(false);
const rightPageRendered = ref(false);

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
  return {
    left: `${reference.x0 * props.scale}px`,
    top: `${reference.y0 * props.scale}px`,
    width: `${reference.width * props.scale}px`,
    height: `${reference.height * props.scale}px`,
  };
}

function goToPerson(id: EntityId): void {
  router.push(`/person/${id}`);
}

async function loadDocument(): Promise<void> {
  pdfDoc.value = await pdfjsLib.getDocument({
    url: props.src,
    wasmUrl: '/pdfjs/wasm/',
  }).promise;
  numPages.value = pdfDoc.value.numPages;
  await renderSpread();
  isLoading.value = false;
}

async function renderSpread(): Promise<void> {
  leftPageRendered.value = false;
  rightPageRendered.value = false;

  await renderPageToCanvas(leftPage.value, leftCanvas.value);
  leftPageRendered.value = true;

  await renderPageToCanvas(leftPage.value + 1, rightCanvas.value);
  rightPageRendered.value = true;
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

watch(leftPage, (newPage: number) => {
  renderSpread();
  router.replace({ name: 'family-book', params: { page: newPage } });
});
</script>

<template>
  <div class="pdf-viewer">
    <div v-if="isLoading">
      <loading-spinner />
    </div>

    <div class="pdf-spread">
      <div class="pdf-page">
        <canvas ref="leftCanvas" class="pdf-page"></canvas>
        <template v-if="leftPageRendered">
          <div
            v-for="reference in references.get(leftPage) ?? []"
            :key="reference.personId"
            :style="toScreenBox(reference)"
            class="pdf-reference-box"
            :class="{ highlighted: reference.personId === personId }"
            @click="goToPerson(reference.personId)"
          ></div>
        </template>
      </div>

      <div class="pdf-page">
        <canvas ref="rightCanvas" class="pdf-page"></canvas>
        <template v-if="rightPageRendered">
          <div
            v-for="reference in references.get(leftPage + 1) ?? []"
            :key="reference.personId"
            :style="toScreenBox(reference)"
            class="pdf-reference-box"
            :class="{ highlighted: reference.personId === personId }"
            @click="goToPerson(reference.personId)"
          ></div>
        </template>
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
  outline: 2px solid var(--vibrant-blue);
  box-sizing: content-box;
  cursor: pointer;
}

.pdf-reference-box:hover {
  outline: 2px solid var(--lavender-gray);
}

.highlighted {
  outline: 2px solid var(--vibrant-coral);
}
</style>
