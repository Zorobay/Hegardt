import type { TrackedMedia, TrackedMediaWatch } from '@/types/person.type.ts';

export function getLatestWatch(trackedMedia: TrackedMedia): TrackedMediaWatch | undefined {
  trackedMedia.watches.sort((a: TrackedMediaWatch, b: TrackedMediaWatch) => {
    return b.timestamp.getTime() - a.timestamp.getTime();
  });
  if (trackedMedia.watches.length > 0) {
    return trackedMedia.watches[0];
  }
  return undefined;
}

export function isMovie(trackedMedia: TrackedMedia): boolean {
  return trackedMedia.type === 'MOVIE';
}

export function isTv(trackedMedia: TrackedMedia): boolean {
  return trackedMedia.type === 'TV';
}
