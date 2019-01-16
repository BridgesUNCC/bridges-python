from bridges.bridges import *
from bridges.color_grid import *
from bridges.color import *

def main():
    # Initialize BRIDGES with your credentials
    bridges = Bridges(0, "test", "211416381091")

    bridges.connector.set_server("local")

    sizei = 25
    sizej = 35

    cg1 = ColorGrid(sizei, sizej)

    for i in range(sizei):
        for j in range(sizej):
            if (i+j) % 2 == 0:
                cg1.set(i,j,Color(0,0,0))
            else:
                cg1.set(i,j,Color(255,255,255))

    bridges.set_data_structure(cg1)
    bridges.visualize()

    cg = bridges.get_color_grid_from_assignment(bridges.get_username(), bridges.get_assignment_id(), 0)

    dims = cg.get_dimensions()
    for k in range(int(dims[1] / 2 - 5), int(dims[1]/2+5)):
        for j in range(int(dims[0]/2-5), int(dims[0]/2 + 5)):
            cg.set(k,j,Color("red"))

    bridges.set_data_structure(cg)
    bridges.visualize()

if __name__ == '__main__':
    main()

