from modules.kinematics.mesh import Mesh
from modules.kinematics.geometry import Geometry
from modules.kinematics.pointmaterial import PointMaterial


class PointItem(Mesh):
    def __init__(self, points=None):
        self.points = [[0, 0, 0]] if points is None else points
        geo = Geometry()
        geo.addAttribute("vec3", "vertexPosition", self.points)
        geo.countVertices()
        mat = PointMaterial({"baseColor": [1, 1, 0]})
        super().__init__(geo, mat)
