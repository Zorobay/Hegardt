<template>
  <div class="person-info-sidebar">
    <p>Född {{ person.age }} år sedan</p>

    <date-location :person="person" prop="birth"/>
    <date-location :person="person" prop="death"/>
    <date-location :person="person" prop="burial"/>

    <b-row v-if="elvis(person, 'notes')">
      <b-col cols="4">
        <p class="heading">{{ Text(`ppage.note`) }}</p>
      </b-col>
      <b-col cols="8">
        <p>{{ this.person.notes }}</p>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import DateLocation from '@/components/pages/PersonalFilePage/InfoSideBar/DateLocation';

export default {
  name: 'InfoSideBar',
  components: {DateLocation},
  props: ['person'],
};
</script>

<style scoped type="scss">

</style>
