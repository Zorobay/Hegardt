import api from './axios';
import type { AxiosResponse } from 'axios';
import type { TrackedMedia, TrackedMediaDto, TrackedMediaWatch, TrackedMediaWatchDto } from '@/types/person.type.ts';

const mapToTrackedMediaWatch = (data: TrackedMediaWatchDto): TrackedMediaWatch => {
  return {
    ...data,
    timestamp: new Date(data.timestamp),
  };
};
const mapToTrackedMedia = (data: TrackedMediaDto): TrackedMedia => {
  return {
    ...data,
    watches: data.watches.map(mapToTrackedMediaWatch),
  };
};
export const mediaTrackerService = {
  getAll: (): Promise<AxiosResponse<TrackedMedia[]>> =>
    api.get<TrackedMediaDto[]>(`/media_tracker/getAll`).then((res: AxiosResponse<TrackedMediaDto[]>) => {
      return {
        ...res,
        data: res.data.map(mapToTrackedMedia),
      };
    }),
};
