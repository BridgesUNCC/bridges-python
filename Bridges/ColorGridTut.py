from Bridges.ColorGrid import *
from Bridges.Bridges import *
from Bridges.Color import *

class ColorGridTut:

    # This example illustrates using the Bridges color grid
    # We will build a checker grid using two different colors

    # Initialize BRIDGES
    bridges = Bridges(120, "test", "1343747370122")

    # set title fo visualization
    bridges.setTitle("A Checkerboard Example Using Grid Type")

    width = 200
    height = 200

    blue = Color(col_name= "blue")
    red = Color(col_name= "red")

    cg = ColorGrid(width, height, red)

    # create a checkerboard pattern
    # 10x10 grid
    num_squares_x = 10
    num_squares_y = 10

    sq_width = width/num_squares_x
    sq_height = width/num_squares_y

    for j in range(num_squares_y):
        for k in range(num_squares_x):

            # use even/odd value of pixel to figure out the color of the squares
            x_even = k%2 == 0
            y_even = j%2 == 0

            if(y_even == True):
                if(x_even == True):
                    col = red
                else:
                    col = blue
            else:
                if(x_even == True):
                    col = blue
                else:
                    col = red

            # find the address of the square
            origin_x = k*sq_width
            origin_y = j*sq_height

            #color the square
            y = origin_y
            print(y)
            x = origin_x
            for y in range(int(origin_y), int(origin_y+sq_height)):
                for x in range(int(origin_x), int(origin_x+sq_width)):
                    print(x,y)
                    cg.set(x, y, col)
                    x = x + 1
                y = y + 1

    bridges.set_data_structure(cg)

    bridges.visualize()

