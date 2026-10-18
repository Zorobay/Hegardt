<script setup lang="ts">
import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover';
import { Button } from '@/components/ui/button';
import { IconCalendarStats } from '@tabler/icons-vue';
import { ref } from 'vue';
import { Calendar } from '@/components/ui/calendar';

const pickedDate = ref<Date | undefined>(undefined);
</script>

<template>
  <Popover>
    <PopoverTrigger as-child>
      <Button
        variant="outline"
        class="data-[empty=true]:text-muted-foreground justify-between font-normal"
        :data-empty="!pickedDate"
      >
        {{ pickedDate ? pickedDate : 'Pick a date' }} <IconCalendarStats />
      </Button>
    </PopoverTrigger>
    <PopoverContent>
      <Calendar />
    </PopoverContent>
  </Popover>
</template>

<style scoped></style>
