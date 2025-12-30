const SexEnum = Object.freeze({
  MAN: 'MAN',
  WOMAN: 'WOMAN',
  UNKNOWN: 'UNKNOWN',
});

export default SexEnum;
export type Sex = (typeof SexEnum)[keyof typeof SexEnum];
