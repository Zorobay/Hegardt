import type { Person } from '@/types/person.type.ts';
import { formatPersonFullName, formatPersonLifespan } from '@/helpers/person-helper.ts';
import type { Sex } from '@/enums/PersonSexEnum.ts';

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

export class FamilyTreeNode {
  x: number = 0;
  y: number = 0;
  id: number;
  fullName: string;
  sex: Sex;
  lifespan: string;

  constructor(person: Person) {
    this.fullName = formatPersonFullName(person);
    this.id = person.id;
    this.sex = person.sex;
    this.lifespan = formatPersonLifespan(person);
  }

  getCoordinates(): Coordinate {
    return new Coordinate(this.x, this.y);
  }

  setCoordinates(x: number, y: number) {
    this.x = x;
    this.y = y;
  }
}

export class Coordinate {
  x: number = 0;
  y: number = 0;
  constructor(x: number = 0, y: number = 0) {
    this.x = x;
    this.y = y;
  }
}
