<template>
  <g>
    <rect
      :class="personClasses"
      :height="nodeHeight" :width="nodeWidth"
      :transform="rectCenterTransform"
      :x="x"
      :y="y"
      rx="10" ry="10"/>
    <object type="image/svg+xml" data="icons/man-with-mustache-avatar.svg">
      Man with mustasche
    </object>
    <slot/>
    <router-link :to="{name: 'PersonalFile', params: {id: person.id}}">
      <foreignObject
        :height="textBoxHeight"
        :transform="textCenterTransform" :width="textBoxWidth"
        :x="x"
        :y="y">
        <p class="person-node-name">{{ person.full_name }}</p>
      </foreignObject>
    </router-link>
  </g>
</template>

<script>
  import sex from '@/common/enums/sex';
  import NodeMixin from '@/components/pages/PersonalFilePage/FamilyTree/mixins/NodeMixin';

  export default {
    name: 'PersonNode',
    props: ['person', 'current'],
    mixins: [NodeMixin],
    data() {
      return {
        isCurrent: !!this.current,
        sex: this.person.sex === sex.UNKNOWN ? null : this.person.sex,
      };
    },
    computed: {
      personClasses() {
        const sex = this.person.sex;
        return `node person-node ${sex.toLowerCase()} ${this.isCurrent ? 'self' : ''}`;
      },
    },
  };
</script>

<style scoped>
.name {
  color: #19232d;
}
</style>
