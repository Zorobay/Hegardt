import js from '@eslint/js';
import stylistic from '@stylistic/eslint-plugin';
import skipFormatting from '@vue/eslint-config-prettier/skip-formatting';
import pluginVue from 'eslint-plugin-vue';
import { defineConfig, globalIgnores } from 'eslint/config';
import globals from 'globals';
import tseslint from 'typescript-eslint';
import vueParser from 'vue-eslint-parser';

export default defineConfig([
  {
    name: 'app/files-to-lint',
    files: ['**/*.{ts,mts,tsx,js,mjs,jsx,vue}'],
  },

  // Only the frontend workspaces (vue/, sebastian/, shared/) are linted
  globalIgnores([
    '**/node_modules/**',
    '**/dist/**',
    '**/dist-ssr/**',
    '**/coverage/**',
    '**/public/pdfjs/**',
    'micronaut/**',
    'python/**',
    'scripts/**',
    'bruno/**',
    'static_media/**',
  ]),

  // Browser globals for app code (window, document, ...)
  {
    name: 'app/globals',
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module',
      globals: {
        ...globals.browser,
      },
    },
  },

  // Node globals for config files (vite.config.ts, eslint.config.js, ...)
  {
    name: 'app/node-config-files',
    files: ['**/*.config.{js,mjs,cjs,ts,mts}'],
    languageOptions: {
      globals: {
        ...globals.node,
      },
    },
  },

  js.configs.recommended,
  ...tseslint.configs.recommended,
  ...pluginVue.configs['flat/recommended'],

  {
    name: 'app/vue-rules',
    files: ['**/*.vue'],
    languageOptions: {
      parser: vueParser,
      parserOptions: {
        parser: tseslint.parser,
        extraFileExtensions: ['.vue'],
        sourceType: 'module',
      },
    },
    rules: {
      // Vue script setup order - defineProps, defineEmits
      'vue/define-macros-order': [
        'error',
        {
          order: ['defineProps', 'defineEmits'],
          defineExposeLast: false,
        },
      ],
      // Vue block order - script, template, style
      'vue/block-order': [
        'error',
        {
          order: ['script', 'template', 'style'],
        },
      ],
    },
  },

  // TypeScript-specific rules
  {
    name: 'app/typescript-rules',
    files: ['**/*.{ts,mts,tsx,vue}'],
    rules: {
      // Member ordering of classes
      '@typescript-eslint/member-ordering': [
        'error',
        {
          default: [
            // Static members
            'public-static-field',
            'protected-static-field',
            'private-static-field',

            // Instance fields
            'public-instance-field',
            'protected-instance-field',
            'private-instance-field',

            // Constructor
            'constructor',

            // Static methods
            'public-static-method',
            'protected-static-method',
            'private-static-method',

            // Instance methods
            'public-instance-method',
            'protected-instance-method',
            'private-instance-method',
          ],
        },
      ],
      // Override complaining about 'props' and '_' in .vue components
      '@typescript-eslint/no-unused-vars': [
        'error',
        {
          argsIgnorePattern: '^_',
          varsIgnorePattern: '^props$',
        },
      ],
      '@typescript-eslint/explicit-function-return-type': [
        'warn',
        {
          allowExpressions: true,
          allowTypedFunctionExpressions: true,
          allowHigherOrderFunctions: true,
          allowDirectConstAssertionInArrowFunctions: true,
          allowConciseArrowFunctionExpressionsStartingWithVoid: true,
        },
      ],
      '@typescript-eslint/no-explicit-any': 'warn',
      '@typescript-eslint/consistent-type-imports': [
        'error',
        {
          prefer: 'type-imports',
        },
      ],
    },
  },

  // Per-app overrides go here, e.g.:
  // {
  //   name: 'sebastian/overrides',
  //   files: ['sebastian/**/*.{ts,vue}'],
  //   rules: {},
  // },

  // Turns off formatting rules that conflict with Prettier
  skipFormatting,

  // Stylistic rules come AFTER skipFormatting, otherwise it switches them off again
  {
    name: 'app/stylistic-rules',
    files: ['**/*.{ts,mts,tsx,js,mjs,jsx,vue}'],
    plugins: {
      '@stylistic': stylistic,
    },
    rules: {
      // Semicolon rule - ALWAYS require them
      '@stylistic/semi': ['error', 'always'],
      // Space before blocks
      '@stylistic/space-before-blocks': ['error', 'always'],
      // Keyword spacing (space before/after keywords like if, for, etc.)
      '@stylistic/keyword-spacing': ['error', { before: true, after: true }],
    },
  },
]);