<script setup lang="ts">
import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from '@/components/ui/sidebar';
import { IconHome } from '@tabler/icons-vue';
import AppProjectSwitcher from '@/components/sidebar/AppProjectSwitcher.vue';
</script>

<template>
  <Sidebar collapsible="icon">
    <SidebarHeader>
      <AppProjectSwitcher />
    </SidebarHeader>

    <SidebarContent>
      <SidebarGroup>
        <SidebarGroupLabel>Movie & TV Tracker</SidebarGroupLabel>
        <SidebarGroupContent>
          <SidebarMenu>
            <SidebarMenuItem>
              <SidebarMenuButton>Hej</SidebarMenuButton>
            </SidebarMenuItem>
            <SidebarMenuItem href="#">
              <SidebarMenuButton as-child>
                <RouterLink :to="{ name: 'TrackerHome' }">
                  <IconHome class="size-8" />
                  <span>Home</span>
                </RouterLink>
              </SidebarMenuButton>
            </SidebarMenuItem>
          </SidebarMenu>
        </SidebarGroupContent>
      </SidebarGroup>
    </SidebarContent>
  </Sidebar>
</template>

<style scoped></style>
