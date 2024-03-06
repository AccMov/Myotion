from math import pi
from numpy import arange, sin
from modules.kinematics.attribute import Attribute
from modules.kinematics.axesitem import AxesItem
from modules.kinematics.base import Base
from modules.kinematics.camera import Camera
from modules.kinematics.geometry import Geometry
from modules.kinematics.griditem import GridItem
from modules.kinematics.mesh import Mesh
from modules.kinematics.object3d import Object3D
from modules.kinematics.pointmaterial import PointMaterial
from modules.kinematics.renderer import Renderer
from modules.kinematics.surfacematerial import SurfaceMaterial

from modules.kinematics.utils import Utils

from OpenGL.GL import *


class BodyRender(Base):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

    def initializeGL(self) -> None:
        super().initializeGL()

        self.renderer = Renderer(self)
        self.scene = Object3D()
        self.camera = Camera(aspectRatio=800 / 600)
        self.camera.setPosition([0.5, 1, 4])

        axes = AxesItem(axisLength=2)
        grid = GridItem(size=20, gridColor=[1, 1, 1], centerColor=[1, 1, 0])
        grid.rotateX(-pi / 2)

        self.scene.add(axes)
        self.scene.add(grid)

    def paintGL(self) -> None:
        super().paintGL()
        self.renderer.render(self.scene, self.camera)
