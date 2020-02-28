from bridges import *
from bridges.data_src_dependent import data_source

class Image():
    def __init__(self):
        self.ele_obj = data_source.get_elevation_data([6.020558108041891,46.10757941505641,9.707863253414155,47.77059916141684]) #Switzerland
        
        # Create the image file header
        self.header = "Hello"
        
        self.width = int(self.ele_obj.cols) 
        self.height = int(self.ele_obj.rows) 
        self.max_val = int(self.ele_obj.maxVal)
            
        self.data = self.ele_obj.data
        self.pixee = []
        # Read the actual image data
        x_val = 0
        y_val = 0
        

        while (y_val < len(self.data)):
            x_val = 0
            while (x_val < len(self.data[y_val])):
                self.pixee.append([y_val, x_val, int(self.data[y_val][x_val])])
                x_val += 1
            y_val += 1
        

    def get_pixel(self, x, y):
        # Return the color of the pixel at x y
        return self.pixee[x + y * self.width]

    def get_image(self):
        # Return this image as a ColorGrid image
        cg = ColorGrid(self.height, self.width)

        for y in range(self.height):
            for x in range(self.width):
                pix = self.get_pixel(x, y)
                if(pix[0] == 255 and pix[1] == 0 and pix[2] == 0):
                    cg.set(y, x, Color(255, 0, 0))
                else:
                    cg.set(y, x, Color(pix[2]*255/self.max_val, pix[2]*255/self.max_val, pix[2]*255/self.max_val))

        return cg

    def set_pixel(self, x, y, color):
        # Set the color of the pixel at x, y
        self.pixee[x + y * self.width] = color

    def greedy_path(self, start_y):
        # Run the greedy path from (0, start_y) to the right of the image
        
        current = [0, start_y]
        self.set_pixel(current[0], current[1], [255, 0, 0])

        # Check the least of the 3 right pixels and move there
        for x in range(self.width-1):
            least = current[1]
            for y in [-1, 1]:
                # Out of bounds of the image just skip
                if current[1] + y <= 0 or current[1] + y > self.height:
                    continue

                if self.get_pixel(current[0] + 1, least)[2] < self.get_pixel(current[0] + 1, current[1] + y)[2]:
                    least = current[1] + y
            
            current[0] += 1
            current[1] = least
            self.set_pixel(current[0], current[1], [255, 0, 0])


def main():
    bridges = Bridges(107, "test", "137842425086")

    bridges.set_title("Mountain Paths - Greedy Algorithms Example")
    bridges.set_description("Path through the mountains through the lowest elevation.")

    img = Image()

    img.greedy_path(img.height // 2)

    bridges.set_data_structure(img.get_image())
    bridges.visualize()

if __name__ == '__main__':
    main()