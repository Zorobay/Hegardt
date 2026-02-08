import Aura from '@primeuix/themes/aura';
import { definePreset } from '@primeuix/themes';

const Theme = definePreset(Aura, {
  semantic: {
    primary: {
      50: '#e8eef9',
      100: '#c2d4f0',
      200: '#99b8e7',
      300: '#709cde',
      400: '#5286d6',
      500: '#3261c4',
      600: '#2d59b0',
      700: '#274f9d',
      800: '#214589',
      900: '#183366',
      950: '#0f2144',
    },
  },
});

export default Theme;
