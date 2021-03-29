
export default {
  props: ['x', 'y', 'width', 'height'],
  data() {
    return {
      nodeWidth: this.width ? this.width : 150,
      nodeHeight: this.height ? this.height : 80,
      innerMargin: 5,
    };
  },
  methods: {
    getBottomEdgePos() {
      return {
        x: this.x,
        y: this.y + this.nodeHeight / 2,
      };
    },
    getTopEdgePos() {
      return {
        x: this.x,
        y: this.y - this.nodeHeight / 2,
      };
    },
    getLeftEdgePos() {
      return {
        x: this.x - this.nodeWidth / 2,
        y: this.y,
      };
    },
    getRightEdgePos() {
      return {
        x: this.x + this.nodeWidth / 2,
        y: this.y,
      };
    },
  },
  computed: {
    textBoxWidth() {
      return this.nodeWidth - this.innerMargin;
    },
    textBoxHeight() {
      return this.nodeHeight - this.innerMargin;
    },
    rectCenterTransform() {
      return `translate(-${this.nodeWidth / 2}, -${this.nodeHeight / 2})`;
    },
    textCenterTransform() {
      return `translate(-${this.textBoxWidth / 2}, -${this.textBoxHeight / 2})`;
    },
  },
};
