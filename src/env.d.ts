// This file is a TypeScript declaration file that provides type definitions for things that TypeScript doesn't understand by default in a Vue project.
// Some libraries don't have TypeScript types. You can declare them in env.d.ts so TypeScript stops complaining.

/// <reference types="vite/client" />

declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  const component: DefineComponent<object, object, unknown>
  export default component
}

// Bootstrap types
declare module 'bootstrap' {
  export * from 'bootstrap'
}
