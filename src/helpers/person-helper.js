import {filterNullOrUndefined} from "@/helpers/util-helper.js";
import {differenceInYears} from "date-fns";

export function formatPersonFullName(person) {
  const firstName = person.firstName;
  const middleNames = person.middleNames;
  const lastName = person.lastName;
  if (!firstName && !middleNames && !lastName) {
    return '?';
  }

  const middleNamesStr = middleNames ? middleNames.join(' ') : '';
  const nameParts = [firstName, middleNamesStr, lastName].filter(el => el);
  return nameParts.join(' ');
}

export function formatPersonDate(date) {
  if (!date) {
    return '';
  }
  const year = date.year;
  const month = _zeroPad(date.month);
  const day = _zeroPad(date.day);
  if (year && !month && !day) {
    return year;
  }
  const parts = filterNullOrUndefined([year, month, day]);
  return parts.join('-');
}

export function formatPersonAge(person) {
  const birthDateObj = person.birth.date;

  if (birthDateObj) {
    let fromDate = personIsDead(person) ? dateObjectToDate(person.death.date) : new Date();
    const birthDate = dateObjectToDate(birthDateObj);
    return differenceInYears(fromDate, birthDate);
  }
  return '?';
}

export function formatPersonLocation(location) {
  if (!location) {
    return '';
  }
  const parts = [location.city, location.country];
  return parts.join(', ');
}

export function personBirthDate(person) {
  return dateObjectToDate(person.birth.date);
}

export function dateObjectToDate(dateObj) {
  return new Date(dateObj.date.$date);
}

export function personIsDead(person) {
  const deathDate = person.death.date;
  return !!deathDate
}

function _zeroPad(data) {
  const dataStr = data ? data.toString() : '';
  if (dataStr.length === 1) {
    return '0' + data;
  }
  return data;
}
