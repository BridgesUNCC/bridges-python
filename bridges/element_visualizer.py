#!/usr/bin/env python
from decimal import Decimal
from bridges.element import *
from bridges.color import *
from decimal import Decimal
##
# This class is used to store the visualization elements on the for the bridges
# Visualization, including the color, shape, opacity, and size of the node.
# <p>
# Objects of this class are stored as properties of all Element subclasses.
# Generally, you will manipulating the ElementVisualizer returned from the
# Element getVisualizer() method, and then call the setVisualizer() method on
# the Element after changes have been made.
#
class ElementVisualizer():

    def __init__(self, color="green", shape ="circle", size=10.0, opacity=1.0):
        """
        ElementVisualizer constuctor
        kwargs:
            (str) color: color for this element
            (str) shape: the shape of the element
            (float) size: the elements size
            (float) opacity: the elements opacity
        Returns:
            None
        """
        self.prop = dict()
        self._color = Color(70, 130, 180, 1.0)
        if color is not "green":
            self.color = color
        self._shape = shape
        self._size = size
        self._opacity = opacity
        self._locationX = Decimal("Infinity")
        self._locationY = Decimal("Infinity")
        self.prop['color'] = ["70", "130", "180", "1.0"]
        self.prop["opacity"] = "1.0"
        self.prop["size"] = "10.0"
        self.prop["shape"] = "circle"
        self.prop["key"] = ""
        self.prop["locationX"] = Decimal("Infinity")
        self.prop["locationY"] = Decimal("Infinity")


    @property
    def size(self) -> float:
        """
        Getter for the elements size
        Returns:
            float: the size
        """
        return self._size

    @size.setter
    def size(self, size) -> None:
        """
        Setter for the size of the element
        Args:
            (float) size: the elements desired size
        Returns:
            None
        """
        self.prop["size"] = str(size)
        self._size = size

    @property
    def color(self) -> Color:
        """
        Getter for the color of the element in the bridges visualization
        Returns:
            Color: Color object representing the color of the element
        """
        return self._color

    @color.setter
    def color(self, *args) -> None:
        """
        Setter for the color of the element in the bridges visualization
        Args:
            (optional) list: requires either 3 ints 0-255 for RGB and an optional float 0.0-1.0 for alpha EX: color = [0, 255, 0, 1.0]
            (optional) str: string representing the element color. from web colors: https://developer.mozilla.org/en-US/docs/Web/CSS/color_value
        Returns:
            None
        Raises:
            ValueError: if the color name provided is not available
        """
        if len(args) == 1 and type(args[0]) == str:
            col = args[0].lower()
            alpha = self.opacity
            if col == "red":
                red = 255
                green = 0
                blue = 0
            elif col == "green":
                red = 0
                green = 255
                blue = 0
            elif col == "blue":
                red = 0
                green = 0
                blue = 255
            elif col == "yellow":
                red = 255
                green = 255
                blue = 0
            elif col == "cyan":
                red = 0
                green = 255
                blue = 255
            elif col == "magenta":
                red = 255
                green = 0
                blue = 255
            elif col == "white":
                red = 0
                green = 0
                blue = 0
            elif col == "black":
                red = 255
                green = 255
                blue = 255
            elif col == "orange":
                red = 255
                green = 155
                blue = 0
            elif col == "turqouise":
                red = 173
                green = 234
                blue = 234
            elif col == "maroon":
                red = 176
                green = 48
                blue = 96
            elif col == "aquamarine":
                red = 127
                green = 255
                blue = 212
            elif col == "azure":
                red = 240
                green = 255
                blue = 2550
            elif col == "beige":
                red = 245
                green = 245
                blue = 220
            elif col == "brown":
                red = 166
                green = 42
                blue = 42
            elif col == "tan":
                red = 210
                green = 180
                blue = 140
            elif col == "olive":
                red = 128
                green = 128
                blue = 0
            elif col == "khaki":
                red = 240
                green = 230
                blue = 140
            elif col == "bisque":
                red = 255
                green = 228
                blue = 196
            elif col == "coral":
                red = 255
                green = 127
                blue = 0
            elif col == "pink":
                red = 255
                green = 192
                blue = 203
            elif col == "lavender":
                red = 230
                green = 230
                blue = 250
            elif col == "purple":
                red = 160
                green = 32
                blue = 240
            elif col == "gold":
                red = 255
                green = 215
                blue = 0
            elif col == "chartreuse":
                red = 127
                green = 255
                blue = 0
            else:
                raise ValueError("Invalid Color")
            #assign the element visualizer a color object
            self._color = Color(red, green, blue, alpha)
        elif type(args[0])== Color:
            self._color = args[0]
        elif len(args) == 3:
            red = args[0]
            green = args[1]
            blue = args[2]
            if len(args) == 4:
                alpha = args[3]
            else:
                alpha = self.opacity
            self._color = Color(red, green, blue, alpha)

    @property
    def shape(self) -> str:
        """
        Getter for the shape of the element
        Returns:
            str: reperesenting the type of shape
        """
        return self._shape

    @shape.setter
    def shape(self, a_shape):
        """
        Setter for the shape of the element
        Args:
            (str) a_shape: the name of shape for element
        """
        a_shape = a_shape.lower()
        self.prop["shape"] = a_shape
        self._shape = a_shape

    @property
    def opacity(self) -> float:
        """
        Getter for the opacity of the element
        Returns:
            float: representing the opacity
        """
        return self.color.alpha

    @opacity.setter
    def opacity(self, opacity) -> None:
        """
        Setter for the opacity of the element
        Args:
            (float) opacity: the opacity to be applied
        Returns:
            None
        """
        self.prop["opacity"] = Decimal(opacity)
        self.color.alpha = opacity
        self._opacity = opacity

    def set_location(self, x, y):
        """
        Setter for the location of the element
        Args:
            (int) x: x location
            (int) y: y location
        Returns:
            None
        """
        self.prop['locationX'] = x
        self.prop['locationy'] = y
        self._locationX = x
        self._locationY = y

    def get_locationX(self) -> int:
        """
        Getter for the X location of element
        Returns:
            int: as the x location
        """
        return self._locationX

    def get_locationY(self) -> int:
        """
        Getter for the y location of the element
        Returns:
            int: as the y position
        """
        return self._locationY
