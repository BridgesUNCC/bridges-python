#!/usr/bin/env python
import webcolors


class Color(object):
    """This class is used to represent colors in bridges.

    We use and RGBA model to represent colors, with the Red Green and Blue components ranging from 0-255,
    with the alpha ranging from 0.0-1.0 inclusive.

    We use webcolors to handle color names passed to the constructor/set_color function.
    https://webcolors.readthedocs.io/en/1.8.1/
    All CSS3 color names should be valid:
    https://developer.mozilla.org/en-US/docs/Web/CSS/color_value
    https://www.w3.org/TR/css-color-3/#svg-color

    Attributes:
        red (int): red component of color ranging from 0-255 inclusive (default 0)
        green (int): green component of color ranging from 0-255 inclusive (default 0)
        blue (int): blue component of color ranging from 0-255 inclusive (default 0)
        alpha (float): alpha component of color ranging from 0.0-1.0 inclusive (default 1.0)
        rgba (tuple(int, int, int, alpha)): RGBA components as respective tuple
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
        """red component of color
        :return int: red component of color
        Must be a value between 0-255 inclusive
        """
        return self._red

    @red.setter
    def red(self, value: int):
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Value for RGB attributes must be able to be casted to int")
        if value < 0 or value > 255:
            raise ValueError("Value for RGB attributes should range from 0-255 inclusive")

        self._red = value

    @red.deleter
    def red(self):
        del self._red

    @property
    def green(self) -> int:
        """green component of color
        :return int: green component of color
        Must be a value between 0-255 inclusive
        """
        return self._green

    @green.setter
    def green(self, value: int):
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Value for RGB attributes must able be to be casted to int")
        if value < 0 or value > 255:
            raise ValueError("Value for RGB attributes should range from 0-255 inclusive")

        self._green = int(value)

    @green.deleter
    def green(self):
        del self._green

    @property
    def blue(self) -> int:
        """blue component of color
        :return int: blue component of color
        Must be a value between 0-255 inclusive
        """
        return self._blue

    @blue.setter
    def blue(self, value: int):
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Value for RGB attributes must able be to be casted to int")
        if value < 0 or value > 255:
            raise ValueError("Value for RGB attributes should range from 0-255 inclusive")

        self._blue = int(value)

    @blue.deleter
    def blue(self):
        del self._blue

    @property
    def alpha(self) -> float:
        """alpha component of color
        :return float: alpha component of color
        Must be a value between 0.0-1.0 inclusive
        """
        return self._alpha

    @alpha.setter
    def alpha(self, value: float):
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Value for Alpha must be able to be casted to float")
        if value < 0.0 or value > 1.0:
            raise ValueError("Value for alpha should range from 0.0 - 1.0 inclusive")

        self._alpha = value

    @alpha.deleter
    def alpha(self):
        del self._alpha

    @property
    def rgba(self) -> (int, int, int, float):
        """RGBA components as respective tuple
        Represents the RGBA values of the color as a tuple, can be used to set or get all values at once
        :return (int, int, int, float): RGBA values respectively
        """
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

    def __init__(self, *args, **kwargs):
        """ Constructor for a Color object
        Usage: requires either 3 ints 0-255 for RGB and an optional float 0.0-1.0 for alpha or a str of a web color
        can also key the RGBA values with r, g, b, a or red, green, blue, alpha respectively and col_name for the str
        :param args: int, int, int, optional float or just a str
        :param kwargs: r/red: int, b/blue: int, g/green: int optional a/alpha: float or col_name: str
        :return: None
        """
        self._red = 0
        self._green = 0
        self._blue = 0
        self._alpha = 1.0
        self.set_color(*args, **kwargs)

    def set_color(self, *args, **kwargs) -> None:
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

    def set_red(self, r: int) -> None:
        """:param int r: Must be a value between 0-255 inclusive"""
        self.red = r

    def get_red(self) -> int:
        """:return int: red component of color"""
        return self.red

    def set_green(self, g: int) -> None:
        """:param int g: Must be a value between 0-255 inclusive"""
        self.green = g

    def get_green(self) -> int:
        """:return int: green component of color"""
        return self.green

    def set_blue(self, b: int) -> None:
        """:param int b: Must be a value between 0-255 inclusive"""
        self.blue = b

    def get_blue(self) -> int:
        """":return int: blue component of color"""
        return self.blue

    def set_alpha(self, a: float) -> None:
        """:param float a: Must be a value between 0.0-1.0 inclusive"""
        self.alpha = a

    def get_alpha(self) -> float:
        """:return float: alpha component of color"""
        return self.alpha

    def get_byte_representation(self) -> list:
        """:return list(int):RGBA values as list of ints from 0-255"""
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
