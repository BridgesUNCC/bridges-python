

class Grid:
    """
    @brief This is a base class in BRIDGES for representing an (n x n) grid.
    
    @author David Burlinson, Matthew McQuaigue

    @date  2018, 7/24/19, 2021

    \sa Color grid tutorial at https://bridgesuncc.github.io/tutorials/Grid.html
    """
    import traceback

    grid_size = [10, 10]
    maxGridSize = [1080, 1920]

    def get_data_structure_type(self) -> str:
        """
        Get the data structure type
        Returns:
            str: representing the data structure type
        """
        return "Grid"

    def __init__(self, **kwargs) -> None:
        """
        Grid constructor
        Kwargs:
            size: size of the grid as array
            rows: number of rows in grid
            cols: number of the columns in grid
        Returns:
            None
        Raises:
            ValueError: if the size dimensions are greater than the max grid sizes (1080, 1920)
        """
        if 'size' in kwargs:
            if (kwargs['size'][0] <= 0 or kwargs['size'][0] > Grid.maxGridSize[0]) or \
                    (kwargs['size'][1] <= 0 or kwargs['size'][1] > Grid.maxGridSize[1]):
                raise ValueError("Invalid size: [" + str(
                    str(kwargs['size'][0]) + "," + str(kwargs['size'][1]) + "] .. please use values between (0 and " +
                    str(self.maxGridSize[0]) + "] for rows and values between (0 and " + str(
                        self.maxGridSize[1]) + "] for columns"))
            self.grid = []
            for i in range(kwargs['size'][0]):
                self.grid.append([])
                for j in range(kwargs['size'][1]):
                    self.grid[i].append(None)
        if 'rows' in kwargs and 'cols' in kwargs:
            size = [kwargs['rows'], kwargs['cols']]
            if (size[0] <= 0 or size[0] > self.maxGridSize[0]) or (size[1] <= 0 or size[1] > self.maxGridSize[1]):
                raise ValueError("Invalid size: [" + str(
                    str(size[0]) + "," + str(size[1]) + "] .. please use values between (0 and " + str(
                        self.maxGridSize[0]) + "] for rows and values between (0 and " + str(
                        self.maxGridSize[1]) + "] for columns"))
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
            list: as the dimensions of the grid
        """
        return [self.grid_size[0], self.grid_size[1]]

    def get(self, row: int, col: int):
        """
        Get the row,col element in the grid
        Args:
            (int) row: row the element is in
            (int) col: col the element is in
        Returns:
            element, none
        Raises
            Exception: printing the traceback stack if returning the row and column is an error
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
        Raises:
            Exception: if setting the element at the row and column is a problem
        """
        try:
            self.grid[int(row)][int(col)] = val
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            return None
