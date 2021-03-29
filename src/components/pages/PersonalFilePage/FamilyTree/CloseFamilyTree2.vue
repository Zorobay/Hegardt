<template>
  <svg-container :height="canvas_height" :width="canvas_width">

    <!-- Mother and edge -->
    <g v-if="mother">
      <person-node :id="motherId" :height="node.height" :person="mother"
                   :width="node.width" :x="motherPositionX" :y="fromPercentagePosY(parentYPerc)"/>
      <edge :end-node-id="personId" :start-node-id="motherId" end-anchor="top" start-anchor="bottom"/>
    </g>

    <!-- Father and edge -->
    <g v-if="father">
      <person-node :id="fatherId" :height="node.height" :person="father"
                   :width="node.width" :x="fatherPositionX" :y="fromPercentagePosY(parentYPerc)"/>
      <edge :end-node-id="personId" :start-node-id="fatherId" end-anchor="top" start-anchor="bottom"/>
    </g>

    <!-- Current Person and edge to first marriage-->
    <person-node :id="personId" :height="node.height" :person="person" :width="node.width"
                 :x="fromPercentagePosX(50)" :y="fromPercentagePosY(50)" current="true"/>
    <edge v-if="spouses.length > 0" :end-node-id="marriageId(spouses[0])" :start-node-id="personId"
          end-anchor="right" start-anchor="bottom"/>


    <!-- Spouses, marriages and children-->
    <g v-for="(spouse, spouseIndex) in spouses" :key="spouseId(spouse)">
      <person-node :id="spouseId(spouse)" :height="node.height" :person="spouse" :width="node.width"
                   :x="spousePositionX(spouseIndex)" :y="fromPercentagePosY(50)"/>
      <marriage-node :id="marriageId(spouse)" :height="marriageNode.height"
                     :marriage="findMarriageFromSpouse(spouse)" :width="marriageNode.width"
                     :x="marriagePositionX(spouseIndex)" :y="fromPercentagePosY(62.5)"/>
      <edge :end-node-id="marriageId(spouse)" :start-node-id="spouseId(spouse)" end-anchor="top" start-anchor="bottom"/>
      <edge v-if="spouseIndex > 0" :end-node-id="marriageId(spouse)" :start-node-id="marriageId(spouses[spouseIndex-1])"
            end-anchor="right" start-anchor="left"/>

      <!-- Children and edges -->
      <g v-for="(child, childIndex) in findChildrenFromSpouse(spouse)" :key="child.id">
        <person-node :id="childId(child)" :key="'box-' + child.id"
                     :height="node.height" :person="child" :width="node.width" :x="childPositionX(spouseIndex)"
                     :y="childPositionY(childIndex)"/>
        <edge :end-node-id="childId(child)" :start-node-id="marriageId(spouse)" end-anchor="left" start-anchor="bottom"/>
      </g>
    </g>

    <!-- Grid -->
    <line :x1="500" :x2="500" stroke-dasharray="4" style="stroke-width: 1; stroke: black; opacity: 30%;" y1="0%"
          y2="100%"/>
    <line stroke-dasharray="4" style="stroke-width: 1; stroke: black; opacity: 30%" x1="0%" x2="100%" y1="50%"
          y2="50%"/>

  </svg-container>
</template>

<script>

  import PersonNode from '@/components/pages/PersonalFilePage/FamilyTree/PersonNode';
  import Edge from '@/components/pages/PersonalFilePage/FamilyTree/Edge';
  import SvgContainer from '@/components/common/svg/SvgContainer';
  import MarriageNode from '@/components/pages/PersonalFilePage/FamilyTree/MarriageNode';

  export default {
    name: 'CloseFamilyTree2',
    components: {MarriageNode, SvgContainer, PersonNode, Edge},
    props: ['person', 'mother', 'father', 'children', 'spouses', 'marriages'],
    data: function() {
      return {
        canvas_width: 1000,
        canvas_height: 1000,
        showControls: false,
        parentYPerc: 25,
        selfYPerc: 50,
        childrenYPerc: 75,
        numChildren: this.children ? this.children.length : 0,
        numSpouses: this.spouses ? this.spouses.length : 0,
        node: {
          width: 200,
          height: 100,
          horizontalMargin: 70,
          verticalMargin: 30,
        },
        marriageNode: {
          width: 100,
          height: 70,
        },
      };
    },
    computed: {
      motherId() {
        return `mother-${this.mother.id}`;
      },
      fatherId() {
        return `father-${this.father.id}`;
      },
      personId() {
        return `person-${this.person.id}`;
      },
      motherPositionX() {
        return this.fromPercentagePosX(50) - (this.node.horizontalMargin + this.node.width) / 2;
      },
      fatherPositionX() {
        return this.motherPositionX + this.node.width + this.node.horizontalMargin;
      },
    },
    methods: {
      childId(child) {
        return `child-${child.id}`;
      },
      spouseId(spouse) {
        return `spouse-${spouse.id}`;
      },
      marriageId(marriage) {
        return `marriage-${marriage.id}`;
      },
      edgeId(startPerson, endPerson) {
        return `edge-${startPerson.id} -> ${endPerson.id}`;
      },
      findMarriageFromSpouse(spouse) {
        const marriages = this.person.spouses;
        const marriage = marriages.filter(m => m._id === spouse.id);
        return marriage.length >= 1 ? marriage[0] : null;
      },
      findChildrenFromSpouse(spouse) {
        return this.children.filter(c => c.father === spouse.id || c.mother === spouse.id);
      },
      fromPercentagePosX(perc) {
        return (perc / 100) * this.canvas_width;
      },
      fromPercentagePosY(perc) {
        return (perc / 100) * this.canvas_height;
      },
      childPositionX(index) {
        // const delta = Math.round(100 / (this.numChildren + 1));
        // const perc = (index + 1) * delta;
        // return this.fromPercentagePosX(perc);
        return this.spousePositionX(index) + (this.node.width / 2) + (this.node.horizontalMargin / 2);
      },
      childPositionY(index) {
        return this.fromPercentagePosY(this.childrenYPerc) + (this.node.height + this.node.verticalMargin) * index;
      },
      spousePositionX(index) {
        return this.fromPercentagePosX(50) - (this.node.width + this.node.horizontalMargin) * (index + 1);
      },
      marriagePositionX(index) {
        // return this.fromPercentagePosX(50) - ((this.node.width + this.node.horizontalMargin) * (index + 1) * 0.5);
        return this.spousePositionX(index);
      },
      onMouseOver() {
        this.showControls = true;
      },
      onMouseLeave() {
        this.showControls = false;
      },
    },
  };
</script>

<style scoped>

</style>
