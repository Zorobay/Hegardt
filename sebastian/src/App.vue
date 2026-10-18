<script setup lang="ts">
import { RouterView } from 'vue-router';
import { SidebarInset, SidebarProvider, SidebarTrigger } from '@/components/ui/sidebar';
import AppSidebar from '@/components/sidebar/AppSidebar.vue';
import { Button } from '@/components/ui/button';
import { IconPlus } from '@tabler/icons-vue';
import TrackMediaDrawer from '@/components/TrackMediaDrawer.vue';
import { ref } from 'vue';

const trackDrawerOpen = ref<boolean>(false);

function onAddButtonClick(): void {}
</script>

<template>
  <SidebarProvider>
    <AppSidebar />
    <SidebarInset class="min-w-0">
      <header>
        <SidebarTrigger />
      </header>
      <main class="flex flex-1 min-w-0 flex-col p-6">
        <RouterView />
      </main>
    </SidebarInset>
  </SidebarProvider>
  <Button
    size="icon"
    class="md:hidden absolute bottom-4 right-4 size-14 rounded-full shadow-lg"
    @click="trackDrawerOpen = true"
  >
    <IconPlus class="size-8" />
  </Button>
  <TrackMediaDrawer :open="trackDrawerOpen" />
</template>

<style scoped></style>
