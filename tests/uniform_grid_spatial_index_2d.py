from tests.pair import *

"""
This is a solution to determine the closest point in a 2D grid, given source point.

This is an early termination algorithm, progressing outward by layers, i.e. the initial
layer is the 3x3 cells around the source cell, then 9x9, etc.  Once a layer is processed which does not update the
closest point, the algorithm stops.
Within each layer, the shortest (orthogonal) distance to
the layer boundaries is compared against the current
shortest distance to possibly ignore that boundary of cells
"""

class MutableDouble:

    def __init__(self, value):
        self.value = value

class SpatialIndex2D:

    def __init__(self, v, c):
        self.ve = v
        self.ce = c

    def distance_squared(self, x1, y1, x2, y2):
        return (x1-x2) * (x1-x2) + (y1 - y2) * (y1 - y2)

    #returns the index in the list used to construct the object closest to the given coordinate
    def get_closest_point(self, x, y, closest_pt, examined_cells):
        pass

class UniformGridSpatialIndex2D(SpatialIndex2D):

    def __init__(self, v, c, size):
        super(UniformGridSpatialIndex2D, self).__init__(v, c)

        self.grid_size = size

        self.grid_points = []
        for i in range(self.grid_size):
            self.grid_points.append([])
            for j in range(self.grid_size):
                self.grid_points[i].append([])

        print("Set size: " + str(len(v)))
        print("Grid")

        #construct xmin, xmax, ymin, ymax
        self.xmin = self.ce.get_x(self.ve[0])
        self.xmax = self.ce.get_x(self.ve[0])
        self.ymin = self.ce.get_y(self.ve[0])
        self.ymax = self.ce.get_y(self.ve[0])

        for i in range(1, len(self.ve)):
            lx = self.ce.get_x(self.ve[i])
            ly = self.ce.get_y(self.ve[i])

            #compute the bounding box of the data
            if lx < self.xmin: self.xmin = lx
            if lx > self.xmax: self.xmax = lx
            if ly < self.ymin: self.ymin = ly
            if ly > self.ymax: self.ymax = ly

        #max distance squared is based on the diagonal distance
        max_dist_sq = float("inf")

        #compute cell size
        self.cell_width = (self.xmax-self.xmin)/self.grid_size
        self.cell_height = (self.ymax-self.ymin)/self.grid_size

        #place each point in the grid
        for i in range(len(self.ve)):
            b = self.get_grid_index(self.ce.get_x(self.ve[i]), self.ce.get_y(self.ve[i]))
            self.grid_points[b.first][b.second].append(i)


    def get_grid_index(self, x, y):
        """
        this function determins the grid index into which an incoming
        point will be inserted
        """

        #index is obtained using the cell dimensions
        ix = int(((x - self.xmin)/self.cell_width))
        iy = int(((y - self.ymin)/self.cell_height))

        ix = 0 if ix < 0 else ix
        ix = self.grid_size-1 if ix >= self.grid_size else ix
        iy = 0 if iy < 0 else iy
        iy = self.grid_size-1 if iy >= self.grid_size else iy

        return Pair(ix,iy)

    def get_closest_point_in_grid_cell(self, x, y, cell_pts, closest_pt, min_dist):

        flag = False
        for i in cell_pts:
            dist = self.distance_squared(x, y, self.ce.get_x(self.ve[i]), self.ce.get_y(self.ve[i]))

            if dist < min_dist.value:
                min_dist.value = dist
                closest_pt.first = self.ce.get_x(self.ve[i])
                closest_pt.second = self.ce.get_y(self.ve[i])
                flag = True

        return flag

    def get_closest_point(self, x, y, closest_pt, examined_cells):
        """
        This function determines the closest point to the point (x, y)
	    The algorithm performs a search of points in the grid layer
	    layer; each layer is generated with pixels around the query
	    point. The algorithm is efficient in the sense that it
	    will terminate if a layer does not find a closer point; also
	    each layer is examined only if the distance to it (row or column
	    of the layer) from the query (orthogonal distance) is
	    smaller than the currently computed minimum distance.
        """

        #generate the layers, outwards from the center cell
        #each iteration we expand the layer by 1 cell in x and y
        #initialize the closest point and distance to something large
        min_dist = MutableDouble(10000000000000)
        closest_pt.first = 100000000000000
        closest_pt.second = 1000000000000

        #get grid index of souce point
        cp = self.get_grid_index(x, y)

        examined_cells.append(Pair(cp.second, cp.first))

        #check the points in the cell and containing the query point
        done = False
        flag = self.get_closest_point_in_grid_cell(x, y, self.grid_points[cp.first][cp.second], closest_pt, min_dist)

        """
        we will next examine layers of cells around the query
		point; the algorithm splits this computation into 2 rows
		and 2 columns, with checks made to ensure cells outside
		the grid are ignored
        """

        #iterate on layers, can have grid_size layers
        for layer in range(1, self.grid_size):
            print(done)
            if(not done):
                pass
            else:
                break

            done = True

            #find the bounds of the layer
            l_col_min = cp.first - layer
            l_col_max = cp.first + layer
            l_row_min = cp.second - layer
            l_row_max = cp.second + layer

            """
            process the layer, identifying the cells in the horizontal
			and vertical rows to be examined; first do the rows


			We will check each row or column if it needs to be 
			processed; it might be outside the grid, or the 
			perpendicular distance to it could be larger than
			closest distance we have already found. Both cases the
			row or column can be ignored
            """

            #limit col indices to be within the grid
            col_min = 0 if l_col_min < 0 else l_col_min
            col_max = self.grid_size-1 if l_col_max >= self.grid_size else l_col_max

            #traverse bottom row
            if l_row_min >= 0:
                #get perp. distance to bottom of layer
                y_dist = y- (self.ymin + cp.second*self.cell_height) + self.cell_height*(layer-1)
                y_dist = y_dist*y_dist

                if y_dist < min_dist.value:
                    for c in range(col_min, col_max+1):
                        examined_cells.append(Pair(l_row_min, c))
                        flag = self.get_closest_point_in_grid_cell(x, y, self.grid_points[c][l_row_min], closest_pt, min_dist)
                        done = done & (not flag)

            #traverse top row
            if l_row_max < self.grid_size:
                #get perp. distance to top row
                y_dist = (((cp.second + 1) * self.cell_height + self.ymin) - y) + self.cell_height*(layer-1)
                y_dist = y_dist*y_dist

                if y_dist < min_dist.value:
                    for c in range(col_min, col_max+1):
                        examined_cells.append(Pair(l_row_max, c))
                        flag = self.get_closest_point_in_grid_cell(x, y, self.grid_points[c][l_row_max], closest_pt, min_dist)
                        done = done & (not flag)

            #next pocess the two columns of the layer
            #first limit the row indices to be within the grid
            row_min = 0 if l_row_min < 0 else l_row_min + 1
            row_max = self.grid_size - 1 if l_row_max >= self.grid_size else l_row_max - 1

            #travers left column
            if l_col_min >= 0:
                #get perp. distance to top row
                x_dist = x - (self.xmin + cp.first*self.cell_width) + self.cell_width*(layer-1)
                x_dist = x_dist*x_dist

                if x_dist < min_dist.value:
                    for r in range(row_min, row_max+1):
                        examined_cells.append(Pair(r, l_col_min))
                        flag = self.get_closest_point_in_grid_cell(x, y, self.grid_points[l_col_min][r], closest_pt, min_dist)
                        done = done & (not flag)

            #traverse right column
            if l_col_max < self.grid_size:
                for r in range(row_min, row_max+1):
                    # get perp. distance to right column
                    x_dist = (((cp.first + 1) * self.cell_width + self.xmin) - x) + (layer-1)*self.cell_width
                    x_dist = x_dist * x_dist

                    if x_dist < min_dist.value:
                        for r in range(row_min, row_max + 1):
                            examined_cells.append(Pair(r, l_col_max))
                            flag = self.get_closest_point_in_grid_cell(x, y, self.grid_points[l_col_max][r],
                                                                       closest_pt, min_dist)
                            done = done & (not flag)

            done = done & (min_dist.value < float('inf'))

        return min_dist.value

    def get_closest_point_brute_force(self, x, y, closest_pt):
        min_dist = float('inf')
        for vert in self.ve:
            x2 = self.ce.get_x(vert)
            y2 = self.ce.get_y(vert)
            dist = self.distance_squared(x,y, x2, y2)
            if dist < min_dist:
                min_dist = dist
                closest_pt.first = x2
                closest_pt.second = y2

        return min_dist


    def get_layer_cells(self, x, y):

        #generate the layers, outwards from the center cell
        #each iteration we expand the layer by 1 cell in x and y
        #get grid index of source point

        cp = Pair(int(x), int(y))

        layer_cells = []
        for k in range(self.grid_size):
            layer_cells.append([])

        layer_cells[0].append(Pair(cp.second, cp.first))

        #iterate on layers, can have grid_size layers
        for layer in range(1, self.grid_size):

            #find the bounds of the layer
            l_col_min = cp.first - layer
            l_col_max = cp.first + layer
            l_row_min = cp.second - layer
            l_row_max = cp.second + layer

            #Process the layer, identifying the cells in the horizontal
            #and veritcal rows to be examined

            #limit col indices to be within the grid
            col_min = 0 if l_col_min < 0 else l_col_min
            col_max = self.grid_size-1 if l_col_max >= self.grid_size else l_col_max

            #travers bottom row
            if l_row_min >= 0:
                for c in range(col_min, col_max+1):
                    layer_cells[layer].append(Pair(l_row_min, c))

            #travers top row
            if l_row_max < self.grid_size:
                for c in range(col_min, col_max+1):
                    layer_cells[layer].append(Pair(l_row_max, c))

            #next process the two columns of the layer

            #first limit the row indices o be within the grid
            row_min = 0 if l_row_min < 0 else l_row_min
            row_max = self.grid_size - 1 if l_row_max >= self.grid_size else l_row_max

            #traverse left column
            if l_col_min >= 0:
                for r in range(row_min, row_max+1):
                    layer_cells[layer].append(Pair(r, l_col_min))

            #traverse right column
            if l_col_max < self.grid_size:
                for r in range(row_min, row_max+1):
                    layer_cells[layer].append(Pair(r, l_col_max))

        return layer_cells