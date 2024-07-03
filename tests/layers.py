from bridges import *
from pair import *

def main():

    bridges = Bridges(1, "test", "137842425086")
    bridges.set_title("2d Grid Layers")
    bridges.server = "live"

    cg = ColorGrid(20, 20, Color("white"))

    layer_cells = get_layer_cells(9, 11, cg)

    bridges.set_data_structure(cg)
    bridges.visualize()



def get_layer_cells(col, row, cg):

    layer_cells = []

    size = cg.grid_size
    grid_size = size[0]
    color_indx = 0
    color = Color("Red")
    cg.set(row, col, color)

    layer_cells.append(Pair(row,col))

    #iterate on layers, can have as  many layers as the size
    #of the grid, since the start cell can be on boundary
    for layer in range(1, grid_size):
        color_indx += 1
        color_indx = color_indx % 8
        color = color_switch(color_indx)

        #find the bounds of the layer
        l_col_min = col - layer
        l_col_max = col + layer
        l_row_min = row - layer
        l_row_max = row + layer

        #process the layer, identifying the cells in the horizontal
        #and vertical rows to be examined
        #limit the col indicies to be within the grid
        col_min =  0 if l_col_min < 0 else  l_col_min
        col_max = grid_size-1 if l_col_max >= grid_size else l_col_max

        #traverse bottom row
        if l_row_min >= 0:
            for c in range(col_min, col_max+1):
                layer_cells.append(Pair(l_row_min, c))
                cg.set(l_row_min, c, color)

        #traverse top row
        if l_row_max < grid_size:
            for c in range(col_min, col_max+1):
                layer_cells.append(Pair(l_row_max, c))
                cg.set(l_row_max, c, color)

        #next process the two columns of the layer
        #first limit the row indices to be within the grid
        row_min = 0 if l_row_min < 0 else l_row_min
        row_max = grid_size-1 if l_row_max >= grid_size else l_row_max

        #traverse left column
        if l_col_min >= 0:
            for r in range(row_min, row_max+1):
                layer_cells.append(Pair(r, l_col_min))
                cg.set(r, l_col_min, color)

        #travers right column
        if l_col_max < grid_size:
            for r in range(row_min, row_max+1):
                layer_cells.append(Pair(r, l_col_max))
                cg.set(r, l_col_max, color)

    return layer_cells

def color_switch(indx):
    switcher = {
        0: Color("red"),
        1: Color("green"),
        2: Color("blue"),
        3: Color('cyan'),
        4: Color("yellow"),
        5: Color("magenta"),
        6: Color("orange"),
        7: Color("black")
    }

    return switcher.get(indx, "Invalid Index")


class Pair():

    def __init__(self, f, s):
        self.first = f
        self.second = s

if __name__ == "__main__":
    main()