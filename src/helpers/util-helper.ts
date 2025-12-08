function fuzz(s: string): string {
  return s?.toLowerCase()?.trim()?.replaceAll(' ', '');
}

export function filterNullOrUndefined<T>(list: T[]): Exclude<T, null | undefined>[] {
  return list.filter((e: T): e is Exclude<T, null | undefined> => {
    return !nullOrUndefined(e);
  });
}

export function nullOrUndefined(data: unknown): boolean {
  return data === null || data === undefined;
}
/**
 *
 * @param baseString The string that is to be searched
 * @param searchString The string that is to be matched. If this string is included in 'baseString' then this function returns true
 */
export function fuzzyMatch(baseString: string, searchString: string): boolean {
  const baseStringFuzzy = fuzz(baseString);
  const searchStringsFuzzy = searchString?.split(' ')?.map((s) => fuzz(s));
  return searchStringsFuzzy.every((s: string) => baseStringFuzzy?.includes(s));
}
