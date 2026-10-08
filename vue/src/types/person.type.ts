import type { Sex } from '@/enums/PersonSexEnum.ts';
import type { PdfReference } from '@/types/pdf-references.type.ts';

export type EntityId = number;

export interface PartialDate {
  date: string | null;
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

export interface Person extends PersonBasic {
  occupations: Occupation[];
  father?: PersonSummary;
  mother?: PersonSummary;
  children: PersonSummary[];
  siblings: Person[];
  marriages: Marriage[];
  pdfReferences: PdfReference[];
  notes: string;
  pdfPage: number;
}

export interface PersonSummary extends PersonBasic {
  notes: string;
  pdfPage: number;
  father?: PersonMinimal;
  mother?: PersonMinimal;
}

export interface PersonBasic extends PersonMinimal {
  birth: LifeEvent;
  death: LifeEvent;
  burial: LifeEvent;
}

export interface PersonMinimal {
  id: EntityId;
  firstName: string;
  lastName: string;
  middleNames: string;
  sex: Sex;
}

export interface PersonsMap {
  [key: EntityId]: PersonSummary;
}
