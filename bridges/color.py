#!/usr/bin/env python
import webcolors

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

        self._red = int(value)

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

        self._green = int(value)

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

        self._blue = int(value)

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
    #def __init__(self, r=0, g=0, b=0, a: float = 0.0, col_name: str = None):
    def __init__(self, *args, **kwargs):
        """
        Usage: requires either 3 ints 0-255 for RGB and an optional float 0.0-1.0 for alpha or a str of a web color
        can also key the RGBA values with r, g, b, a or red, green, blue, alpha respectively and col_name for the str
        :param args: int, int, int optional float or str
        :param kwargs: r/red: int, b/blue: int, g/green: int optional a/alpha: float or col_name: str
        :return: None
        """
        self._red = 0
        self._green = 0
        self._blue = 0
        self._alpha = 1.0
        self.set_color(*args, **kwargs)

    # 	sets color to the given r, g, b, a components
    #
    #	@param r, g, b   - checked to be in the range 0-255
    #   @param a - checked to be in range 0.0-1.0
    #   @param col_name - name of color as string
    #
    def set_color(self, *args, **kwargs):
        """
        Usage: requires either 3 ints 0-255 for RGB and an optional float 0.0-1.0 for alpha or a str of a web color
        can also key the RGBA values with r, g, b, a or red, green, blue, alpha respectively and col_name for the str
        :param args: int, int, int optional float or str
        :param kwargs: r/red: int, b/blue: int, g/green: int optional a/alpha: float or col_name: str
        :return: None
        """
        col_name = None
        if args:
            if len(args) == 4 or len(args) == 3:
                self.red = args[0]
                self.green = args[1]
                self.blue = args[2]
                if len(args) == 4:
                    self.alpha = args[3]
            elif len(args) == 1:
                if type(args[0]) is str:
                    col_name = args[0]
            else:
                raise ValueError("To use Color constructor pass 3 RGB values and a float alpha value or a color name")
        elif kwargs:
            if 'col_name' in kwargs:
                col_name = kwargs['col_name']
            if 'r' in kwargs:
                self.red = kwargs['r']
            if 'red' in kwargs:
                self.red = kwargs['red']
            if 'g' in kwargs:
                self.green = kwargs['g']
            if 'green' in kwargs:
                self.green = kwargs['green']
            if 'b' in kwargs:
                self.blue = kwargs['b']
            if 'blue' in kwargs:
                self.blue = kwargs['blue']
            if 'a' in kwargs:
                self.alpha = kwargs['a']
            if 'alpha' in kwargs:
                self.alpha = kwargs['alpha']

        if col_name is not None:
            try:
                web_color = webcolors.name_to_rgb(col_name)
                self.set_color(web_color.red, web_color.green, web_color.blue)
            except ValueError:
                raise ValueError(col_name + " is not a valid color name")

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
