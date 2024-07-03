from bridges import *
from scipy.misc import imread
class Image:


    def __init__(self, **kwargs):
        """
        Constructor
        :param kwargs:
            string input_file: the path to the ppm file
            int width: the width of the image
            int height: the height of the image
        """
        if kwargs.get("input_file"):
            self.read(kwargs['input_file'])
        if kwargs.get("width") and kwargs.get("height"):
            self.image_array = []
            self.processed_array = []
            self.width = kwargs['width']
            self.height = kwargs['height']
        else:
            self.width = self.height = self.maxVal = 0
            self.image_array = None
            self.processed_array = None

    #reads an image from the given input image
    def read(self, file_name):
        data = []
        with open(file_name, 'r') as ppm:
            for line in ppm:
                for s in line.split():
                    data.append(s)

        self.magic = data[0]
        self.width = int(float(data[1]))
        self.height = int(float(data[2]))
        self.max_val = int(data[3])

        print("Header: " + self.magic + " " + str(self.width) + " " + str(self.height) + " " + str(self.max_val))

        if self.image_array is None:
            self.image_array = []

        if self.processed_array is None:
            self.processed_array = []

        k = 4
        #read the pixels
        for i in range(self.height * self.width * 3):
            self.image_array.append(int(data[k]))
            self.processed_array.append(None)
            k += 1

    #displays image using the BRIDGES color grid
    def set_color_grid(self, cg, processed):
        n = 0
        print(self.processed_array, processed)
        for j in range(self.height):
            for k in range(self.width):
                if processed:
                    cg.set(j, k, Color(self.processed_array[n], self.processed_array[n+1], self.processed_array[n+2]))
                else:
                    cg.set(j, k, Color(self.image_array[n], self.image_array[n+1], self.image_array[n+2]))

                n+= 3

    def to_gray_scale(self):
        k = 0
        for i in range(self.height):
            for j in range(self.width):
                r = float(self.image_array[k])
                g = float(self.image_array[k+1])
                b = float(self.image_array[k+2])

                #compute the gray value
                gray = int(r* 0.299 + g * 0.587 + b* 0.144)
                #store in the processed array
                self.processed_array[k] = self.processed_array[k+1] = self.processed_array[k+2] = max(0, min(gray, 255))
                k+=3


    def flip_horizontal(self):
        k = 0
        for i in range(self.height):
            for j in range(int(self.width/2)):
                n = (i*self.width + j)*3
                m = (i*self.width + (self.width - j - 1))*3

                #swap the nth and mth pixels
                tmp = [self.image_array[n], self.image_array[n+1], self.image_array[n+2]]

                self.processed_array[n] = self.image_array[m]
                self.processed_array[n+1] = self.image_array[m+1]
                self.processed_array[n+2] = self.image_array[m+2]
                self.processed_array[m] = tmp[0]
                self.processed_array[m+1] = tmp[1]
                self.processed_array[m+2]= tmp[2]

    def flatten_blue(self):
        k = 0
        for i in range(self.height):
            for j in range(self.width):
                self.processed_array[k] = self.image_array[k]
                self.processed_array[k+1] = self.image_array[k+1]
                self.processed_array[k+2] = 0
                k += 3

    def flatten_red(self):
        k = 0
        for i in range(self.height):
            for j in range(self.width):
                self.processed_array[k] = 255 - int(self.image_array[k])
                self.processed_array[k+1] = int(self.image_array[k + 1])
                self.processed_array[k+2] = int(self.image_array[k + 2])
                k += 3

    #reads the new image and blends with existing image
    def blend(self, file_name, blend_factor):
        w = 0
        h = 0
        data = []

        #assumes a ppm file
        with open(file_name, 'r') as ppm:
            for line in ppm:
                for s in line.split():
                    data.append(s)

        w = int(data[1])
        h = int(data[2])
        max_val = int(data[3])

        #center the incoming image
        x2_min = (self.width - w)/2
        x2_max = x2_min + w
        y2_min = (self.height - h)/2
        y2_max = y2_min + h

        x_offset = (self.width - w)/2
        y_offset = (self.height - h)/2
        pix_addr = 0
        k = 4
        for i in range(self.height):
            for j in range(self.width):
                pix_addr = i*self.width*3 + j*3

                #read and blend pixels withing range
                if (i>=y2_min) and (i < y2_max) and (j >= x2_min) and (j < x2_max):
                    r = int(data[k])
                    k += 1
                    g = int(data[k])
                    k +=1
                    b = int(data[k])
                    k += 1
                    print(k)
                    r2 = int((blend_factor * r + (1-blend_factor)*int(self.image_array[pix_addr])))
                    g2 = int((blend_factor * g + (1-blend_factor)*int(self.image_array[pix_addr+1])))
                    b2 = int((blend_factor * b + (1-blend_factor)*int(self.image_array[pix_addr+2])))


                    self.processed_array[pix_addr] = r2
                    self.processed_array[pix_addr+1] = g2
                    self.processed_array[pix_addr+2] = b2

                else:

                    self.processed_array[pix_addr] = self.image_array[pix_addr]
                    self.processed_array[pix_addr+1] = self.image_array[pix_addr+1]
                    self.processed_array[pix_addr+2] = self.image_array[pix_addr+2]

                pix_addr += 3
