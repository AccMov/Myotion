from ..mesh import Mesh
from ..geometry import Geometry
from ..materials.linematerial import LineMaterial


class GridItem(Mesh):
    def __init__(
        self,
        size=10,
        divisions=10,
        gridColor=[1, 1, 1],
        centerColor=[0.5, 0.5, 0.5],
        lineWidth=1,
    ):
        geo = Geometry()
        positionData = []
        colorData = []

        values = []
        deltaSize = size / divisions
        for n in range(divisions + 1):
            values.append(-size / 2 + n * deltaSize)
        for x in values:
            positionData.append([x, -size / 2, 0])
            positionData.append([x, size / 2, 0])
            if x == 0:
                colorData.append(centerColor)
                colorData.append(centerColor)
            else:
                colorData.append(gridColor)
                colorData.append(gridColor)

        for y in values:
            positionData.append([-size / 2, y, 0])
            positionData.append([size / 2, y, 0])
            if y == 0:
                colorData.append(centerColor)
                colorData.append(centerColor)
            else:
                colorData.append(gridColor)
                colorData.append(gridColor)
        geo.addAttribute("vec3", "vertexPosition", positionData)
        geo.addAttribute("vec3", "vertexColor", colorData)
        geo.countVertices()

        mat = LineMaterial(
            {"lineWidth": lineWidth, "useVertexColors": True, "lineType": "segments"}
        )
        super().__init__(geo, mat)
