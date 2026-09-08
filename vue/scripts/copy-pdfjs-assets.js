// scripts/copy-pdfjs-assets.js
//
// Why this exists:
// pdf.js needs its worker script (pdf.worker.min.mjs) and its wasm codec
// binaries (jbig2.wasm, openjpeg.wasm, qcms_bg.wasm, etc.) to be reachable
// as plain static files at runtime, served from known URLs.
//
// Vite's `new URL('...', import.meta.url)` bundling trick only works for a
// single, statically-traceable file reference - it does NOT work for a
// directory path into a package (like 'pdfjs-dist/wasm/'), because pdf.js
// builds the actual file URLs itself at runtime (wasmUrl + 'jbig2.wasm',
// etc.), which Vite can't see or trace at build time. Without this, wasm
// codec loading silently fails in dev and 404s in production.
//
// The reliable fix is to copy these files straight out of node_modules and
// into public/, where Vite copies everything byte-for-byte into dist/ with
// no bundling logic involved. This script automates that copy so it
// re-runs on every `npm install` (e.g. after bumping the pdfjs-dist
// version), instead of relying on someone remembering to do it by hand.

import { copyFileSync, existsSync, mkdirSync, readdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));

const PDFJS_BUILD_DIR = join(__dirname, '../node_modules/pdfjs-dist/build');
const PDFJS_WASM_DIR = join(__dirname, '../node_modules/pdfjs-dist/wasm');

const PUBLIC_PDFJS_DIR = join(__dirname, '../public/pdfjs');
const PUBLIC_WASM_DIR = join(__dirname, '../public/pdfjs/wasm');

const WORKER_FILENAME = 'pdf.worker.min.mjs';

function ensureDir(path) {
  if (!existsSync(path)) {
    mkdirSync(path, { recursive: true });
  }
}

function copyFile(sourceDir, filename, destDir) {
  const source = join(sourceDir, filename);
  const dest = join(destDir, filename);

  if (!existsSync(source)) {
    console.warn(`[copy-pdfjs-assets] Skipping missing file: ${source}`);
    return;
  }

  copyFileSync(source, dest);
  console.log(`[copy-pdfjs-assets] Copied ${filename} to ${dest}`);
}

function main() {
  if (!existsSync(PDFJS_BUILD_DIR) || !existsSync(PDFJS_WASM_DIR)) {
    console.warn('[copy-pdfjs-assets] pdfjs-dist not found in node_modules, skipping.');
    return;
  }

  ensureDir(PUBLIC_PDFJS_DIR);
  ensureDir(PUBLIC_WASM_DIR);

  // Worker script - lives in build/
  copyFile(PDFJS_BUILD_DIR, WORKER_FILENAME, PUBLIC_PDFJS_DIR);

  // Wasm codec binaries - copy every .wasm file found, so this keeps working
  // even if pdf.js adds/renames binaries in a future version.
  const wasmFiles = readdirSync(PDFJS_WASM_DIR).filter((f) => f.endsWith('.wasm'));

  if (wasmFiles.length === 0) {
    console.warn('[copy-pdfjs-assets] No .wasm files found in pdfjs-dist/wasm.');
  }

  for (const filename of wasmFiles) {
    copyFile(PDFJS_WASM_DIR, filename, PUBLIC_WASM_DIR);
  }

  console.log('[copy-pdfjs-assets] Done.');
}

main();
