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

    def get_data_structure_type(self):
        return "ColorGrid"

    #
    #  Grid constructor with size arguments
    #
    #  @param rows - int representing the number of rows of the grid
    #  @param cols - int representing the number of columns of the grid
    #  @param color - Color object
    #
    def __init__(self, rows: int = 10, cols: int = 10, color: Color = baseColor):
        """
        Grid constructor
        :param int rows: number of rows in the grid
        :param int cols: number of columns in the grid
        :param Color color: base color of the each grid pixel
        """
        super(ColorGrid, self).__init__(rows=rows, cols=cols)
        self.baseColor = color
        self.gridSize = [rows, cols]

        self.initialize_grid()

   ##
   #  Populate the grid with the base color
   #
   #
    def initialize_grid(self):
        for i in range(self.gridSize[0]):
            for j in range(self.gridSize[1]):
                self.set(i, j, self.baseColor)

    ##
    # set the (row, col) element in the ColorGrid
    # @param row - which row to access
    # @param col - which col to access
    # @param color - background color for the cell at row,col
    def set(self, row, col, color):
        super(ColorGrid, self).set(row, col, color)

    ##
    # get the Run Length Encoding of ColorGrid
    #
    def get_rle(self):

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

    ##
    # get raw encoding of ColorGrid
    def get_raw(self):
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

    ##
    #  
    #   get the JSON representation of the color grid
    #
    #   @return the JSON representation of the color grid
    #
    def get_data_structure_representation(self):
        # imageBytes = bytearray()
        # for i in range(self.gridSize[0]):
        #     if (self.grid[i] is not None):
        #         for j in range(self.gridSize[1]):
        #             color = self.grid[i][j]
        #             color = color.getByteRepresentation()
        #             for k in range(len(color)):
        #                 imageBytes.append(color[k])
                    # for k in range(len(color)):
                    #     imageBytes.append(int.from_bytes(color[k], 'little'))
        byte_buff = self.get_rle()
        encoding = "RLE"

        if len(byte_buff) > self.gridSize[0] * self.gridSize[1] * 4:
            encoding = "RAW"
            byte_buff = self.get_raw()
            print("RAW ran")
        else:
            print("RLE ran")


        # json_str = self.QUOTE + "nodes" + self.QUOTE + self.COLON + self.OPEN_BOX + self.QUOTE + base64.b64encode((imageBytes)).decode() + self.QUOTE + self.CLOSE_BOX + self.COMMA
        json_str = self.QUOTE + "encoding" + self.QUOTE + self.COLON + self.QUOTE + encoding + self.QUOTE + self.COMMA + self.QUOTE + "nodes" + self.QUOTE + self.COLON + self.OPEN_BOX  + self.QUOTE + base64.b64encode(bytes(byte_buff)).decode() + self.QUOTE + self.CLOSE_BOX + self.COMMA

        json_str += self.QUOTE + "dimensions" + self.QUOTE + self.COLON + self.OPEN_BOX + str(self.gridSize[0]) + "," + str(self.gridSize[1]) + self.CLOSE_BOX + self.CLOSE_CURLY

        return json_str
