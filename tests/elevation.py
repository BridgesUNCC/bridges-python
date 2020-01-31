from bridges.color_grid import *
from bridges.bridges import *
from bridges.color import *
from bridges.data_src_dependent import data_source
import sys
import os

def main():
    # This example illustrates using the Bridges color grid
    # We will build a checker grid using two different colors


    # create the Bridges object, set credentials
    bridges = Bridges(999, "jstrahler", "209382050691")


    """white = Color(col_name="white") 

    # create a 100x100 color grid
    width = 100
    height = 100
    cg = ColorGrid(width, height, white)

    num_squares_x = 100
    num_squares_y = 100

    sq_width = width / num_squares_x
    sq_height = width / num_squares_y

    
    #TODO: import data file

    #TODO: change for loops to loop through data 
    for j in range(num_squares_y):
        for k in range(num_squares_x):
            
            #TODO: color algortihm based on ele data

            col = white
            # find the address of the square
            origin_x = k * sq_width
            origin_y = j * sq_height

            # color the square
            if (os.path.isfile("e.asc")):
                f = open("e.asc")
                #data = f.read()
            n = 0
            a = []
            y=0
            for line in f:
                if (n<6):
                    n += 1
                    continue
                temp = line.split(" ")
                del temp[0]
                #print(len(temp))
                a.append(temp)
                maxVal = 0
                for co in temp:
                    if (int(co) > maxVal):
                        maxVal = int(co)

            for y in range(int(origin_y), int(origin_y + sq_height)):
                for x in range(int(origin_x), int(origin_x + sq_width)):
                    try:
                        g = (int(a[y][x]) / maxVal)*(255)
                        t = Color(g,g,g)
                        
                    except Exception as e:
                        #print(e)
                        t = Color(col_name="black")
                    cg.set(x, y, t)
                    x = x + 1
                y = y + 1

    bridges.set_data_structure(cg)

    bridges.visualize()
    """



    ele_obj = data_source.get_elevation_data([-98.02593749997456,41.03133177632377,-97.94531249997696,41.508577297430456])
    print(ele_obj.cols)
    print(ele_obj.rows)
    print(ele_obj._xll)
    print(ele_obj._yll)
    print(ele_obj.cellsize)
    print(ele_obj.data)

    

if __name__ == "__main__":
    main()