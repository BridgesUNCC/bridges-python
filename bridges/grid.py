##
#  @brief This is a class in BRIDGES for representing an (n x n) grid.
#  @author David Burlinson
#
import traceback

class Grid:
    grid = []
    gridSize = [10, 10]
    maxGridSize = [1080, 1920]

    def _get_data_structure_type(self) -> str:
        """
        Get the data structure type
        Returns:
            str
        """
        return "Grid"

    def __init__(self, size = None, rows = None, cols = None) -> None:
        """
        grid constructor
        Args:
            size: size of the grid as array
            rows: number of rows in grid
            cols: number of the columns in grid
        Returns:
            None
        Raises:
            value error
        """
        if 'size' is not None:
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

    @property
    def dimensions(self) -> list:
        """
        Getter for the dimensions of the grid
        Returns:
            list
        """
        return [self.gridSize[0], self.gridSize[1]]

    def get(self, row: int, col: int):
        """
        Get the row,col element in the grid
        Args:
            row: row the element is in
            col: col the element is in
        Returns:
            list, None
        Raises
            traceback exception
        """
        try:
            return self.grid[row][col]
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            return None

    def set(self, row: int, col: int, val) -> None:
        """
        set the (row, col) element in the grid
        Args:
            row: row position
            col: column position
            val: value to be set in (row, col) position
        Returns:
            None
        """
        self.grid[int(row)][int(col)] = val
