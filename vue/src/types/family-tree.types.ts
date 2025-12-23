import type { Person } from '@/types/person.type.ts';

export interface EnhancedPerson extends Person {
  x: number;
  y: number;
}

export interface FamilyTree {
  centerX: number;
  centerY: number;
  minX: number;
  maxX: number;
  minY: number;
  maxY: number;
  persons: EnhancedPerson[];
}

export function newFamilyTree(): FamilyTree {
  return { centerX: 0, centerY: 0, minX: 0, minY: 0, maxX: 0, maxY: 0, persons: [] };
}
