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


def ismarker(points, label):
    """check if label is a marker

    Args:
        points (dict of listof str): dictionary of all points in the c3d file
        label (str): current label name

    Returns:
        bool : if label is a marker
    """
    for key in points:
        if key != "LABELS" and "value" in points[key] and label in points[key]["value"]:
            return False
    return True


class BodyRender(Base):
    def __init__(self, parent=None) -> None:
        self.c3d = pm.c3dFile(
            "E:/Dev/auto-marker-label/training_data/training/caohengyi_bend.c3d.c3d"
        )
        self.frame = self.c3d.data["frame_number"]
        self.start = 0
        labels = self.c3d.data["point_labels"]
        points = self.c3d.data["points"]
        analog = self.c3d.data["analog"]
        self.points = []
        for joint in points.data:
            if isrealmarker(labels, joint):
                self.points.append(
                    [
                        points.data[joint][0].xyz[0],
                        points.data[joint][0].xyz[2],
                        points.data[joint][0].xyz[1],
                    ]
                )
        super().__init__(parent)

    def initializeGL(self) -> None:
        super().initializeGL()

        self.renderer = Renderer(self)
        self.scene = Object3D()
        self.camera = Camera(aspectRatio=800 / 600, far=50000)
        self.camera.setPosition([0, 1000, 3000])
        self.rig = MovementRig(unitsPerSecond=100)
        self.rig.add(self.camera)
        self.rig.setPosition([0, 1, 2])
        self.scene.add(self.rig)

        axes = AxesItem(axisLength=100)
        grid = GridItem(size=5000, gridColor=[1, 1, 1], centerColor=[1, 1, 0])
        grid.rotateX(-pi / 2)
        self.point = PointItem(self.points)

        self.scene.add(axes)
        self.scene.add(grid)
        self.scene.add(self.point)

    def paintGL(self) -> None:
        super().paintGL()
        self.renderer.render(self.scene, self.camera)
        self.rig.update(self.input, self.deltaTime)
