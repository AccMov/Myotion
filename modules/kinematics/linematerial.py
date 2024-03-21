from modules.kinematics.basicmaterial import BasicMaterial
from OpenGL.GL import *


class LineMaterial(BasicMaterial):
    def __init__(self, properties={}):
        super().__init__()

        self.settings["drawStyle"] = GL_LINE_STRIP
        self.settings["lineWidth"] = 1
        self.settings["lineType"] = "connected"
        self.setProperties(properties)

    def updateRenderSettings(self):
        glLineWidth(self.settings["lineWidth"])
        if self.settings["lineType"] == "connected":
            self.settings["drawStyle"] = GL_LINE_STRIP
        elif self.settings["lineType"] == "loop":
            self.settings["drawStyle"] = GL_LINE_LOOP
        elif self.settings["lineType"] == "segments":
            self.settings["drawStyle"] = GL_LINES
        else:
            raise Exception("Unknown line type: " + self.settings["lineType"])
