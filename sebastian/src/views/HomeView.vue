<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { mediaTrackerService } from '@/api/mediaTrackerService.ts';
import type { TrackedMedia } from '@/types/person.type.ts';
import { Carousel, CarouselContent, CarouselItem, CarouselNext, CarouselPrevious } from '@/components/ui/carousel';
import { Card, CardContent } from '@/components/ui/card';

const allTrackedMedia = ref<TrackedMedia[]>([]);

onMounted(async () => {
  const res = await mediaTrackerService.getAll();
  allTrackedMedia.value = res.data ?? [];
});
</script>

<template>
  <div class="flex flex-col gap-6">
    <h1>Movie & TV Tracker</h1>
    <h2>Recent Activity</h2>
    <Carousel class="w-full">
      <CarouselContent>
        <CarouselItem v-for="item in allTrackedMedia" :key="item.id" class="basis-auto pl-3">
          <Card class="relative aspect-2/3 w-36 overflow-hidden p-0">
            <CardContent class="flex aspect-2/3 items-baseline justify-center p-0">
              <img
                :src="`https://image.tmdb.org/t/p/w342${item.posterPath}`"
                class="size-full object-cover"
                :alt="item.title"
                loading="lazy"
              />
              <!--              <span class="absolute bottom-0 inset-x-0 bg-black/60 text-white p-2 text-sm">{{ item.title }}</span>-->
            </CardContent>
          </Card>
        </CarouselItem>
      </CarouselContent>
      <CarouselPrevious class="left-2" />
      <CarouselNext class="right-2" />
    </Carousel>
    <p>Welcome to the home of Sebastian @ sebastian.hegardt.se :)</p>
  </div>
</template>

<style scoped></style>
