import { filterNullOrUndefined } from '@/helpers/util-helper.ts';
import { differenceInYears } from 'date-fns';
import type { DateInfo, Location, Person } from '@/types/person.type.ts';

export function formatPersonFullName(person: Person | undefined | null): string {
  if (!person) {
    return '';
  }
  const firstName = person.firstName;
  const middleNames = person.middleNames;
  const lastName = person.lastName;
  if (!firstName && !middleNames && !lastName) {
    return '?';
  }

  const middleNamesStr = middleNames ? middleNames.join(' ') : '';
  const nameParts = [firstName, middleNamesStr, lastName].filter((el) => el);
  return nameParts.join(' ');
}

export function formatPersonDate(date: DateInfo | undefined | null): string {
  if (!date) {
    return '';
  }
  const year = date.year;
  const month = _zeroPad(date.month);
  const day = _zeroPad(date.day);
  if (year && !month && !day) {
    return year?.toString();
  }
  const parts = filterNullOrUndefined([year, month, day]);
  return parts.join('-');
}

export function formatPersonAge(person: Person): string {
  const birthDateObj = person.birth.date;

  if (birthDateObj) {
    const fromDate = personIsDead(person) ? dateObjectToDate(person.death.date) : new Date();
    const birthDate = dateObjectToDate(birthDateObj);
    if (fromDate && birthDate) {
      return differenceInYears(fromDate, birthDate)?.toString();
    }
  }
  return '?';
}

export function formatPersonLocation(location: Location): string {
  if (!location) {
    return '';
  }
  const parts = [location.city, location.country];
  return parts.join(', ');
}

export function personBirthDate(person: Person): Date | undefined {
  return dateObjectToDate(person?.birth?.date);
}

export function dateObjectToDate(dateObj: DateInfo | undefined | null): Date | undefined {
  if (dateObj?.date?.$date) {
    return new Date(dateObj.date.$date);
  }
  return undefined;
}

export function personIsDead(person: Person): boolean {
  const deathDate = person.death.date;
  return !!deathDate;
}

export function formatPersonLifespan(person: Person): string {
  const birthYear = person.birth?.date?.year ?? '';
  const deathYear = person.death?.date?.year ?? '';
  return `${birthYear}${deathYear ? ' - ' : ''}${deathYear}`;
}

function _zeroPad(data: number | undefined | null): string {
  const dataStr = data ? data.toString() : '';
  if (dataStr.length === 1) {
    return '0' + data;
  }
  return dataStr;
}
