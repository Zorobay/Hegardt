import type { Sex } from '@/enums/PersonSexEnum.ts';

export type PersonId = number;
export type PersonOptionalId = PersonId | null | undefined;
export interface DateInfo {
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
  date: DateInfo | null;
  location: Location | null;
  notes: string;
}

export interface Marriage {
  date?: DateInfo | null;
  location?: Location | null;
  personId: PersonId;
}

export interface Person {
  pdfPage?: number;
  birth: LifeEvent;
  burial: LifeEvent;
  children: PersonId[];
  death: LifeEvent;
  father: PersonOptionalId;
  fileId: string;
  firstName: string;
  lastName: string;
  marriages: Marriage[];
  middleNames: string[];
  mother: PersonOptionalId;
  notes: string;
  occupations: string[];
  references: string[];
  sex: Sex;
  id: PersonId;
}

export interface PersonsData {
  [key: PersonId]: Person;
}
