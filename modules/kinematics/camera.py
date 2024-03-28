# import standard library

# import third party library
from numpy.linalg import inv

# import local library
from modules.kinematics.matrix import Matrix
from modules.kinematics.object3d import Object3D


class Camera(Object3D):
    def __init__(self, angleOfView=60, aspectRatio=1, near=0.1, far=1000):
        super().__init__()
        self.projectionMatrix = Matrix.makePersepctive(
            angleOfView, aspectRatio, near, far
        )
        self.viewMatrix = Matrix.makeIdentity()

    def updateViewMatrix(self):
        self.viewMatrix = inv(self.getWorldMatrix())

    def setPerspective(self, angleOfView=50, aspectRatio=1, near=0.1, far=1000):
        self.projectionMatrix = Matrix.makePerspective(
            angleOfView, aspectRatio, near, far
        )

    def setOrthographic(self, left=-1, right=1, bottom=-1, top=1, near=-1, far=1):
        self.projectionMatrix = Matrix.makeOrthographic(
            left, right, bottom, top, near, far
        )
