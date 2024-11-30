export function filterNullOrUndefined(list) {
  return list.filter(e => {return !nullOrUndefined(e)});
}

export function nullOrUndefined(data) {
  return data === null || data === undefined;
}

export function elvis(data, def) {
  if (!data) {
    return def;
  }
  return data;
}
