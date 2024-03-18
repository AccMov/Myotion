from math import pi
from modules.kinematics.axesitem import AxesItem
from modules.kinematics.base import Base
from modules.kinematics.camera import Camera
from modules.kinematics.griditem import GridItem
from modules.kinematics.movmentrig import MovementRig
from modules.kinematics.object3d import Object3D
from modules.kinematics.pointitem import PointItem
from modules.kinematics.renderer import Renderer
from modules.kinematics.utils import Utils

import pyMotion as pm

from OpenGL.GL import *


class BodyRender(Base):
    def __init__(self, parent=None) -> None:
        self.c3d=pm.c3dFile("E:/Dev/auto-marker-label/training_data/training/caohengyi_bend.c3d.c3d")
        print("-----------------")
        print(self.c3d.data)
        super().__init__(parent)

    def initializeGL(self) -> None:
        super().initializeGL()

        self.renderer = Renderer(self)
        self.scene = Object3D()
        self.camera = Camera(aspectRatio=800 / 600)
        self.camera.setPosition([100, 100, 500])
        self.rig = MovementRig(unitsPerSecond=100)
        self.rig.add(self.camera)
        self.rig.setPosition([0, 1, 2])
        self.scene.add(self.rig)

        axes = AxesItem(axisLength=100)
        grid = GridItem(size=100, gridColor=[1, 1, 1], centerColor=[1, 1, 0])
        grid.rotateX(-pi / 2)
        point = PointItem()

        self.scene.add(axes)
        self.scene.add(grid)
        self.scene.add(point)

    def paintGL(self) -> None:
        super().paintGL()
        self.renderer.render(self.scene, self.camera)
        self.rig.update(self.input, self.deltaTime)
