#!/usr/bin/env python
from typing import List

import webcolors


class Color(object):
    """
    This class is used to represent colors in bridges.

    We use and RGBA model to represent colors, with the Red Green and Blue components ranging from 0-255,
    with the alpha ranging from 0.0-1.0 inclusive.

    We use webcolors to handle color names passed to the constructor/set_color function.
    https://www.w3.org/TR/css-color-3/#svg-color

    Color names are listed below:<br>

    aliceblue, antiquewhite, cyan, aquamarine, azure, beige, bisque, 
    black, blanchedalmond, blue, blueviolet, brown, burlywood, cadetblue, 
    chartreuse, chocolate, coral, cornflowerblue, cornsilk, crimson, 
    darkblue, darkcyan, darkgoldenrod, darkgrey, darkgreen, darkkhaki, 
    darkmagenta, darkolivegreen, darkorange, darkorchid, darkred, 
    darksalmon, darkseagreen, darkslateblue, darkslategrey, darkturquoise, 
    darkviolet, deeppink, deepskyblue, dimgrey, dodgerblue, firebrick, 
    floralwhite, forestgreen, magenta, gainsboro, ghostwhite, gold, 
    goldenrod, grey, green, greenyellow, honeydew, hotpink, indianred, 
    indigo, ivory, khaki, lavender, lavenderblush, lawngreen, 
    lemonchiffon, lightblue, lightcoral, lightcyan, lightgoldenrodyellow, 
    lightgrey, lightgreen, lightpink, lightsalmon, lightseagreen, 
    lightskyblue, lightslategrey, lightsteelblue, lightyellow, lime, 
    limegreen, linen, maroon, mediumaquamarine, mediumblue, mediumorchid, 
    mediumpurple, mediumseagreen, mediumslateblue, mediumspringgreen, 
    mediumturquoise, mediumvioletred, midnightblue, mintcream, mistyrose, 
    moccasin, navajowhite, navy, oldlace, olive, olivedrab, orange, 
    orangered, orchid, palegoldenrod, palegreen, paleturquoise, 
    palevioletred, papayawhip, peachpuff, peru, pink, plum, 
    powderblue, purple, red, rosybrown, royalblue, saddlebrown, 
    salmon, sandybrown, seagreen, seashell, sienna, silver, 
    skyblue, slateblue, slategrey, snow, springgreen, steelblue, tan, 
    teal, thistle, tomato, turquoise, violet, wheat, white, whitesmoke, 
    yellow, yellowgreen

    Attributes: red (int): red component of color ranging from 0-255 inclusive (default 0) green (int): green component of color ranging from 0-255 inclusive (default 0) blue (int): blue component of color ranging from 0-255 inclusive (default 0) alpha (float): alpha component of color ranging from 0.0-1.0 inclusive (default 1.0) rgba (tuple(int, int, int, alpha)): RGBA components as respective tuple
    Args:
        args: int, int, int, Optional(float) or a str as singular arg
        kwargs:
            r or red: Optional(int)
            b or blue: Optional(int)
            g or green: Optional(int)
            a or alpha: Optional(float)
            col_name: Optional(str)
    Raises:
        ValueError: if args is not 3 ints with an optional 4th arg for alpha or just one str arg
        ValueError: if a str passed is not a valid webcolor
        ValueError: if any of the RGBA values are outside of their respective range
    Examples:
        >>> my_color = Color("red")
        >>> my_color.rgba
        (255, 0, 0, 1.0)
        >>> my_color = Color(r=255)
        >>> my_color.rgba
        (255, 0, 0, 1.0)
        >>> my_color = Color(255, 0, 0)
        >>> my_color.rgba
        (255, 0, 0, 1.0)
        >>> my_color = Color()
        >>> my_color.red = 255
        >>> my_color.rgba
        (255, 0, 0, 1.0)
    """
    @property
    def red(self) -> int:
        """
        Getter for red component of color (0-255 inclusive)
        Returns:
            (int) red component of color
        """
        return self._red

    @red.setter
    def red(self, value: int):
        """
        Setter for red component of color (0-255 inclusive)
        Args:
            value(int): red component of color
        Returns:
            None
        """
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Value for RGB attributes must be able to be casted to int")
        if value < 0 or value > 255:
            raise ValueError("Value for RGB attributes should range from 0-255 inclusive")

        self._red = value

    @property
    def green(self) -> int:
        """
        Getter for green component of color (0-255 inclusive)
        Returns:
            int: green component of color
        """
        return self._green

    @green.setter
    def green(self, value: int): 
        """
        Setter for green component of color (0-255 inclusive)
        Args:
            value(int): green component of color
        Returns:
            None
        """
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Value for RGB attributes must able be to be casted to int")
        if value < 0 or value > 255:
            raise ValueError("Value for RGB attributes should range from 0-255 inclusive")

        self._green = int(value)

    @property
    def blue(self) -> int:
        """
        Getter for blue component of color (0-255 inclusive)
        Returns:
            int: blue component of color
        """
        return self._blue

    @blue.setter
    def blue(self, value: int):
        """
        Setter for blue component of color (0-255 inclusive)
        Args:
            value(int): blue component of color
        Returns:
            None
        """
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Value for RGB attributes must able be to be casted to int")
        if value < 0 or value > 255:
            raise ValueError("Value for RGB attributes should range from 0-255 inclusive")

        self._blue = int(value)

    @property
    def alpha(self) -> float:
        """
        Getter for alpha(opacity) component of color (0-1.0 inclusive)
        Returns:
            float: alpha component of color
        """
        return self._alpha

    @alpha.setter
    def alpha(self, value: float):
        """
        Setter for alpha component of color (0-1.0 inclusive)
        Args:
            value(float): alpha component of color (0-1.0)
        Returns:
            None
        """
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Value for Alpha must be able to be casted to float")
        if value < 0.0 or value > 1.0:
            raise ValueError("Value for alpha should range from 0.0 - 1.0 inclusive")

        self._alpha = value

    @property
    def rgba(self) -> (int, int, int, float):
        """
        RGBA components as respective tuple.  Represents the RGBA values of the color as a tuple, can be used to set or get all values at once
        Returns:
            (int, int, int, float) - RGBA values respectively
        """
        return self.red, self.green, self.blue, self.alpha

    @rgba.setter
    def rgba(self, rgba: (int, int, int, float)):
        """
        Set RGBA components.
        Args:
            rgba: r,g,b,a (list)
		Returns: 
            None
        """
        self.red, self.blue, self.green, self.alpha = rgba

    def __init__(self, *args, **kwargs):
        """ Constructor for a Color object
        Usage: requires either 3 ints 0-255 for RGB and an optional float 0.0-1.0 for alpha or a str of a web color can also key the RGBA values with r, g, b, a or red, green, blue, alpha respectively and col_name for the str
        Args:
            args: int, int, int, optional float or just a str
            kwargs: r/red: int, b/blue: int, g/green: int optional a/alpha: float or col_name: str
        Returns:
            None
        """
        self._red = 0
        self._green = 0
        self._blue = 0
        self._alpha = 1.0
        self.set_color(*args, **kwargs)

    def set_color(self, *args, **kwargs) -> None:
        """
        Sets color for a an element or link. Requires either 3 ints 0-255 for RGB and an optional float 0.0-1.0 for alpha or a str of a web color can also key the RGBA values with r, g, b, a or red, green, blue, alpha respectively and col_name for the str
        Args:
            args: int, int, int optional float or str
            kwargs: r/red: int, b/blue: int, g/green: int optional a/alpha: float or col_name: str
        """
        col_name = None
        if args:
            errorcondition = True
            if len(args) == 1 and type(args[0]) == list:
                self.red = args[0][0]
                self.green = args[0][1]
                self.blue = args[0][2]
                self.alpha = args[0][3]
                errorcondition=False
            if len(args) == 4 or len(args) == 3:
                self.red = args[0]
                self.green = args[1]
                self.blue = args[2]
                if len(args) == 4:
                    self.alpha = args[3]
                errorcondition = False
            elif len(args) == 1:
                if type(args[0]) is str:
                    col_name = args[0]
                    errorcondition=False
                elif type(args[0]) is Color:
                    self.red = args[0].red
                    self.green = args[0].green
                    self.blue = args[0].blue
                    self.alpha = args[0].alpha
                    errorcondition = False
            if errorcondition:
                raise ValueError("To use Color constructor pass 3 RGB values and a float alpha value or a color name or a Color object")
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

    def get_byte_representation(self) -> list:
        """
        Gets the RGBA values as list of ints from 0-255
        Returns:
            byte representation of color
        """
        r = self.red
        g = self.green
        b = self.blue
        a = round(255 * self.alpha)

        bytebuffer = list()
        bytebuffer.append(r)
        bytebuffer.append(g)
        bytebuffer.append(b)
        bytebuffer.append(a)

        return bytebuffer

    def __eq__(self, other):
        """deep equality check, by value of each RGBA value"""
        if not isinstance(other, self.__class__):
            return False

        return (self.red == other.red and
                self.green == other.green and
                self.blue == other.blue and
                self.alpha == other.alpha)
