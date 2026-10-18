import { format } from 'date-fns';

const MINUTE_SECONDS = 60;
const HOUR_SECONDS = MINUTE_SECONDS * 60;
const DAY_SECONDS = HOUR_SECONDS * 24;
const WEEK_SECONDS = DAY_SECONDS * 7;
const YEAR_SECONDS = WEEK_SECONDS * 52;

const DATE_FORMAT_TIME = 'H:m:s';

export function describeTimeAgoShort(date: Date | undefined): string {
  if (!date) {
    return '';
  }

  const now = Date.now();
  const diffSeconds = (now - date.getTime()) / 1000;
  if (diffSeconds < MINUTE_SECONDS) {
    return 'now';
  }
  if (diffSeconds >= MINUTE_SECONDS && diffSeconds < HOUR_SECONDS) {
    return `${Math.floor(diffSeconds / MINUTE_SECONDS)}m ago`;
  }
  if (diffSeconds >= HOUR_SECONDS && diffSeconds < DAY_SECONDS) {
    return `${Math.floor(diffSeconds / HOUR_SECONDS)}h ago`;
  }
  if (diffSeconds >= DAY_SECONDS && diffSeconds < WEEK_SECONDS) {
    return `${Math.floor(diffSeconds / DAY_SECONDS)}d ago`;
  }
  if (diffSeconds >= WEEK_SECONDS && diffSeconds < YEAR_SECONDS) {
    return `${Math.floor(diffSeconds / WEEK_SECONDS)}w ago`;
  }
  if (diffSeconds >= YEAR_SECONDS) {
    return `${Math.floor(diffSeconds / YEAR_SECONDS)}y ago`;
  }
  return '?';
}

export function timeAsString(date: Date): string {
  return format(date, DATE_FORMAT_TIME);
}
