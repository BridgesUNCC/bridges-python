#!/usr/bin/env python
## package: bridges.base
from bridges.color import *

# from Element import Element

##
#  @brief This class maintains the visual attributes of links that join
#  bridges elements.
#
#  Visual properties include color, thickness, and opacity.
#  Objects of this class are stored as part of the Element class.
#  Generally, a user will manipulate the LinkVisualizer returned from the
#  Element's getLinkVisualizer(Element it) method (which it is the bridges element
#	this element is linked to), and then set attributes using its methods. Links are
#  utilized in all types of linked lists, tree and graph structures.
#
#  Supported attribute values are as follows:<p>
#
#  <b>Supported Colors (by name)</b>: <p>
#  "red", "green", "blue","yellow","cyan","magenta",
#  "white",, "black", "orange",  "turquoise",  "maroon",  <br>
#  "aquamarine",  "azure",  "beige", "brown",  "tan",  "olive",
#  "chartreuse", "khaki", "bisque",  "coral", <br>
#  "pink",  "lavender",  "purple",  "gold" <p>
#
#  <b> Color by RGBA Specification :</b>  Range: 0-255 for each component <p>
#
#  <b> Thickness: </b> Range : 0.0-50.0
#
#  <b> Opacity: </b> Range (0.0-1.0) </p>
#
#  @author Mihai Mehedint, Kalpathi Subramanian, Matthew McQuaigue
#
#
#  \sa Example Tutorial at <br>
#  http://bridgesuncc.github.io/Hello_World_Tutorials/SLL.html
#
#
class LinkVisualizer():

    def __init__(self) -> None:
        """
        Constructor for the link visualizer'
        Retruns:
            None
        """
        self._color = Color(70, 130, 180, 1.0)
        self._thickness = 1.0
        self._weight = 1.0

    @property
    def thickness(self) -> float:
        """
        Getter for the thickness of links visualization
        Returns:
            float: the thickness
        """
        return self._thickness

    @thickness.setter
    def thickness(self, th):
        """
        Setter for the thickness of links in visualization
        Args:
            (float) th: the thickness to be applied to visualization
        Returns:
            None
        """
        self._thickness = th

    @property
    def weight(self) -> float:
        """
        Getter for the weight on the link
        Returns:
            float: weight
        """
        return self._weight

    @weight.setter
    def weight(self, wt: float) -> None:
        """
        Setter for the weight of the link
        Args:
            (float) wt: weight to be applied
        Returns:
            None
        """
        self.weight = wt

    @property
    def color(self) -> Color:
        """
        Getter for the color of the link in the visualization
        Returns:
            Color
        """
        return self._color

    @color.setter
    def color(self, *args, **kwargs):
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
    def opacity(self):
        return self.color.alpha

    @opacity.setter
    def opacity(self, opacity):
        self.color.alpha = opacity

    def get_link_properties(self):
        link_props = {
            "color": [str(self.color.red), str(self.color.green), str(self.color.blue), str(self.color.alpha)],
            "thickness": str(self.thickness),
            "weight": str(self.weight)
        }
        return link_props

    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label

