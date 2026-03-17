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

export interface Person extends PersonSummary {
  pdfPage?: number;
  children: PersonId[];
  father: PersonOptionalId;
  fileId: string;
  marriages: Marriage[];
  mother: PersonOptionalId;
  notes: string;
  occupations: string[];
  references: string[];
}

export interface PersonSummary {
  id: PersonId;
  firstName: string;
  lastName: string;
  middleNames: string;
  sex: Sex;
  birth: LifeEvent;
  death: LifeEvent;
  burial: LifeEvent;
}

export interface PersonsData {
  [key: PersonId]: Person;
}
