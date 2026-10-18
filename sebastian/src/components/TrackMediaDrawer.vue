<script setup lang="ts">
import {
  Drawer,
  DrawerContent,
  DrawerDescription,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
} from '@/components/ui/drawer';
import { Button } from '@/components/ui/button';
import { Field, FieldGroup, FieldLabel } from '@/components/ui/field';
import { Input } from '@/components/ui/input';
import { ref } from 'vue';
import StarRatingInput from '@/components/StarRatingInput.vue';
import DatePicker from '@/components/DatePicker.vue';
import TimePicker from '@/components/TimePicker.vue';

const open = defineModel<boolean>('open', { default: false });

const rating = ref<number>(0);
const searchValue = ref<string>('');

function onSubmit(): void {}
</script>

<template>
  <Drawer v-model:open="open" class="lg:w-70">
    <DrawerContent>
      <DrawerHeader>
        <DrawerTitle>Track new media</DrawerTitle>
        <DrawerDescription>Search for a Movie or TV show to track</DrawerDescription>
      </DrawerHeader>

      <div class="px-4">
        <form @submit.prevent="onSubmit">
          <FieldGroup>
            <Field>
              <FieldLabel> Search </FieldLabel>
              <Input v-model="searchValue" placeholder="Search TMDB..."></Input>
            </Field>
            <Field>
              <FieldLabel> Rating </FieldLabel>
              <StarRatingInput></StarRatingInput>
            </Field>
            <FieldGroup class="grid grid-cols-3">
              <Field class="col-span-2">
                <FieldLabel> Date </FieldLabel>
                <DatePicker />
              </Field>
              <Field>
                <FieldLabel> Time </FieldLabel>
                <TimePicker />
              </Field>
            </FieldGroup>
          </FieldGroup>
        </form>
      </div>

      <DrawerFooter>
        <Button>Save</Button>
      </DrawerFooter>
    </DrawerContent></Drawer
  >
</template>

<style scoped></style>
