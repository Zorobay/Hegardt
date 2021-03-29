<template>
  <div id="svg-container" class="svg-container">
    <p>viewBox: {{ viewBoxPretty }}</p>
    <p>mousePos: {{mousePos }}</p>

    <svg viewBox="0 0 1000 1000" id="svg-canvas-outer">
      <svg :viewBox="viewBox" id="svg-canvas-inner">
        <slot></slot>
      </svg>

      <g transform="translate(30,30)">
        <g class="svg-button btn btn-primary" @click="zoomIn">
          <circle class="button" cx="0" cy="0" r="20"/>
          <path d="M 0 10 H 10 V 0 H 20 V 10 H 30 V 20 H 20 V 30 H 10 V 20 H 0 Z" fill="white" transform="translate(-15,-15)"/>
        </g>
        <g class="svg-button" transform="translate(-25, 25)" @click="resetView">
          <rect width="50" height="30" fill="black"/>
          <text transform="translate(25, 15)" fill="white" dominant-baseline="middle" text-anchor="middle">RESET</text>
        </g>
        <g class="svg-button" transform="translate(0, 80)" @click="zoomOut">
          <circle class="button" cx="0" cy="0" r="20"  fill="black"/>
          <path d="M0 10 H 30 V20 H0 Z" fill="white" transform="translate(-15,-15)"/>
        </g>
      </g>

    </svg>
  </div>
</template>

<script>
  export default {
    name: 'SvgContainer',
    props: ['width', 'height'],
    data() {
      return {
        showControls: false,
        controlsWidthBase: 60,
        controlsHeightBase: 120,
        viewBoxWidth: this.width,
        viewBoxHeight: this.height,
        viewBoxScale: 1.0,
        viewBoxX: 0,
        viewBoxY: 0,
        startPoint: null,
        endPanX: 0,
        endPanY: 0,
        currentlyPanning: false,
        svgElement: undefined,
        mousePos: '',
      };
    },
    computed: {
      viewBox() {
        return `${this.viewBoxX} ${this.viewBoxY} ${this.scaledViewBoxWidth} ${this.scaledViewBoxHeight}`;
      },
      viewBoxPretty() {
        return `${this.viewBoxX.toFixed(2)} ${this.viewBoxY.toFixed(2)} ${this.scaledViewBoxWidth.toFixed(2)} ${this.scaledViewBoxHeight.toFixed(2)}`;
      },
      controlsWidth() {
        return this.controlsWidthBase * this.viewBoxScale;
      },
      controlsHeight() {
        return this.controlsHeightBase * this.viewBoxScale;
      },
      scaledViewBoxWidth() {
        return this.viewBoxWidth * this.viewBoxScale;
      },
      scaledViewBoxHeight() {
        return this.viewBoxHeight * this.viewBoxScale;
      },
    },
    methods: {
      fromPercentagePosX(perc) {
        return (perc / 100) * this.scaledViewBoxWidth;
      },
      fromPercentagePosY(perc) {
        return (perc / 100) * this.scaledViewBoxHeight;
      },
      onMouseOver() {
        this.showControls = true;
      },
      onMouseLeave() {
        this.showControls = false;
      },
      zoomIn() {
        this.viewBoxScale *= 0.8;
      },
      zoomOut() {
        this.viewBoxScale /= 0.8;
      },
      resetView() {
        this.viewBoxScale = 1.0;
        this.viewBoxX = 0;
        this.viewBoxY = 0;
      },
      onScroll(event) {
        event.preventDefault();
        const normalizedDelta = event.wheelDelta / 120;
        normalizedDelta < 0 ? this.zoomOut() : this.zoomIn();
      },
      bindEvents() {
        this.svgElement = document.getElementById('svg-canvas-inner');
        const container = document.getElementById('svg-container');
        container.addEventListener('mousedown', this.startPan);
        container.addEventListener('mousemove', this.pan);
        container.addEventListener('mouseup', this.endPan);
        container.addEventListener('mouseleave', this.endPan);
        container.addEventListener('wheel', this.onScroll);
      },
      startPan(event) {
        this.currentlyPanning = true;
        this.startPoint = this.getMouseSVGPosition(event);
      },
      pan(event) {
        const panCoord = this.getMouseSVGPosition(event);

        if (this.currentlyPanning) {
          event.preventDefault();
          this.viewBoxX -= panCoord.x - this.startPoint.x;
          this.viewBoxY -= panCoord.y - this.startPoint.y;
        }

        this.mousePos = `${panCoord.x.toFixed(2)},${panCoord.y.toFixed(2)}`;
      },
      endPan(event) {
        this.currentlyPanning = false;
        this.startPoint = null;
      },
      getMouseSVGPosition(event) {
        const invertedCTM = this.svgElement.getScreenCTM().inverse();
        const point = this.svgElement.createSVGPoint();
        point.x = event.clientX;
        point.y = event.clientY;
        return point.matrixTransform(invertedCTM);
      },
    },
    mounted() {
      this.bindEvents();
    },
  };
</script>

<style scoped>

</style>
