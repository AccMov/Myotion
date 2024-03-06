from OpenGL.GL import *


class Utils:
    @staticmethod
    def initializeShader(shaderCode, shaderType):
        shaderRef = glCreateShader(shaderType)
        glShaderSource(shaderRef, shaderCode)
        glCompileShader(shaderRef)
        if glGetShaderiv(shaderRef, GL_COMPILE_STATUS) != GL_TRUE:
            raise Exception(glGetShaderInfoLog(shaderRef))
        return shaderRef

    @staticmethod
    def initializeProgram(vsCode, fsCode):
        vertexShaderRef = Utils.initializeShader(vsCode, GL_VERTEX_SHADER)
        fragmentShaderRef = Utils.initializeShader(fsCode, GL_FRAGMENT_SHADER)
        programRef = glCreateProgram()
        glAttachShader(programRef, vertexShaderRef)
        glAttachShader(programRef, fragmentShaderRef)
        glLinkProgram(programRef)
        if glGetProgramiv(programRef, GL_LINK_STATUS) != GL_TRUE:
            raise Exception(glGetProgramInfoLog(programRef))
        return programRef
