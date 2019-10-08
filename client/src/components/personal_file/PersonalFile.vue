<template>
  <div>
    <h3>Ansedel</h3>
    <h4>Person Name</h4>

    <div class="row">
      <div class="col-md-4">
        <p class="text-center">Född&nbsp</p>
        <WellCell></WellCell>
      </div>
      <div class="col-md-4">
        <p class="text-center">Död&nbsp</p>
        <WellCell></WellCell>

      </div>
      <div class="col-md-4">
        <p class="text-center">Begravd&nbsp</p>
        <WellCell></WellCell>

      </div>
    </div>
  </div>
</template>

<script>
  import WellCell from "./WellCell";

  export default {
    name: "PersonalFile",
    components: {WellCell}
  }
</script>

<style scoped>

</style>
