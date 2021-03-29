<template>
  <div class="person-info-sidebar">
    <p>Född {{ person.age }} år sedan</p>

    <info-sidebar-row :heading-note="elvis(person, 'birth.notes')"
                      :info="prettyDate(elvis(person, 'birth.date'))"
                      :info-note="elvis(person, 'birth.location.notes')"
                      :sub-info="formatLocation(elvis(person, 'birth.location'))"
                      heading-key="ppage.birth.heading"
                      id-prefix="birth"/>
    <info-sidebar-row :heading-note="elvis(person, 'death.notes')"
                      :info="prettyDate(elvis(person, 'death.date'))"
                      :info-note="elvis(person, 'death.location.notes')"
                      :sub-info="formatLocation(elvis(person, 'death.location'))"
                      heading-key="ppage.death.heading"
                      id-prefix="death"/>
    <info-sidebar-row :heading-note="elvis(person, 'burial.notes')"
                      :info="prettyDate(elvis(person, 'burial.date'))"
                      :info-note="elvis(person, 'burial.location.notes')"
                      :sub-info="formatLocation(elvis(person, 'burial.location'))"
                      heading-key="ppage.burial.heading"
                      id-prefix="burial"/>
    <info-sidebar-row v-if="elvis(person, 'notes')"
                      :info="elvis(person, 'notes')"
                      heading-key="ppage.note.heading"
                      id-prefix="notes"/>
  </div>
</template>

<script>
  import InfoSidebarRow from '@/components/pages/PersonalFilePage/InfoSideBar/InfoSidebarRow';

  export default {
    name: 'InfoSideBar',
    components: {InfoSidebarRow},
    props: ['person'],
  };
</script>

<style scoped type="scss">
.person-info-sidebar {
  background-color: #f0f0f0;
  border-radius: 15px;
}
</style>
