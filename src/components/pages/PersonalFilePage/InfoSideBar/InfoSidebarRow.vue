<template>
  <b-row>
    <b-col class="heading-col" cols="4">
      <p :id="headingId" :class="headingClass">{{ Text(headingKey) }}</p>
    </b-col>

    <b-col cols="8">
      <template v-if="info || subInfo">
        <div class="info-container">
          <p v-if="info.length < maxInfoContentLength" :id="infoId" :class="infoClass">
            {{ info }}
          </p>
          <div v-else>
            <collapsible-text :id-prefix="idPrefix" :text="info"/>
          </div>
        </div>
        <p class="sub-info">{{ subInfo }}</p>
      </template>
      <template v-else>
        <p class="info">...</p>
      </template>
    </b-col>

    <b-tooltip v-if="headingNote" :target="headingId">{{ headingNote }}</b-tooltip>
    <b-tooltip v-if="infoNote" :target="infoId">{{ infoNote }}</b-tooltip>
  </b-row>

</template>

<script>

  import CollapsibleText from '@/components/common/CollapsibleText';

  export default {
    name: 'InfoSidebarRow',
    components: {CollapsibleText},
    props: ['idPrefix', 'headingKey', 'info', 'subInfo', 'headingNote', 'infoNote'],
    data() {
      return {
        maxInfoContentLength: 300,
        headingId: 'heading-' + this.idPrefix,
        infoId: 'info-' + this.idPrefix,
        headingClass: 'heading' + (this.headingNote ? ' hoverable' : ''),
        infoClass: 'info' + (this.infoNote ? ' hoverable' : ''),
      };
    },
  };


</script>

<style scoped type="scss">

.heading {
  font-size: 13pt;
  color: #282b09;
  font-weight: bold;
  text-align: right;
}

.info {
  font-size: 12pt;
  margin-bottom: 5px;
  line-height: 1.2;
}

.sub-info {
  font-size: 11pt;
  font-style: italic;
}
</style>
