<template>
<div class="accordion">
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button" type="button" data-bs-toggle="collapse" :data-bs-target="'#'+id" aria-expanded="true" aria-controls="collapseOne">
        {{heading}}
      </button>
    </h2>
    <div :id="id" class="accordion-collapse collapse show" data-bs-parent="#accordionExample">
      <div class="accordion-body">
        <slot></slot>
      </div>
    </div>
  </div>
</div>
</template>

<script setup>
import {useId} from 'vue';
const props = defineProps(['heading']);
const id = useId();
</script>

<style scoped>
.accordion-button {
  font-weight: bold;
}
</style>
