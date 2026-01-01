// eslint.config.js
import js from '@eslint/js';
import pluginVue from 'eslint-plugin-vue';
import skipFormatting from '@vue/eslint-config-prettier/skip-formatting';
import tseslint from 'typescript-eslint';
import vueParser from 'vue-eslint-parser';

export default [
  {
    name: 'app/files-to-lint',
    files: ['**/*.{ts,mts,tsx,js,mjs,jsx,vue}'],
  },

  {
    name: 'app/files-to-ignore',
    ignores: ['**/dist/**', '**/dist-ssr/**', '**/coverage/**'],
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
      // Vue component tag order - script, template, style
      'vue/component-tags-order': [
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
      // Semicolon rule - ALWAYS require them
      semi: ['error', 'always'],
      '@typescript-eslint/semi': ['error', 'always'],
      '@typescript-eslint/no-unused-vars': [
        'error',
        {
          argsIgnorePattern: '^_',
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
      // Space before blocks
      'space-before-blocks': ['error', 'always'],

      // Keyword spacing (space before/after keywords like if, for, etc.)
      'keyword-spacing': [
        'error',
        {
          before: true,
        },
      ],
    },
  },

  skipFormatting,
];
