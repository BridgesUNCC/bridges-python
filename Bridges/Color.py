#!/usr/bin/env python

#import bridges.validation.InvalidValueException
import base64


##
#	@brief This class is used to represent colors in BRIDGES.
#
#	We use an RGBA model
#	to represent colors, with each component in the range 0-255. BRIDGES
#	also supports named colors for user convenience, but these are converted
#	into [RGBA] prior to transmission to the server for visualization.
#
# 	<p>
#
#	@author K.R. Subramanian,
#	@date 7/14/16
#
#
class Color():
    red = 70
    green = 130
    blue = 180
    alpha = 1.0

    #  alpha represents opacity from 0.0-1.0
    color_names = dict()

    ##
    #
    # Constructor, given r, g, b, a components
    #
    # @param r, g, b, a  - checked to be in the range 0-255
    # @param col_name - the name of a color for an element as string
    #
    def __init__(self, col_name = None, r = None, g = None, b = None, a = None):
        if col_name is not None:
            self.set_color(col_name)
        else:
            self.set_color(r = r, g = g, b = b, a = a)


    ##
    #
    # 	sets color to the given r, g, b, a components
    #
    #	@param r, g, b, a  - checked to be in the range 0-255
    #   @param col_name - name of color as string
    #
    def set_color(self, col_name = None, r= None, g = None, b = None, a = None):
        #  check color component ranges
        if col_name is not None:
            if col_name == "red":
                self.red = 255
                self.green = 0
                self.blue = 0
                self.alpha = 1.0
                return
            elif col_name == "green":
                self.red = 0
                self.green = 255
                self.blue = 0
                self.alpha = 1.0
                return
            elif col_name == "blue":
                self.red = 0
                self.green = 0
                self.blue = 255
                self.alpha = 1.0
                return
            elif col_name == "yellow":
                self.red = 255
                self.green = 255
                self.blue = 0
                self.alpha = 1.0
                return
            elif col_name == "cyan":
                self.red = 0
                self.green = 255
                self.blue = 255
                self.alpha = 1.0
                return
            elif col_name == "magenta":
                self.red = 255
                self.green = 0
                self.blue = 255
                self.alpha = 1.0
                return
            elif col_name == "white":
                self.red = 255
                self.green = 255
                self.blue = 255
                self.alpha = 1.0
                return
            elif col_name == "black":
                self.red = 0
                self.green = 0
                self.blue = 0
                self.alpha = 1.0
                return
            elif col_name == "orange":
                self.red = 255
                self.green = 155
                self.blue = 0
                self.alpha = 1.0
                return
            elif col_name == "turquoise":
                self.red = 173
                self.green = 234
                self.blue = 234
                self.alpha = 1.0
                return
            elif col_name == "maroon":
                self.red = 176
                self.green = 48
                self.blue = 96
                self.alpha = 1.0
                return
            elif col_name == "aquamarine":
                self.red = 127
                self.green = 255
                self.blue = 212
                self.alpha = 1.0
                return
            elif col_name == "azure":
                self.red = 240
                self.green = 255
                self.blue = 255
                self.alpha = 1.0
                return
            elif col_name == "beige":
                self.red = 245
                self.green = 245
                self.blue = 220
                self.alpha = 1.0
                return
            elif col_name == "brown":
                self.red = 166
                self.green = 42
                self.blue = 42
                self.alpha = 1.0
                return
            elif col_name == "tan":
                self.red = 210
                self.green = 180
                self.blue = 140
                self.alpha = 1.0
                return
            elif col_name == "olive":
                self.red = 128
                self.green = 128
                self.blue = 0
                self.alpha = 1.0
                return
            elif col_name == "chartreuse":
                self.red = 127
                self.green = 255
                self.blue = 0
                self.alpha = 1.0
                return
            elif col_name == "khaki":
                self.red = 240
                self.green = 230
                self.blue = 140
                self.alpha = 1.0
                return
            elif col_name == "bisque":
                self.red = 255
                self.green = 228
                self.blue = 196
                self.alpha = 1.0
                return
            elif col_name == "coral":
                self.red = 255
                self.green = 127
                self.blue = 0
                self.alpha = 1.0
                return
            elif col_name == "pink":
                self.red = 255
                self.green = 192
                self.blue = 203
                self.alpha = 1.0
                return
            elif col_name == "lavender":
                self.red = 230
                self.green = 230
                self.blue = 250
                self.alpha = 1.0
                return
            elif col_name == "purple":
                self.red = 160
                self.green = 32
                self.blue = 240
                self.alpha = 1.0
                return
            elif col_name == "gold":
                self.red = 255
                self.green = 215
                self.blue = 0
                self.alpha = 1.0
                return
        elif (r >= 0 and r <= 255 and g >= 0 and g <= 255 and b >= 0 and b <= 255 and a >= 0.0 and a <= 1.0):
            self.red = r
            self.green = g
            self.blue = b
            self.alpha = a
            return

        raise ValueError("Invalid color range (r,g,b must be 0-255, alpha in 0-1)\n")

    ##
    #
    # 	sets the red component
    #
    # @param r  - checked to be in the range 0-255
    #
    #
    def set_red(self, r):
        if r>=0 and r<=255:
            self.red = r
            return
        raise ValueError("Invalid color range(red):" + " must be in the range 0-255\n")

    ##
    #
    # 	gets the red component
    #
    # 	@return  red - returns the red component of the color
    #
    #
    def get_red(self):
        return self.red

    ##
    #
    # 	sets the green component
    #
    # 	@param g  - checked to be in the range 0-255
    #
    #
    def set_green(self, g):
        if g >= 0 and g <= 255:
            self.green = g
            return
        raise ValueError("Invalid color range(green):" + " must be in the range 0-255\n")

    ##
    #
    # 	gets the green component
    #
    # 	@return  green - returns the green component of the color
    #
    #
    def get_green(self):
        return self.green

    ##
    #
    # 	sets the blue component
    #
    # 	@param b  - checked to be in the range 0-255
    #
    #
    def set_blue(self, b):
        if b >= 0 and b <= 255:
            self.blue = b
            return
        raise ValueError("Invalid color range(blue):" + " must be in the range 0-255\n")

    ##
    #
    # 	gets the blue component
    #
    # 	@return  blue - returns the blue component of the color
    #
    #
    def get_blue(self):
        return self.blue

    ##
    #
    # 	sets the alpha(opacity) component
    #
    # 	@param a  - checked to be in the range 0-255
    #
    #
    def set_alpha(self, a):
        if a >= 0.0 and a <= 1.0:
            self.alpha = a
            return
        raise ValueError("Invalid color range(alpha):" + " must be in the range 0.0-1.0\n")

    ##
    #
    # 	gets the alpha component
    #
    # 	@return  alpha - returns the alpha(opacity) component of the color
    #
    #
    def get_alpha(self):
        return self.alpha

    ##
    # gets a Byte representation of a color
    #
    # @return - returns the RGBA color as a byte array
    #
    def getByteRepresentation(self):
        r = self.red
        g = self.green
        b = self.blue
        a = round(255 * self.alpha)

        # rd = r.to_bytes(10, byteorder='little')
        # gn = g.to_bytes(10, byteorder='little')
        # bl = b.to_bytes(10, byteorder='little')
        # al = a.to_bytes(10, byteorder='little')


        bytebuffer = []
        bytebuffer.append(r)
        bytebuffer.append(g)
        bytebuffer.append(b)
        bytebuffer.append(a)

        return bytebuffer
