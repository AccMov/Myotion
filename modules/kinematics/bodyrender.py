from math import pi

from PySide6.QtWidgets import QWidget
from OpenGL.GL import *

from .camera import Camera
from .items import AxesItem, GridItem, PointItem
from .base import Base
from .movmentrig import MovementRig
from .object3d import Object3D
from .renderer import Renderer


class BodyRender(Base):
    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.model = None
        self.point = None
        self.playing = False

    def initializeGL(self) -> None:
        super().initializeGL()
        self.currentFrame = 0
        self.renderer = Renderer(self)
        self.scene = Object3D()
        self.camera = Camera(aspectRatio=1, far=50000)
        self.camera.setPosition([0, 2000, 3000])
        self.camera.lookAt([0, 0, 0])
        self.rig = MovementRig(unitsPerSecond=100)
        self.rig.add(self.camera)

        axes = AxesItem(axisLength=100)
        grid = GridItem(size=5000, gridColor=[1, 1, 1], centerColor=[1, 1, 0])
        grid.rotateX(-pi / 2)

        self.scene.add(axes)
        self.scene.add(grid)

    def paintGL(self) -> None:
        super().paintGL()
        if self.point in self.scene.children:
            self.scene.remove(self.point)
        self.point = self.getFrame()
        self.scene.add(self.point)
        self.renderer.render(self.scene, self.camera)
        self.rig.update(self.input, self.deltaTime)

    def getFrame(self):
        cf = []
        for joint in self.model.realpoints:
            cf.append(
                [
                    self.model.realpoints[joint][self.currentFrame].xyz[0],
                    self.model.realpoints[joint][self.currentFrame].xyz[2],
                    self.model.realpoints[joint][self.currentFrame].xyz[1],
                ]
            )
        return PointItem(cf)

    def setModel(self, model):
        self.model = model
        self.currentFrame = 0

    def setFrame(self, frame):
        self.currentFrame = frame
    
    def play(self):
        self.playing = not self.playing
