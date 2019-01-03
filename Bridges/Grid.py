##
#  @brief This is a class in BRIDGES for representing an (n x n) grid.
#  @author David Burlinson
#  @param
import traceback

class Grid:
    grid = []
    gridSize = [10, 10]
    maxGridSize = [1080, 1920]

    def get_data_structure_type(self):
        return "Grid"

    ##
    # Grid constructors
    # @param size - size of the grid as array
    # @param rows - number of rows in grid
    # @param cols - number of columns in grid
    #
    def __init__(self, size = None, rows = None, cols = None):
        if size is not None:
            if ((size[0] <= 0 or size[0] > self.maxGridSize[0]) or (size[1] <= 0 or size[1] > self.maxGridSize[1])):
                raise ValueError("Invalid size: [" + str(str(size[0]) + "," + str(size[1]) + "] .. please use values between (0 and " + str(self.maxGridSize[0]) + "] for rows and values between (0 and " + str(self.maxGridSize[1]) + "] for columns"))
            self.grid = []
            for i in range(size[0]):
                self.grid.append([])
                for j in range(size[1]):
                    self.grid[i].append(None)
        if rows is not None and cols is not None:
            size = [rows, cols]
            if ((size[0] <= 0 or size[0] > self.maxGridSize[0]) or (size[1] <= 0 or size[1] > self.maxGridSize[1])):
                raise ValueError("Invalid size: [" + str(str(size[0]) + "," + str(size[1]) + "] .. please use values between (0 and " + str(self.maxGridSize[0]) + "] for rows and values between (0 and " + str(self.maxGridSize[1]) + "] for columns"))
            self.grid = []
            for i in range(size[0]):
                self.grid.append([])
                for j in range(size[1]):
                    self.grid[i].append(None)

    ##
    #  set up inner lists (columns)
    #  initialize values in inner lists
    def get_dimensions(self):
        return [self.gridSize[0], self.gridSize[1]]

    ##
    #  get the (row, col) element in the grid
    def get(self, row, col):
        try:
            return self.grid[row][col]
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            return None

    ##
    #  set the (row, col) element in the grid
    def set(self, row, col, val):
        self.grid[int(row)][int(col)] = val
