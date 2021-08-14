from bridges.color import *
from bridges.grid import *
import base64

class ColorGrid(Grid):
    """
    @brief This is a class in BRIDGES for representing an (n x n) grid.
    
    A ColorGrid is essentially an image. One can construct an image of
    a particular size using the ColorGrid() constructor to be either
    blank or filled with a particular Color depending on which
    constructor is called.
    
    \code{.py}
    grid = new ColorGrid(rows, columns)
    grid.set(2, 3, Color("lightsalmon")
    \endcode
    
    You can get a ColorGrid from an existing Bridges ColorGrid assignment using
    bridges.get_color_grid_from_assignment(bridges.get_username(), bridges.get_assignment_id(), 0)
    
    @author David Burlinson, Matthew McQuaigue
    
    @date 2018, 7/24/19, 2021
    
    Color grid tutorial at https://bridgesuncc.github.io/tutorials/Grid.html
    """


    baseColor = Color(r=0, g=0, b=0, a=1.0)

    def get_data_structure_type(self) -> str:
        """
        Get the data structure type
        Returns:
            str : data structure type
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
        self.base_color = color
        self.grid_size = [rows, cols]
        self.initialize_grid()

    def initialize_grid(self) -> None:
        """
        initialize the grid anf populate with base colors
        Returns:
            None
        """
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                self.set(i, j, self.base_color)

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

        while pos < self.grid_size[0] * self.grid_size[1]:
            posY = pos / self.grid_size[1]
            posX = pos % self.grid_size[1]
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

        if total_count != self.grid_size[0] * self.grid_size[1]:
            print("Something broke in getRLE construction")

        return img_bytes

    def get_raw(self) -> bytearray:
        """
        Get raw encoding of color grid
        Returns:
            bytearray: representing the colors of grid cells
        """
        img_bytes = bytearray()
        for i in range(self.grid_size[0]):
            if self.grid[i] is not None:
                for j in range(self.grid_size[1]):
                    if self.grid[i][j] is not None:
                        color = self.grid[i][j]
                        color = color.get_byte_representation()
                        for k in range(len(color)):
                            img_bytes.append(color[k])
        return img_bytes

    def get_data_structure_representation(self) -> dict:
        """
        Get the JSON representation of the color grid
        Returns:
            str: representing the json  of the color grid
        """
        byte_buff = self.get_rle()
        encoding = "RLE"

        if len(byte_buff) > self.grid_size[0] * self.grid_size[1] * 4:
            encoding = "RAW"
            byte_buff = self.get_raw()
            print("RAW ran")
        else:
            print("RLE ran")

        json_dict = {
            "encoding": encoding,
            "nodes": [base64.b64encode(bytes(byte_buff)).decode()],
            "dimensions": [self.grid_size[0], self.grid_size[1]]
        }

        return json_dict
