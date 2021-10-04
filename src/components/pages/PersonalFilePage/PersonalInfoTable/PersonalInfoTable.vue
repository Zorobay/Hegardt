<template>
  <div>
    <h3>Milestones</h3>
    <table class="table">
      <tr>
        <th>Milestone</th>
        <th>Date</th>
        <th>Location</th>
        <th>Notes</th>
      </tr>
      <tr v-for="milestone in ['birth', 'death', 'burial']" :key="milestone">
        <td>{{ toName(milestone) }}</td>
        <td>{{ formatDate(elvis(person, `${milestone}.date`)) }}</td>
        <td>{{ formatLocation(elvis(person, `${milestone}.location`))}}</td>
        <td>{{ elvis(person, `${milestone}.notes`)}}</td>
      </tr>
    </table>

    <h3>Occupations</h3>
    <table class="table">
      <tr>
        <th>Description</th>
        <th>Date</th>
        <th>Location</th>
      </tr>
      <tr v-for="occupation in occupations" :key="occupation.id">
        <td>{{elvis(occupation, 'notes')}}</td>
        <td>{{formatDate(elvis(occupation, 'date'))}}</td>
        <td>{{formatLocation(elvis(occupation, 'location'))}}</td>
      </tr>
    </table>

    <h3>References</h3>
    <table class="table">
      <tr>
        <th>Reference</th>
      </tr>
      <tr v-for="reference in references" :key="reference.id">
        <td>{{reference.content}}</td>
      </tr>
    </table>
  </div>
</template>

<script>

  export default {
    name: 'PersonalInfoTable',
    props: ['person'],
    computed: {
      references() {
        return this.addIds(this.elvis(this.person, 'references'));
      },
      occupations() {
        return this.addIds(this.elvis(this.person, 'occupations'));
      },
    },
  };
</script>

<style scoped>

</style>
