<script setup lang="ts">
import { onMounted, ref, watch } from 'vue';
import type { PDFDocumentProxy, PDFPageProxy, RenderTask } from 'pdfjs-dist';
import * as pdfjsLib from 'pdfjs-dist';

const { src } = defineProps<{ src: string }>();

pdfjsLib.GlobalWorkerOptions.workerSrc = new URL('pdfjs-dist/build/pdf.worker.min.mjs', import.meta.url).toString();

const canvasRefs = ref<HTMLCanvasElement[]>([]);
const containerRef = ref<HTMLDivElement | null>(null);
const scale = ref(0.75);
const totalPages = ref(0);
let pdfDoc: PDFDocumentProxy | null = null;
const renderTasks: RenderTask[] = [];

const renderPage = async (pageNum: number): Promise<void> => {
  const canvas = canvasRefs.value[pageNum - 1];
  if (!canvas) return; // guard against missing ref

  const page: PDFPageProxy = await pdfDoc!.getPage(pageNum);
  const dpr = window.devicePixelRatio || 1;
  const containerWidth = containerRef.value?.clientWidth ?? 800;
  const unscaledViewport = page.getViewport({ scale: 1 });
  const fitScale = (containerWidth / unscaledViewport.width) * scale.value;
  const viewport = page.getViewport({ scale: fitScale * dpr });

  const ctx = canvas.getContext('2d')!;
  canvas.width = viewport.width;
  canvas.height = viewport.height;
  canvas.style.width = `${viewport.width / dpr}px`;
  canvas.style.height = `${viewport.height / dpr}px`;

  const task = page.render({ canvasContext: ctx, viewport, canvas });
  renderTasks[pageNum - 1] = task;

  try {
    await task.promise;
  } catch (e) {
    if (e instanceof Error && e.name === 'RenderingCancelledException') return;
    throw e; // re-throw anything unexpected
  }
};

const cancelAll = async (): Promise<void> => {
  const tasks = [...renderTasks];
  renderTasks.length = 0;
  await Promise.allSettled(
    tasks.map((task) => {
      task?.cancel();
      return task?.promise; // wait for the promise to actually finish
    }),
  );
};

const renderAll = async (): Promise<void> => {
  await cancelAll();
  for (let i = 1; i <= totalPages.value; i++) {
    await renderPage(i);
  }
};

onMounted(async () => {
  pdfDoc = await pdfjsLib.getDocument(src).promise;
  totalPages.value = pdfDoc.numPages;
  await renderAll();
});

watch(scale, renderAll);
</script>

<template>
  <div class="pdf-viewer">
    <div class="controls">
      <button :disabled="scale <= 0.5" @click="scale -= 0.25">−</button>
      <span>{{ Math.round(scale * 100) }}%</span>
      <button :disabled="scale >= 3" @click="scale += 0.25">+</button>
    </div>
    <div ref="containerRef" class="pages">
      <div v-for="n in totalPages" :key="n" class="page-wrapper">
        <canvas :ref="(el) => (canvasRefs[n - 1] = el as HTMLCanvasElement)" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.pdf-viewer {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.controls {
  display: flex;
  gap: 0.5rem;
  align-items: center;
  padding: 0.5rem;
  flex-shrink: 0;
}

.pages {
  overflow: auto;
  flex: 1;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.page-wrapper {
  display: flex;
  justify-content: center;
}

canvas {
  box-shadow: 0 2px 8px rgb(0 0 0 / 20%);
  max-width: none;
}
</style>
