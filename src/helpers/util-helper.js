function fuzz(s) {
  return s?.toLowerCase()?.trim()?.replaceAll(' ', '')
}

export function filterNullOrUndefined(list) {
  return list.filter(e => {return !nullOrUndefined(e)});
}

export function nullOrUndefined(data) {
  return data === null || data === undefined;
}

/**
 *
 * @param baseString The string that is to be searched
 * @param searchString The string that is to be matched. If this string is included in 'baseString' then this function returns true
 */
export function fuzzyMatch(baseString, searchString) {
  const baseStringFuzzy = fuzz(baseString);
  const searchStringsFuzzy = searchString?.split(' ')?.map(s => fuzz(s));
  return searchStringsFuzzy.every(s => baseStringFuzzy?.includes(s));
}

export function elvis(data, def) {
  if (!data) {
    return def;
  }
  return data;
}
