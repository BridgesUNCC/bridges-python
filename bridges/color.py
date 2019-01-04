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
class Color(object):
    @property
    def red(self) -> int:
        """
        :return int: red component of color
        Must be a value between 0-255 inclusive
        """
        return self._red

    @red.setter
    def red(self, value: int):
        if value < 0 or value > 255:
            raise ValueError("Value for RGB attributes should range from 0-255 inclusive")

        self._red = value

    @red.deleter
    def red(self):
        del self._red

    @property
    def green(self) -> int:
        """
        :return int: green component of color
        Must be a value between 0-255 inclusive
        """
        return self._green

    @green.setter
    def green(self, value: int):
        if value < 0 or value > 255:
            raise ValueError("Value for RGB attributes should range from 0-255 inclusive")

        self._green = value

    @green.deleter
    def green(self):
        del self._green

    @property
    def blue(self) -> int:
        """
        :return int: blue component of color
        Must be a value between 0-255 inclusive
        """
        return self._blue

    @blue.setter
    def blue(self, value: int):
        if value < 0 or value > 255:
            raise ValueError("Value for RGB attributes should range from 0-255 inclusive")

        self._blue = value

    @blue.deleter
    def blue(self):
        del self._blue

    @property
    def alpha(self) -> float:
        """
        :return float: alpha component of color
        Must be a value between 0.0-1.0 inclusive
        """
        return self._alpha

    @alpha.setter
    def alpha(self, value: float):
        if value < 0.0 or value > 1.0:
            raise ValueError("Value for alpha should range from 0.0 - 1.0 inclusive")

        self._alpha = value

    @alpha.deleter
    def alpha(self):
        del self._alpha

    @property
    def rgba(self) -> (int, int, int, float):
        return self.red, self.green, self.blue, self.alpha

    @rgba.setter
    def rgba(self, rgba: (int, int, int, float)):
            self.red, self.blue, self.green, self.alpha = rgba

    @rgba.deleter
    def rgba(self):
        del self.red
        del self.blue
        del self.green
        del self.alpha

    #  alpha represents opacity from 0.0-1.0
    color_names = dict()

    ##
    #
    # Constructor, given r, g, b, a components
    #
    # @param r, g, b, a  - checked to be in the range 0-255
    # @param col_name - the name of a color for an element as string
    #
    def __init__(self, r=0, g=0, b=0, a: float = 0.0, col_name: str = None):
        """

        :param int r:
        :param int g:
        :param int b:
        :param float a:
        :param str col_name:
        """
        self._red = r
        self._green = g
        self._blue = b
        self._alpha = a

        if col_name is not None:
            self.set_color(col_name=col_name)

    # 	sets color to the given r, g, b, a components
    #
    #	@param r, g, b   - checked to be in the range 0-255
    #   @param a - checked to be in range 0.0-1.0
    #   @param col_name - name of color as string
    #
    def set_color(self, r: int = 0, g: int = 0, b: int =  0, a: float = 0.0, col_name: str = None):
        """

        :param int r:
        :param int g:
        :param int b:
        :param float a:
        :param str col_name:
        :return: None
        """
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
        else:
            self.red = r
            self.green = g
            self.blue = b
            self.alpha = a

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
    def get_byte_representation(self):
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

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return (self.red == other.red and
                self.green == other.green and
                self.blue == other.blue and
                self.alpha == other.alpha)
