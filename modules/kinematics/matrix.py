from locale import normalize
from math import acos, atan2, sin, cos, tan, pi

import numpy
from numpy import subtract, divide, cross
from numpy.linalg import norm

class Matrix(object):

    @staticmethod
    def makeIdentity():
        return numpy.array([[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def makeTranslation(x, y, z):
        return numpy.array([[1, 0, 0, x],
                            [0, 1, 0, y],
                            [0, 0, 1, z],
                            [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def makeRotationX(angle):
        c = cos(angle)
        s = sin(angle)
        return numpy.array([[1, 0,  0, 0],
                            [0, c, -s, 0],
                            [0, s,  c, 0],
                            [0, 0,  0, 1]]).astype(float)

    @staticmethod
    def makeRotationY(angle):
        c = cos(angle)
        s = sin(angle)
        return numpy.array([[c, 0, s, 0],
                            [0, 1, 0, 0],
                            [-s, 0, c, 0],
                            [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def makeRotationZ(angle):
        c = cos(angle)
        s = sin(angle)
        return numpy.array([[c, -s, 0, 0],
                            [s,  c, 0, 0],
                            [0,  0, 1, 0],
                            [0,  0, 0, 1]]).astype(float)
        
    @staticmethod
    def makeRotationOrbit(x,y,position,target):
        from_target = subtract(position, target)
        radius = norm(from_target)
        p=atan2(from_target[0],from_target[2])
        t=acos(from_target[1]/radius)
        factor = 1.5*pi
        p+=x*factor
        t+=y*factor
        if (t>pi):
            t=pi-1
        if (t<0):
            t=1
        
        position[0]=target[0]+radius*sin(p)*sin(t)
        position[1]=target[1]+radius*cos(t)
        position[2]=target[2]+radius*sin(t)*cos(p)
        return Matrix.makeTranslation(position[0],position[1],position[2])
    
    @staticmethod
    def makeScale(s):
        return numpy.array([[s, 0, 0, 0],
                            [0, s, 0, 0],
                            [0, 0, s, 0],
                            [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def makePerspective(angleOfView=60, aspectRatio=1, near=0.1, far=1000):
        a = angleOfView * pi / 180.0
        d = 1.0 / tan(a / 2)
        r = aspectRatio
        b = (far + near) / (near - far)
        c = 2 * far * near / (near - far)
        return numpy.array([[d/r, 0,  0, 0],
                            [0, d,  0, 0],
                            [0, 0,  b, c],
                            [0, 0, -1, 0]]).astype(float)

    @staticmethod
    def makeLookAt(position, target):
        worldUp = [0, 1, 0]
        forward = subtract(target, position)
        right = cross(forward, worldUp)

        # if forward and worldUp vectors are parallel,
        #  right vector is zero;
        #    fix by perturbing worldUp vector a bit
        if norm(right) < 0.001:
            offset = numpy.array([0.001, 0, 0])
            right = cross(forward, worldUp + offset)

        up = cross(right, forward)

        # all vectors should have length 1
        forward = divide(forward, norm(forward))
        right = divide(right, norm(right))
        up = divide(up, norm(up))

        return numpy.array([
            [right[0], up[0], -forward[0], position[0]],
            [right[1], up[1], -forward[1], position[1]],
            [right[2], up[2], -forward[2], position[2]],
            [0, 0, 0, 1]])

    @staticmethod
    def makeOrthographic(left=-1, right=1, bottom=-1, top=1, near=-1, far=1):
        return numpy.array(
            [
                [2 / (right-left), 0, 0, -(right+left)/(right-left)],
                [0, 2 / (top-bottom), 0, -(top+bottom)/(top-bottom)],
                [0, 0, -2 / (far-near), -(far+near)/(far-near)],
                [0, 0, 0, 1]
            ]
        )
    