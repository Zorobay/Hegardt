<template>
  <div>
    <h6 v-if="person">
      <router-link
        :to="{name: 'PersonalFile', params: {id: person._id}}">{{person.full_name}}
      </router-link>
      <span class="badge badge-info">{{formatDate(elvis(person, 'birth.date'))}}</span>
    </h6>
    <h6 v-else>?</h6>
  </div>
</template>

<script>
  export default {
    name: 'NameLink',
    props: ['person'],
  };
</script>

<style scoped>

</style>
