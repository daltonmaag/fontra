import { getRemoteProxy } from "../src/remote.js";
import VarPath from "./var-path.js";
import { VarGlyph } from "./var-glyph.js";
import { CanvasController } from "../src/canvas-controller.js";
import {
  SceneGraph,
  MiscPathItem,
  PathHandlesItem,
  PathPathItem,
  PathNodesItem,
  HoverLayer,
  pointInRect,
  centeredRect,
} from "../src/scene-graph.js";


export class AppController {
  constructor() {
    const canvas = document.querySelector("#edit-canvas");

    this.remote = getRemoteProxy("ws://localhost:8001/", async () => await this.initGlyphNames());
    this.canvasController = new CanvasController(canvas);

    this._glyphsCache = {};
    this.varLocation = {};

    this.path = new VarPath();

    const scene = new SceneGraph();
    this.componentsLayer = new MiscPathItem([]);
    scene.push(this.componentsLayer);
    scene.push(new PathHandlesItem(this.path));
    scene.push(new PathPathItem(this.path));
    scene.push(new PathNodesItem(this.path));
    this.hoverLayer = new HoverLayer(this.path)
    scene.push(this.hoverLayer);
    this.canvasController.scene = scene;

    this.canvasController.canvas.addEventListener("mousemove", event => this.handleMouseMove(event));

    window.sliderChanged = (value, axisTag) => {
      this.setAxisValue(value, axisTag);
    };
  }

  async initGlyphNames() {
    const glyphNamesMenu = document.querySelector("#glyph-select");
    const glyphNames = await this.remote.getGlyphNames();
    for (const glyphName of glyphNames) {
      const option = document.createElement("option");
      option.setAttribute("value", glyphName);
      option.append(glyphName);
      glyphNamesMenu.appendChild(option);
    }
  }

  async glyphNameChangedCallback(glyphName) {
    const didSetGlyph = await this.setSelectedGlyph(glyphName);
    if (!didSetGlyph) {
      return;
    }
    // Rebuild axis sliders
    const axisSliders = document.querySelector("#axis-sliders");
    axisSliders.innerHTML = "";  // Delete previous sliders
    for (const axis of this.getAxisInfo()) {
      const label = document.createElement("label");
      const slider = document.createElement("input");
      label.setAttribute("class", "slider-label");
      slider.setAttribute("type", "range");
      slider.setAttribute("step", "any");
      slider.setAttribute("class", "slider");
      slider.setAttribute("min", axis.minValue);
      slider.setAttribute("max", axis.maxValue);
      slider.setAttribute("value", axis.defaultValue);
      slider.setAttribute("oninput", `sliderChanged(this.value, "${axis.name}")`);
      label.appendChild(slider);
      label.append(axis.name);
      axisSliders.appendChild(label);
    }
  }

  handleMouseMove(event) {
    const point = this.canvasController.localPoint(event);
    const selRect = centeredRect(
      point.x, point.y,
      this.canvasController.drawingParameters.nodeSize / this.canvasController.magnification,
    );
    const currentHoverSelection = this.hoverLayer.hoverSelection;
    this.hoverLayer.hoverSelection = null;
    let index = 0;
    for (const point of this.path.iterPoints()) {
      if (pointInRect(point, selRect)) {
        this.hoverLayer.hoverSelection = index;
        break;
      }
      index++;
    }
    if (this.hoverLayer.hoverSelection !== currentHoverSelection) {
      this.canvasController.setNeedsUpdate();
    }
  }

  async setSelectedGlyph(glyphName) {
    const glyph = await this.getRemoteGlyph(glyphName);
    if (glyph === null) {
      return false;
    }
    this.hoverLayer.hoverSelection = null;
    this.glyph = glyph;
    this.varLocation = {};
    this.axisMapping = _makeAxisMapping(this.glyph.axes);
    await this._instantiateGlyph();
    this.canvasController.setNeedsUpdate();
    return true;
  }

  *getAxisInfo() {
    const done = {};
    for (const axis of this.glyph.axes) {
      const baseName = _getAxisBaseName(axis.name);
      if (done[baseName]) {
        continue;
      }
      done[baseName] = true;
      const axisInfo = {...axis};
      axisInfo.name = baseName;
      yield axisInfo;
    }
  }

  async setAxisValue(value, axisName) {
    for (const realAxisName of this.axisMapping[axisName]) {
      this.varLocation[realAxisName] = value;
    }
    await this._instantiateGlyph();
    this.canvasController.setNeedsUpdate();
  }

  async getRemoteGlyph(glyphName) {
    let glyph = this._glyphsCache[glyphName];
    if (glyph === undefined) {
      glyph = await this.remote.getGlyph(glyphName);
      if (glyph !== null) {
        glyph = VarGlyph.fromObject(glyph);
      }
      this._glyphsCache[glyphName] = glyph;
    }
    return this._glyphsCache[glyphName];
  }

  async _instantiateGlyph() {
    const inst = this.glyph.instantiate(this.varLocation);
    this.path.coordinates = inst.path.coordinates;
    this.path.pointTypes = inst.path.pointTypes;
    this.path.contours = inst.path.contours;

    let compoPaths2d = [];
    if (inst.components !== undefined) {
      const compoPaths = await inst.getComponentPaths(
        async glyphName => await this.getRemoteGlyph(glyphName),
        this.varLocation,
      );
      compoPaths2d = compoPaths.map(path => {
        const path2d = new Path2D();
        path.drawToPath(path2d);
        return path2d;
      });
    }
    this.componentsLayer.paths = compoPaths2d;
  }

}


function _makeAxisMapping(axes) {
  const axisMapping = {};
  for (const axis of axes) {
    const baseName = _getAxisBaseName(axis.name);
    if (axisMapping[baseName] === undefined) {
      axisMapping[baseName] = [];
    }
    axisMapping[baseName].push(axis.name);
  }
  return axisMapping;
}


function _getAxisBaseName(axisName) {
  const asterixPos = axisName.indexOf("*");
  if (asterixPos > 0) {
    return axisName.slice(0, asterixPos);
  }
  return axisName;
}
