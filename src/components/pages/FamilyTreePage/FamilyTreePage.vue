<template>
  <div id="app">
    <div class="controls">
      <div>
        <label>Adjust width</label>
        <input max="100" min="0" type="range" v-model="settings.width"/>
      </div>
      <div>
        <label>Stroke color</label>
        <input type="color" v-model="settings.strokeColor"/>
      </div>
      <div>
        Selected: {{ selected }}
      </div>
    </div>
    <div :style="{width: settings.width + '%'}" class="svg-container">
      <svg id="svgId" preserveAspectRatio="xMinYMin meet" viewBox="0 0 960 600">
        <g class="node" v-bind:key="node.id" v-bind:style="node.style" v-for="(index, node) in nodes"
           v-on:click="select(index, node)">
          <circle v-bind:r="node.r" v-bind:style="{'fill': index == selected ? '#ff0000' : '#bfbfbf'}"></circle>
          <text v-bind:dx="node.textpos.x" v-bind:dy="node.textpos.y" v-bind:style="node.textStyle">{{ node.text }}</text>
        </g>
        <g class="link" v-bind:key="link.id" v-for="link in links"></g>


      </svg>
    </div>
  </div>
</template>

<script>
  import * as d3 from "d3";


  export default {
    name: "FamilyTreePage",
    data() {
      return {
        data: [{
          id: 1, name: "Sebastian", children: [{id: 2, name: "Anna", children: []},
            {id: 3, name: "Sören", children: []}]
        }],
        selected: null,
        settings: {
          strokeColor: "#29B5FF",
          width: 100
        }
      };
    },
    computed: {
      tree() {
        const root = d3.hierarchy(this.data);
        root.dx = 10;
        root.dy = this.settings.width / (root.height + 1);
        return d3.cluster().nodeSize([root.dx, root.dy])(root);
      },
      nodes: function () {
        var that = this;
        if (this.tree) {
          return this.tree.descendants().map(d => {
            let x = (200 + d.x) + "px";
            let y = parseInt(-1 * d.y + 30) + "px";
            return {
              id: d.id,
              r: 2.5,
              text: d.id,
              textpos: {
                x: d.children ? -8 : 8,
                y: 3
              },
              textStyle: {
                textAnchor: d.children ? "end" : "start"
              }
            };
          });
        }
      },
      links: function () {
        return this.tree.descendants().slice(1).map(function (d) {
          let x = d.x + 200, parent_x = d.parent.x + 200;
          let y = parseInt(-1 * d.y + 30);
          let parent_y = parseInt(-1 * d.parent.y + 30);
          return {
            id: d.id,
            d: "M" + x + "," + y + "L" + parent_x + "," + parent_y,
          };
        });
      }

    },
    methods: {
      select: function (index, node) {
        this.selected = index;
      }
    }
  }
</script>

<style scoped>
  #chart div {
    display: inline-block;
    background: #4285F4;
    width: 20px;
    margin-right: 3px;
  }
</style>
