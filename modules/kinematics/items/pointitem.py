from ..mesh import Mesh
from ..geometry import Geometry
from ..materials.pointmaterial import PointMaterial


class PointItem(Mesh):
    def __init__(self, p=None):
        self.geo = Geometry()
        self.geo.addAttribute("vec3", "vertexPosition", p)
        self.geo.countVertices()
        mat = PointMaterial({"baseColor": [1, 1, 1]})
        super().__init__(self.geo, mat)
