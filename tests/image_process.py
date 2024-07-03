from bridges import *
from tests.image import *

def main():

    bridges = Bridges(40, "test", "137842425086")

    #read input image
    img = Image()
    img.read('./yosemite.ppm')

    #create BRIDGES color grid
    cg = ColorGrid(img.height, img.width)

    #display the original image
    img.set_color_grid(cg, False)
    bridges.set_data_structure(cg)
    bridges.visualize()

    #convert to grayscale and display
    img.to_gray_scale()
    img.set_color_grid(cg, True)
    bridges.set_data_structure(cg)
    bridges.visualize()

    #flip rows horizontally and display
    img.flip_horizontal()
    img.set_color_grid(cg, True)
    bridges.set_data_structure(cg)
    bridges.visualize()

    #flatten blue component and display
    img.flatten_blue()
    img.set_color_grid(cg, True)
    bridges.set_data_structure(cg)
    bridges.visualize()

    # flatten red component and display
    img.flatten_red()
    img.set_color_grid(cg, True)
    bridges.set_data_structure(cg)
    bridges.visualize()

    #blend images and display
    img.blend('./Lenna.ppm', 0.5)
    img.set_color_grid(cg, True)
    bridges.set_data_structure(cg)
    bridges.visualize()

if __name__ == '__main__':
    main()
