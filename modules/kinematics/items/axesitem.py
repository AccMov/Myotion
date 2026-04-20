from ..mesh import Mesh
from ..geometry import Geometry
from ..materials.linematerial import LineMaterial


class AxesItem(Mesh):
    def __init__(
        self, axisLength=1, lineWidth=4, axisColors=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    ):
        geo = Geometry()
        positionData = [
            [0, 0, 0],
            [axisLength, 0, 0],
            [0, 0, 0],
            [0, axisLength, 0],
            [0, 0, 0],
            [0, 0, axisLength],
        ]
        colorData = [
            axisColors[0],
            axisColors[0],
            axisColors[1],
            axisColors[1],
            axisColors[2],
            axisColors[2],
        ]
        geo.addAttribute("vec3", "vertexPosition", positionData)
        geo.addAttribute("vec3", "vertexColor", colorData)
        geo.countVertices()
        mat = LineMaterial(
            {"lineWidth": lineWidth, "useVertexColors": True, "lineType": "segments"}
        )
        super().__init__(geo, mat)
