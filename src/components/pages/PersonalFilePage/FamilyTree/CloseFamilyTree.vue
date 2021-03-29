<template>
  <div id="close-family-tree">
  </div>
</template>

<script>
  import * as d3 from 'd3';

  export default {
    name: 'CloseFamilyTree',
    props: ['person'],
    data() {
      return {
        width: 750,
        height: 600,
        tree_width: 700,
        tree_height: 400,
        margin: {
          top: 50,
          right: 50,
          left: 50,
          bottom: 50,
        },
        TYPE: {'ROOT': 1, 'PARENT': 2, 'CHILD': 3},
      };
    },
    watch: {
      person: {
        deep: true,
        handler(n, o) {
          this.drawTree();
        },
      },
    },
    methods: {
      sizeFromType(type) {
        switch (type) {
        case this.TYPE.PARENT:
          return {width: 100, height: 100};
        case this.TYPE.ROOT:
          return {width: 0, height: 0};
        default:
          return {width: 100, height: 100};
        }
      },
      constructHierarchy(fullName, children, type) {
        if (!(children instanceof Array)) {
          children = [children];
        }

        children = children.filter(c => !!c);
        for (let i = 0; i < children.length; i++) {
          const child = children[i];
          children[i] = this.constructHierarchy(child.full_name, []);
        }

        const {width, height} = this.sizeFromType(type);

        return {
          full_name: fullName, width: width, height: height, type: type,
          name: fullName,
          children: children,
        };
      },
      getNodes() {
        const root = this.constructHierarchy('invisible root', [this.person.father, this.person.mother], this.TYPE.ROOT);
        root.children.forEach(child => child.children = [this.constructHierarchy(this.person.full_name, this.person.children)]);
        return root;
      },
      createSVG() {
        this.clearSVG();
        return d3
          .select('#close-family-tree')
          .append('svg')
          .attr('width', this.width)
          .attr('height', this.height)
          .append('g')
          .style(
            'transform',
            `translate(${this.margin.left}px, ${this.margin.top}px)`,
          );
      },
      clearSVG() {
        d3.select('#close-family-tree svg').remove();
      },
      drawTree() {
        // Compute the layout.
        const svg = this.createSVG();
        const root = d3.hierarchy(this.getNodes());

        const treeLayout = d3.tree().size([this.tree_width, this.tree_height]);
        const tree = treeLayout(root);
        const nodes = tree.descendants();
        const links = tree.links();
        console.log(tree.descendants());
        console.log(tree.links());

        const circles = svg.append('g').attr('id', 'nodes').selectAll('circle').data(nodes);
        circles.enter().append('rect')
          .attr('x', d => d.x)
          .attr('y', d => d.y)
          .attr('width', d => d.data.width)
          .attr('height', d => d.data.height);

        const texts = svg.append('g').attr('class', 'labels').selectAll('text').data(nodes);
        texts.enter().append('text').attr('fill', 'red').attr('text-anchor', 'middle')
          .style('visibility', d => {
            if (d.data.type === this.TYPE.ROOT) {
              return 'hidden';
            }
            return 'visible';
          })
          .attr('x', d => d.x)
          .attr('y', d => d.y)
          .text(d => {
            return d.data.name;
          });

        const edges = svg.append('g').attr('id', 'edges').selectAll('edge').data(links);
        edges.enter().append('path')
          .style('visibility', d => {
            if (d.source.data.type === this.TYPE.ROOT) {
              return 'hidden';
            }
            return 'visible';
          })
          .attr('class', 'edge')
          .attr('d', d => {
            return `M ${d.source.x} ${d.source.y + d.source.height} L ${d.target.x} ${d.target.y}`;
          });
      },
    },
  };
</script>

<style scoped>

>>> path {
  fill: none;
  stroke: red;
}

</style>
