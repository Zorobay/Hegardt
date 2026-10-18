export interface TrackedMedia {
  id: number;
  title: string;
  tmdb_id: number;
  rating: number;
  posterPath: string;
  type: string;
  watches: TrackedMediaWatch[];
}

export interface TrackedMediaWatch {
  timestamp: Date;
}

export interface TrackedMediaDto extends Omit<TrackedMedia, 'watches'> {
  watches: TrackedMediaWatchDto[];
}

export interface TrackedMediaWatchDto {
  timestamp: string;
}
