<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { mediaTrackerService } from '@/api/mediaTrackerService.ts';
import type { TrackedMedia } from '@/types/person.type.ts';
import { Carousel, CarouselContent, CarouselItem, CarouselNext, CarouselPrevious } from '@/components/ui/carousel';
import { Card, CardContent } from '@/components/ui/card';
import { IconClockPlus, IconEye } from '@tabler/icons-vue';
import { Badge } from '@/components/ui/badge';
import { describeTimeAgoShort } from '../../../shared/src/helpers/time-helpers.ts';
import { getLatestWatch, isMovie, isTv } from '@/helpers/tracked-media-helpers.ts';
import StatCard from '@/components/StatCard.vue';

const allTrackedMedia = ref<TrackedMedia[]>([]);
const trackedMovies = ref<TrackedMedia[]>([]);
const trackedTv = ref<TrackedMedia[]>([]);

onMounted(async () => {
  const res = await mediaTrackerService.getAll();
  allTrackedMedia.value = res.data ?? [];

  trackedMovies.value = allTrackedMedia.value.filter(isMovie);
  trackedTv.value = allTrackedMedia.value.filter(isTv);
});
</script>

<template>
  <div class="flex flex-col gap-6">
    <h1>Movie & TV Tracker</h1>
    <h2>Stats</h2>
    <div class="grid grid-cols-2 gap-6 max-w-120">
      <StatCard title="Unique movies" :value="trackedMovies.length" />
      <StatCard title="Unique TV-shows" :value="trackedTv.length" />
    </div>
    <h2>Recent Activity</h2>
    <Carousel class="w-full">
      <CarouselContent>
        <CarouselItem v-for="item in allTrackedMedia" :key="item.id" class="basis-auto">
          <Card class="relative aspect-2/3 w-36 overflow-hidden p-0">
            <CardContent class="flex aspect-2/3 items-baseline justify-center p-0">
              <img
                :src="`https://image.tmdb.org/t/p/w342${item.posterPath}`"
                class="size-full object-cover"
                :alt="item.title"
                loading="lazy"
              />
              <Badge variant="default" class="absolute top-1">
                <IconClockPlus class="size-10" />
                {{ describeTimeAgoShort(getLatestWatch(item)?.timestamp) }}
              </Badge>
              <Badge v-if="item.watches.length > 1" variant="secondary" class="absolute bottom-1">
                <IconEye />
                {{ item.watches.length }}
              </Badge>
            </CardContent>
          </Card>
        </CarouselItem>
      </CarouselContent>
      <CarouselPrevious class="left-2" />
      <CarouselNext class="right-2" />
    </Carousel>
  </div>
</template>

<style scoped></style>
