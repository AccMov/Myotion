from numpy.linalg import inv

from modules.kinematics.matrix import Matrix
from modules.kinematics.object3d import Object3D


class OrbitCamera(Object3D):
    def __init__(self, angleOfView=60, aspectRatio=1, near=0.1, far=1000):
        super().__init__()
        self.center = [0, 0, 0]
        self.projectionMatrix = Matrix.makePerspective(
            angleOfView, aspectRatio, near, far
        )
        self.viewMatrix = Matrix.makeIdentity()

    def updateViewMatrix(self):
        self.viewMatrix = inv(self.getWorldMatrix())

    def rotateX(self, angle, localCoord=True):
        super().rotateX(angle, localCoord)

    def rotateY(self, angle, localCoord=True):
        super().rotateY(angle, localCoord)
