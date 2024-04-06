from OpenGL.GL import *

from ..uniform import Uniform
from ..utils import Utils


class Material(object):
    def __init__(self, vShader, fShader):
        self.program = Utils.initializeProgram(vShader, fShader)
        self.uniforms = {}
        self.uniforms["modelMatrix"] = Uniform("mat4", None)
        self.uniforms["viewMatrix"] = Uniform("mat4", None)
        self.uniforms["projectionMatrix"] = Uniform("mat4", None)

        self.settings = {}
        self.settings["drawStyle"] = GL_TRIANGLES

    def addUniform(self, type, name, value):
        self.uniforms[name] = Uniform(type, value)

    def locateUniforms(self):
        for name, uniform in self.uniforms.items():
            uniform.locateVariable(self.program, name)

    def setProperties(self, properties):
        for name, value in properties.items():
            if name in self.uniforms.keys():
                self.uniforms[name].data = value
            elif name in self.settings.keys():
                self.settings[name] = value
            else:
                raise Exception("Unknown property: " + name)

    def updateRenderSettings(self):
        pass
