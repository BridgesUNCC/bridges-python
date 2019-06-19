from bridges.color import *
from bridges.grid import *
import base64


##
#  @brief This is a class in BRIDGES for representing an (n x n) grid.
#  @author David Burlinson
#
#
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

    baseColor = Color(r=0, g=0, b=0, a=1.0)

    def _get_data_structure_type(self) -> str:
        """
        Get the data structure type
        Returns:
            str
        """
        return "ColorGrid"

    def __init__(self, rows: int = 10, cols: int = 10, color: Color = baseColor) -> None:
        """
        Color Grid constructor
        Args:
            rows: number of rows in the grid
            cols: number of columns in the grid
            color: base color of the each grid pixel
        Returns:
            None
        """
        super(ColorGrid, self).__init__(rows=rows, cols=cols)
        self.baseColor = color
        self.gridSize = [rows, cols]
        self.initialize_grid()

    def initialize_grid(self) -> None:
        """
        initialize the grid anf populate with base colors
        Returns:
            None
        """
        for i in range(self.gridSize[0]):
            for j in range(self.gridSize[1]):
                self.set(i, j, self.baseColor)

    def set(self, row: int, col: int, color: Color) -> None:
        """
        Set the (row, col) element in the color grid
        Args:
            row - which row to access
            col - which col to access
            color - background color for the cell at row,col
        Returns:
            None
        """
        super(ColorGrid, self).set(row, col, color)

    def get_rle(self) -> bytearray:
        """
        Get the run length encoding of color grid
        Returns:
            bytearray
        """
        img_bytes = bytearray()
        count = 0
        total_count = 0
        pos = 0
        last = self.grid[0][0]

        while pos < self.gridSize[0] * self.gridSize[1]:
            posY = pos / self.gridSize[1]
            posX = pos % self.gridSize[1]
            current = self.grid[int(posY)][int(posX)]

            if count == 0:
                count = 1
                last = current
            else:
                if last == current:
                    count += 1
                else:
                    total_count += count
                    img_bytes.append(count-1)
                    last = last.get_byte_representation()

                    for k in range(len(last)):
                        img_bytes.append(last[k])

                    count = 1
                    last = current
            if count == 256:
                total_count += count
                img_bytes.append(count-1)
                last = last.get_byte_representation()
                for k in range(len(last)):
                    img_bytes.append(last[k])
                count = 0
            pos += 1
        total_count += count
        img_bytes.append(count-1)
        last = last.get_byte_representation()
        for k in range(len(last)):
            img_bytes.append(last[k])

        if total_count != self.gridSize[0] * self.gridSize[1]:
            print("Something broke in getRLE construction")

        return img_bytes

    def get_raw(self) -> bytearray:
        """
        Get raw encoding of color grid
        Returns:
            bytearray
        """
        img_bytes = bytearray()
        for i in range(self.gridSize[0]):
            if self.grid[i] is not None:
                for j in range(self.gridSize[1]):
                    if self.grid[i][j] is not None:
                        color = self.grid[i][j]
                        color = color.get_byte_representation()
                        for k in range(len(color)):
                            img_bytes.append(color[k])
        return img_bytes

    def _get_data_structure_representation(self) -> str:
        """
        Get the JSON representation of the color grid
        Returns:
            str
        """
        byte_buff = self.get_rle()
        encoding = "RLE"

        if len(byte_buff) > self.gridSize[0] * self.gridSize[1] * 4:
            encoding = "RAW"
            byte_buff = self.get_raw()
            print("RAW ran")
        else:
            print("RLE ran")

        json_str = self.QUOTE + "encoding" + self.QUOTE + self.COLON + self.QUOTE + encoding + self.QUOTE + self.COMMA + self.QUOTE + "nodes" + self.QUOTE + self.COLON + self.OPEN_BOX  + self.QUOTE + base64.b64encode(bytes(byte_buff)).decode() + self.QUOTE + self.CLOSE_BOX + self.COMMA
        json_str += self.QUOTE + "dimensions" + self.QUOTE + self.COLON + self.OPEN_BOX + str(self.gridSize[0]) + "," + str(self.gridSize[1]) + self.CLOSE_BOX + self.CLOSE_CURLY

        return json_str
