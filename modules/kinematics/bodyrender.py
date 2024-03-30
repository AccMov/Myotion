from math import pi
import os

from modules.kinematics.axesitem import AxesItem
from modules.kinematics.base import Base
from modules.kinematics.camera import Camera
from modules.kinematics.griditem import GridItem
from modules.kinematics.movmentrig import MovementRig
from modules.kinematics.object3d import Object3D
from modules.kinematics.pointitem import PointItem
from modules.kinematics.renderer import Renderer

import pyMotion as pm

from PySide6.QtWidgets import QWidget
from OpenGL.GL import *


def isrealmarker(rawlabels, label):
    """check if a marker is a real marker by replacing the last character with 'L' 'O' 'A' 'P'

    Args:
        rawlabels (list of str): all labels in the c3d file
        label (str): current label being investigated

    Returns:
        bool: True if the marker is a real marker
    """

    if (
        label.endswith("L")
        or label.endswith("O")
        or label.endswith("A")
        or label.endswith("P")
    ):
        return not (
            label[:-1] + "L" in rawlabels
            and label[:-1] + "O" in rawlabels
            and label[:-1] + "A" in rawlabels
            and label[:-1] + "P" in rawlabels
        )
    return True


def ismarker(label):
    """check if label is a marker

    Args:
        points (dict of listof str): dictionary of all points in the c3d file
        label (str): current label name

    Returns:
        bool : if label is a marker
    """
    return len(label) < 6


class BodyRender(Base):
    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        c3d = pm.c3dFile(os.getcwd() + "/ERRPT.c3d")
        self.frame = c3d.data["frame_number"]
        self.start = 0
        labels = list(
            filter(
                lambda x: ismarker(x) and isrealmarker(c3d.data["point_labels"], x),
                c3d.data["point_labels"],
            )
        )
        p = c3d.data["points"].data
        analog = c3d.data["analog"]
        self.points = {}
        for joint in labels:
            self.points[joint] = p[joint]

    def initializeGL(self) -> None:
        super().initializeGL()

        self.renderer = Renderer(self)
        self.scene = Object3D()
        self.camera = Camera(aspectRatio=9 / 16, far=50000)
        self.camera.setPosition([0, 1000, 3000])
        self.rig = MovementRig(unitsPerSecond=100)
        self.rig.add(self.camera)
        self.rig.setPosition([0, 1, 2])
        self.scene.add(self.rig)

        axes = AxesItem(axisLength=100)
        grid = GridItem(size=5000, gridColor=[1, 1, 1], centerColor=[1, 1, 0])
        grid.rotateX(-pi / 2)
        self.point = self.currentFrame()

        self.scene.add(axes)
        self.scene.add(grid)
        self.scene.add(self.point)

    def paintGL(self) -> None:
        super().paintGL()
        self.scene.remove(self.point)
        self.point = self.currentFrame()
        self.scene.add(self.point)
        self.start += 1
        if self.start >= self.frame:
            self.start = 0
        self.renderer.render(self.scene, self.camera)
        self.rig.update(self.input, self.deltaTime)

    def currentFrame(self):
        cf = []
        for joint in self.points:
            cf.append(
                [
                    self.points[joint][self.start].xyz[0],
                    self.points[joint][self.start].xyz[2],
                    self.points[joint][self.start].xyz[1],
                ]
            )
        return PointItem(cf)
