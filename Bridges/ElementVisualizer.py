#!/usr/bin/env python
from decimal import Decimal
from Bridges.Element import *
from Bridges.Color import *

##
# This class is used to store the visualization elements on the for the Bridges
# Visualiztion, including the color, shape, opacity, and size of the node.
# <p>
# Objects of this class are stored as properties of all Element subclasses.
# Generally, you will manipulating the ElementVisualizer returned from the
# Element getVisualizer() method, and then call the setVisualizer() method on
# the Element after changes have been made.
#
class ElementVisualizer():
    #  Visualization properties for this Node.

    shape = "circle"
    key = ""
    locationX = float("inf")
    locationY = float("inf")
    size = 10.0
    opacity = 1.0


    prop = dict()
    color = Color(None, 70, 130, 180, 1.0)

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
    def __init__(self, a_color = "green", a_shape = "circle", size = 10.0, opacity = 1.0):
        if a_color is not "green":
            self.set_color(a_color)
        if a_shape is not "circle":
            self.set_shape(a_shape)
        if size is not 10.0:
            self.set_size(10.0)
        if opacity is not 1.0:
            self.set_opacity(opacity)
        else:
            self.color = Color(None, 70, 130, 180, 1.0)


    ##
    # Set the size of the Element in the Bridge Visualization in pixels
    #
    # @param size
    #            the pixel size of the Element in the Bridges Visualization
    #
    def set_size(self, size):
        self.prop["size"] = str(size)
        self.size = size

    ##
    # Get the size of the Element in the Bridges Visualiation
    #
    # @return the size in pixels of the Element in the Bridges Visualization
    #
    def get_size(self):
        return self.size

    ##
    #  Set the color of the Element in the Bridges Visualization to "aColor".
    #  @param aColor the string reprsenting the color of the Element in the Bridges Visualization
    #
    def set_color(self, col_name):

        #  this.aColor = aColor;
        a_color = col_name.lower()

        red = int()
        green = int()
        blue = int()
        alpha = float()

        if col_name is not None:
            if col_name == "red":
                self.red = 255
                self.green = 0
                self.blue = 0
                self.alpha = 1.0

            elif col_name == "green":
                self.red = 0
                self.green = 255
                self.blue = 0
                self.alpha = 1.0

            elif col_name == "blue":
                self.red = 0
                self.green = 0
                self.blue = 255
                self.alpha = 1.0

            elif col_name == "yellow":
                self.red = 255
                self.green = 255
                self.blue = 0
                self.alpha = 1.0

            elif col_name == "cyan":
                self.red = 0
                self.green = 255
                self.blue = 255
                self.alpha = 1.0

            elif col_name == "magenta":
                self.red = 255
                self.green = 0
                self.blue = 255
                self.alpha = 1.0

            elif col_name == "white":
                self.red = 255
                self.green = 255
                self.blue = 255
                self.alpha = 1.0

            elif col_name == "black":
                self.red = 0
                self.green = 0
                self.blue = 0
                self.alpha = 1.0

            elif col_name == "orange":
                self.red = 255
                self.green = 155
                self.blue = 0
                self.alpha = 1.0

            elif col_name == "turquoise":
                self.red = 173
                self.green = 234
                self.blue = 234
                self.alpha = 1.0

            elif col_name == "maroon":
                self.red = 176
                self.green = 48
                self.blue = 96
                self.alpha = 1.0

            elif col_name == "aquamarine":
                self.red = 127
                self.green = 255
                self.blue = 212
                self.alpha = 1.0

            elif col_name == "azure":
                self.red = 240
                self.green = 255
                self.blue = 255
                self.alpha = 1.0

            elif col_name == "beige":
                self.red = 245
                self.green = 245
                self.blue = 220
                self.alpha = 1.0

            elif col_name == "brown":
                self.red = 166
                self.green = 42
                self.blue = 42
                self.alpha = 1.0

            elif col_name == "tan":
                self.red = 210
                self.green = 180
                self.blue = 140
                self.alpha = 1.0

            elif col_name == "olive":
                self.red = 128
                self.green = 128
                self.blue = 0
                self.alpha = 1.0

            elif col_name == "chartreuse":
                self.red = 127
                self.green = 255
                self.blue = 0
                self.alpha = 1.0

            elif col_name == "khaki":
                self.red = 240
                self.green = 230
                self.blue = 140
                self.alpha = 1.0

            elif col_name == "bisque":
                self.red = 255
                self.green = 228
                self.blue = 196
                self.alpha = 1.0

            elif col_name == "coral":
                self.red = 255
                self.green = 127
                self.blue = 0
                self.alpha = 1.0

            elif col_name == "pink":
                self.red = 255
                self.green = 192
                self.blue = 203
                self.alpha = 1.0

            elif col_name == "lavender":
                self.red = 230
                self.green = 230
                self.blue = 250
                self.alpha = 1.0

            elif col_name == "purple":
                self.red = 160
                self.green = 32
                self.blue = 240
                self.alpha = 1.0

            elif col_name == "gold":
                self.red = 255
                self.green = 215
                self.blue = 0
                self.alpha = 1.0

        self.prop["color"] = a_color

        self.color = Color(None, self.red, self.green, self.blue, self.alpha)
    ##
    # Get the color of the Element in the Bridges Visualization
    #  @return the string reprsenting the color of the Element in the Bridges Visualization
    #
    def get_color(self):
        return self.color

    ##
    # Get the shape of the Element in the Bridges Visualization.
    # @return the string that represents the Element's shape in the Bridges Visualization.
    #
    def get_shape(self):
        return self.shape

    ##
    # Sets the shape of the Element in the Bridges Visualization
    #
    # @param aShape the string representing the shape of the Element in the Bridges Visualization
    #
    def set_shape(self, a_shape):
        #  this.aShape = aShape;
        a_shape = a_shape.lower()
        #Validation.validateShape(a_shape)
        self.prop["shape"] = a_shape
        self.shape = a_shape

    ##
    # Sets the opacity of the Element in the Bridges Visualization
    #
    # @param opacity a double between 0 and 1 representing how transparent the node
    #            should be on the Bridges Visualization. 0 for invisible, 1 for
    #            fully visible, a decimal between 0 and 1 for varying
    #            transparency.
    #
    def set_opacity(self, opacity):
        #Validation.validateOpacity(opacity)
        self.prop["opacity"] = Decimal(opacity)
        self.color.set_alpha(opacity)
        self.opacity = opacity

    ##
    #  Get the opacity of the Element in the Bridges Visualization
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
