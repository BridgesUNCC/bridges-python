from Bridges.Color import *
from Bridges.Grid import *
import base64

class ColorGrid(Grid):
    QUOTE = "\""
    COMMA = ","
    COLON = ":"
    OPEN_CURLY = "{"
    CLOSE_CURLY = "}"
    OPEN_PAREN = "("
    CLOSE_PAREN = ")"
    OPEN_BOX = "["
    CLOSE_BOX = "]"

    baseColor = Color(r = 0,g = 0,b = 0,a = 1.0)

    def get_data_structure_type(self):
        return "ColorGrid"

    def __init__(self, rows = None, cols = None, color = None):
        if rows is None and cols is None and color is None:
            self.__init__(10, 10, self.baseColor)
        elif rows is not None and cols is not None and color is None:
            self.__init__(rows, cols, self.baseColor)
        elif rows is not None and cols is not None and color is not None:
            super(ColorGrid, self).__init__(rows = rows, cols = cols)
            self.baseColor = color
            self.gridSize = [rows, cols]

            self.initializeGrid()

    def initializeGrid(self):
        for i in range(self.gridSize[0]):
            for j in range(self.gridSize[1]):
                self.set(i, j, self.baseColor)

    def set(self, row, col, color):
        super(ColorGrid, self).set(row, col, color)

    def get_data_structure_representation(self):
        imageBytes = bytearray()
        for i in range(self.gridSize[0]):
            if (self.grid[i] is not None):
                for j in range(self.gridSize[1]):
                    color = self.grid[i][j]
                    color = color.getByteRepresentation()
                    for k in range(len(color)):
                        imageBytes.append(color[k])
                    # for k in range(len(color)):
                    #     imageBytes.append(int.from_bytes(color[k], 'little'))

        json_str = self.QUOTE + "nodes" + self.QUOTE + self.COLON + self.OPEN_BOX + self.QUOTE + base64.b64encode((imageBytes)).decode() + self.QUOTE + self.CLOSE_BOX + self.COMMA

        json_str += self.QUOTE + "dimensions" + self.QUOTE + self.COLON + self.OPEN_BOX + str(self.gridSize[0]) + "," + str(self.gridSize[1]) + self.CLOSE_BOX + self.CLOSE_CURLY

        return json_str

