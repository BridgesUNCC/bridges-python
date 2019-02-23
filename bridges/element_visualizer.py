#!/usr/bin/env python
from decimal import Decimal
from bridges.element import *
from bridges.color import *
from decimal import Decimal


##
# This class is used to store the visualization elements on the for the bridges
# Visualiztion, including the color, shape, opacity, and size of the node.
# <p>
# Objects of this class are stored as properties of all Element subclasses.
# Generally, you will manipulating the ElementVisualizer returned from the
# Element getVisualizer() method, and then call the setVisualizer() method on
# the Element after changes have been made.
#
class ElementVisualizer(object):
    #  Visualization properties for this Node.

    shape = "circle"
    key = ""
    locationX = Decimal("Infinity")
    locationY = Decimal("Infinity")
    size = 10.0
    opacity = 1.0

    prop = dict()

    prop["color"] = "[70, 130, 180, 1.0]"
    prop["opacity"] = "1.0"
    prop["size"] = "10.0"
    prop["shape"] = "circle"
    prop["key"] = ""
    prop["locationX"] = str(locationX)
    prop["locationY"] = str(locationY)

    ##
    # Construct an ElementVisualizer with the default visualization settings.
    # The default settings are color = green, opacity = 1.0, size = 10.0, shape
    # = circle.
    #
    def __init__(self, a_color="green", a_shape ="circle", size=10.0, opacity=1.0):
        if a_color is not "green":
            self.set_color(a_color)
        else:
            self.color = Color(70, 130, 180, 1.0)
        if a_shape is not "circle":
            self.set_shape(a_shape)
        if size is not 10.0:
            self.set_size(10.0)
        if opacity is not 1.0:
            self.set_opacity(opacity)

    ##
    # Set the size of the Element in the Bridge Visualization in pixels
    #
    # @param size
    #            the pixel size of the Element in the bridges Visualization
    #
    def set_size(self, size):
        self.prop["size"] = str(size)
        self.size = size

    ##
    # Get the size of the Element in the bridges Visualiation
    #
    # @return the size in pixels of the Element in the bridges Visualization
    #
    def get_size(self):
        return self.size

    ##
    #  Set the color of the Element in the bridges Visualization to "aColor".
    #  @param aColor the string reprsenting the color of the Element in the bridges Visualization
    #
    def set_color(self, *args, **kwargs):
        """
        Usage: requires either 3 ints 0-255 for RGB and an optional float 0.0-1.0 for alpha or a str of a web color
        can also key the RGBA values with r, g, b, a or red, green, blue, alpha respectively and col_name for the str
        :param args: int, int, int optional float or str
        :param kwargs: r/red: int, b/blue: int, g/green: int optional a/alpha: float or col_name: str
        :return: None
        """
        self.color.set_color(*args, **kwargs)

    ##
    # Get the color of the Element in the bridges Visualization
    #  @return the string reprsenting the color of the Element in the bridges Visualization
    #
    def get_color(self):
        return self.color

    ##
    # Get the shape of the Element in the bridges Visualization.
    # @return the string that represents the Element's shape in the bridges Visualization.
    #
    def get_shape(self):
        return self.shape

    ##
    # Sets the shape of the Element in the bridges Visualization
    #
    # @param aShape the string representing the shape of the Element in the bridges Visualization
    #
    def set_shape(self, a_shape):
        #  this.aShape = aShape;
        a_shape = a_shape.lower()
        self.prop["shape"] = a_shape
        self.shape = a_shape

    ##
    # Sets the opacity of the Element in the bridges Visualization
    #
    # @param opacity a double between 0 and 1 representing how transparent the node
    #            should be on the bridges Visualization. 0 for invisible, 1 for
    #            fully visible, a decimal between 0 and 1 for varying
    #            transparency.
    #
    def set_opacity(self, opacity):
        self.prop["opacity"] = Decimal(opacity)
        self.color.set_alpha(opacity)
        self.opacity = opacity

    ##
    #  Get the opacity of the Element in the bridges Visualization
    # @return the opacity value
    #
    def get_opacity(self):
        return self.color.get_alpha()

    ##
    # The randomColor method selects a random color from the available list of
    # colors found in Validation.java and sets the color of the current element
    #
    # @return a color name as a string value
    #
    # def random_color(self):
    #     a = Validation.COLOR_NAMES.toArray()
    #     return self.setColor(a[Random().nextInt(a.length)].__str__())

    def set_location(self, x, y):
        self.locationX = x
        self.locationY = y

    def get_locationX(self):
        return self.locationX

    def get_locationY(self):
        return self.locationY
