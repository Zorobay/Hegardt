import type { Sex } from '@/enums/PersonSexEnum.ts';

export type EntityId = number;

export interface PartialDate {
  date: {
    $date: number;
  };
  day: number | null;
  month: number | null;
  year: number | null;
}

export interface Location {
  city: string;
  country: string;
  notes: string;
  region: string;
  latitude?: number;
  longitude?: number;
  fetchStatus?: string;
}

export interface LifeEvent {
  date: PartialDate | null;
  location: Location | null;
  notes: string;
}

export interface Marriage {
  date?: PartialDate | null;
  location?: Location | null;
  spouse1: PersonSummary;
  spouse2: PersonSummary;
}

export interface Occupation {
  id: EntityId;
  notes: string;
  location: Location;
  date: PartialDate;
}

export interface PersonTreeNode extends PersonBasic {
  father: PersonTreeNode;
  mother: PersonTreeNode;
}

export interface PersonTreeRoot extends PersonBasic {
  children: Set<PersonSummary>;
  father: PersonTreeNode;
  mother: PersonTreeNode;
}

export interface Person extends PersonSummary {
  occupations: Occupation[];
  father?: PersonSummary;
  mother?: PersonSummary;
  children: Person[];
  siblings: Person[];
  marriages: Marriage[];
}

export interface PersonSummary extends PersonBasic {
  notes: string;
  pdfPage: number;
}

export interface PersonBasic {
  id: EntityId;
  firstName: string;
  lastName: string;
  middleNames: string;
  sex: Sex;
  birth: LifeEvent;
  death: LifeEvent;
  burial: LifeEvent;
}

export interface PersonsMap {
  [key: EntityId]: Person;
}
