# package: bridges.base

#
#  * @brief This is a class in BRIDGES for representing an (n x n) grid.
#  * @author David Burlinson
#  * @param
#
# class Grid():
#     grid = []
#     gridSize = [10, 10]
#     maxGridSize = [480, 640]
#
#     def get_data_structure_type(self):
#         return "Grid"
#
#     #
#     # 	 * Grid constructors
#     #    *
#     #
#     def __init__(self):
#         self.__init__(self, self.gridSize)
#
#     def __init___0(self, size):
#         super(Grid, self).__init__()
#         self.__init__([None]*)
#
#     def __init___1(self, rows, cols):
#         super(Grid, self).__init__()
#         self.__init__([None]*)
#
#     def __init___2(self, size):
#         super(Grid, self).__init__()
#         if (size[0] <= 0 or size[0] > self.maxGridSize[0]) or (size[1] <= 0 or size[1] > self.maxGridSize[1]):
#             raise ValueError("\nInvalid size: [" + size[0] + "," + size[1] + "]... please use values between (0 and " + self.maxGridSize[0] + "] for rows and values between (0 and " + self.maxGridSize[1] + "] for columns!\n")
#         #  set up outer list capacity (rows)
#         self.grid = [size[0]]
#         i = 0
#         while i < size[0]:
#             self.grid.append([size[1]])
#             while j < size[1]:
#                 self.grid.get(i).add(None)
#                 j += 1
#             i += 1
#         #  set up inner lists (columns)
#         #  initialize values in inner lists
#     def get_dimensions(self):
#         return [None]*
#
#     #  get the (row, col) element in the grid
#     def get(self, row, col):
#         try:
#             return self.grid.get(row).get(col)
#         except Exception as e:
#             e.printStackTrace()
#             return None
#
#     #  set the (row, col) element in the grid
#     def set(self, row, col, val):
#         try:
#             self.grid.get(row).set(col, val)
#         except Exception as e:
#             e.printStackTrace()
