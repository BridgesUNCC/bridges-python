from bridges import *
from tests.comp_e import *
from tests.uniform_grid_spatial_index_2d import *

from random import *

def main():

    #create the bridges object and set the credentials
    bridges = Bridges(5, "test", "988181220044")

    bridges.set_title("Spatial Indexing")
    bridges.set_description("Computes the closest point from a given point, using Open Street Map Data")
    bridges.server = "local"

    #get open street map data, using New York, with secondary road data
    osm_data = get_osm_data("New York, New York", "secondary")

    #get the vertices
    vertices = osm_data.vertices
    print("total vertices: " + str(len(vertices)))

    ce = CompEOSM()

    #create the uniform grid spatial index object
    ugsi = UniformGridSpatialIndex2D(vertices, ce, 10)

    #use a color grid to display cells examined and layers
    cg = ColorGrid(10, 10, Color("white"))

    examined_cells = []

    #pick points at random from the vertices, compute the closest
    #point, then do the same with brute force algorithm and check
    #if they match

    closest_pt = Pair(0.0, 0.0)

    #get the range of vertices in x and y, we will make a query points
    # to be inside the bounding box of the domain
    minx = 10000000
    miny = 10000000
    maxx = -10000000
    maxy = -10000000

    for v in vertices:
        x = v.longitude
        y = v.latitude
        minx = x if x < minx else minx
        maxx = x if x > maxx else maxx
        miny = y if y < miny else miny
        maxy = y if y > maxy else maxy

    """
    we will run it with the efficient algorithm, then with brute force
	and make sure the same points are returned. We will compute the
    difference in distances to ensure our algorithm is working
	we will test with 100 randomly  chosen (x,y) positions within
	the grid 
    """

    num_points = 1
    for i in range(num_points):
        examined_cells.clear()

        #choose a point inside the bounding box of points
        x = random() * (maxx-minx) + minx
        y = random() * (maxy-miny) + miny
        print(str(i) + "Source Point: " + str(x) + "," + str(y))
        dist = ugsi.get_closest_point(x, y, closest_pt, examined_cells)
        print(str(i) + "ALG Closest Point: " + str(closest_pt.first) + "," + str(closest_pt.second))

        dist1 = math.sqrt(dist)
        print("ALG Min dist: " + str(dist1))

        #test with brute force
        dist = ugsi.get_closest_point_brute_force(x, y, closest_pt)
        dist2 = math.sqrt(dist)
        print("BFA Closest Point: " + str(closest_pt.first) + "," + str(closest_pt.second))

        diff = dist1-dist2
        diff = -diff if diff < 0.0 else diff
        print("BFA Min Dist: " + str(dist2))
        print("Difference: " + str(diff))

    """
    we can also look at the cells that were examined by the algorithm
	in determining teh closest point. We show an example of that
	by displaying it on the color grid
	choose a point inside the bounding box of the points
	I iterated a few times to get a case that gets more than one cell
	examined!
    """
    x = 0.0
    y = 0.0
    for i in range(10):
        x = random() * (maxx - minx) + minx
        y = random() * (maxy - miny) + miny
        print("Source Point: " + str(x) + "," + str(y))

    examined_cells.clear()
    dist = ugsi.get_closest_point(x, y, closest_pt, examined_cells)
    print("num cells examined:" + str(len(examined_cells)))
    print("closest point: " + str(closest_pt.first) + "," + str(closest_pt.second))
    print("distance: " + str(math.sqrt(dist)))
    for i in range(10):
        for j in range(10):
            cg.set(i, j, Color("white"))
    for k in range(len(examined_cells)):
        #we will keep changing the colors for each cell
        j = k%6
        c = color_switch(j)
        cg.set(examined_cells[k].first, examined_cells[k].second, Color(c))

    bridges.set_data_structure(cg)
    bridges.visualize()


    #also can illustrate the layers generated starting from a cell
    #in the grid this is illustrated below
    layer_cells = ugsi.get_layer_cells(3.0, 2.0)

    for i in range(cg.grid_size[1]):
        for j in range(cg.grid_size[0]):
            cg.set(i, j, Color("white"))

    k = 0
    for layer in layer_cells:
        k = k%6
        c = color_switch(k)
        for cell in layer:
            cg.set(cell.second, cell.first, Color(c))
        k += 1

    bridges.visualize()

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

if __name__ == "__main__":
    main()