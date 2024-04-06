from OpenGL.GL import *

from ..materials.basicmaterial import BasicMaterial


class PointMaterial(BasicMaterial):
    def __init__(self, properties={}):
        super().__init__()

        self.settings["drawStyle"] = GL_POINTS
        self.settings["pointSize"] = 8
        self.settings["roundedPoints"] = True
        self.setProperties(properties)

    def updateRenderSettings(self):
        glPointSize(self.settings["pointSize"])
        if self.settings["roundedPoints"]:
            glEnable(GL_POINT_SMOOTH)
        else:
            glDisable(GL_POINT_SMOOTH)
