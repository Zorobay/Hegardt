<script setup lang="ts">
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu';
import { IconLayoutCards, IconMovie, IconSelector } from '@tabler/icons-vue';
import { SidebarMenu, SidebarMenuButton, SidebarMenuItem, useSidebar } from '@/components/ui/sidebar';

const isMobile = useSidebar();
</script>

<template>
  <SidebarMenu>
    <SidebarMenuItem href="#">
      <DropdownMenu>
        <DropdownMenuTrigger as-child>
          <SidebarMenuButton size="lg">
            <div
              class="flex aspect-square size-8 items-center justify-center rounded-sm bg-sidebar-primary text-sidebar-primary-foreground"
            >
              <IconLayoutCards class="size-4" />
            </div>
            <div class="grid flex-1 text-left text-sm leading-tight">
              <span class="truncate font-semibold">Sebastian</span>
              <span class="truncate text-xs">Projects</span>
            </div>
            <IconSelector class="ml-auto" />
          </SidebarMenuButton>
        </DropdownMenuTrigger>
        <DropdownMenuContent :side="isMobile ? 'bottom' : 'right'">
          <DropdownMenuLabel> Projects </DropdownMenuLabel>
          <DropdownMenuItem as-child>
            <RouterLink :to="{ name: 'TrackerHome' }">
              <IconMovie />
              <span>Media Tracker</span>
            </RouterLink>
          </DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </SidebarMenuItem>
  </SidebarMenu>
</template>

<style scoped></style>
