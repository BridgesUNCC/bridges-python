#!/usr/bin/env python
## package: bridges.base
import Color
# from Element import Element

##
#  @brief This class maintains the visual attributes of links that join
#  Bridges elements.
#
#  Visual properties include color, thickness, and opacity.
#  Objects of this class are stored as part of the Element class.
#  Generally, a user will manipulate the LinkVisualizer returned from the
#  Element's getLinkVisualizer(Element it) method (which it is the Bridges element
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
#  @author Mihai Mehedint, Kalpathi Subramanian
#
#  @date 6/22/16, 1/16/17, 5/17/17
#
#  \sa Example Tutorial at <br>
#  http://bridgesuncc.github.io/Hello_World_Tutorials/SLL.html
#
#
class LinkVisualizer(object):
    #  Link visualization properties for this element.
    #  maintains mapping from the terminating vertex to its
    #  visual properties
    #  implemented as a hashmap mapping into properties, which
    #  is als a hashmap, to keep the accesses constant time.
    QUOTE = "\""
    COMMA = ","
    COLON = ":"
    OPEN_CURLY = "{"
    CLOSE_CURLY = "}"
    OPEN_PAREN = "("
    CLOSE_PAREN = ")"
    OPEN_BOX = "["
    CLOSE_BOX = "]"

    #  link color
    color = Color.Color(None, 70, 130, 180, 1.0)

    #  link thickness
    thickness = float()

    #  link weight
    weight = float()

    def __init__(self):
        # super(LinkVisualizer.LinkVisualizer, self).__init__()
        self.set_color (None, 70, 130, 180, 1.0)
        self.set_thickness(1.0)
        self.set_weight(1.0)

    ##
    # Set the thickness of the link in the Bridge Visualization in pixels; thickness
    # shoudl be in the range 0-50.0
    #
    # @param thickness
    #
    #
    def set_thickness(self, th):
        # Validation.validateThickness(th)
        self.thickness = th

    ##
    # Get the thickness of the link in the Bridges Visualiation
    #
    # @return the size in pixels of the Element in the Bridges Visualization
    #
    def get_thickness(self):
        return self.thickness

    ##
    # Set the weight of the link, useful in graph algorithms, for example.
    # weight value is user defined, and determined by the input graph specification.
    #
    # @param weight
    #
    #
    def set_weight(self, wt):
        #  is user defined so no checking
        self.weight = wt

    ##
    # Get the weight of the link
    #
    # @return the stored edge weight
    #
    def get_weight(self):
        return self.weight

    ##
    #
    #	Set the color of the link in the Bridges Visualization to "aColor".
    #
    # 	@param col_name the string reprsenting the color of the Element in
    #		the Bridges Visualization; supported named colors are
    #  	"red", "green", "blue", "yellow", "cyan", "magenta", "white", "black",
    #  	"orange", "turquoise", "maroon", "aquamarine", "azure", "beige",
    #  	"brown", "tan", "olive", "chartreuse", "khaki", "bisque", "coral",
    #  	"pink", "lavender", "purple", "gold"
    #
    #
    def set_color(self, col_name = None, r=None, g=None, b=None, a=None):
        if col_name is not None:
            col = col_name.lower()
            #  validates and returns a 4 component RGBA val
            red = int()
            green = int()
            blue = int()
            alpha = 1.0
            if col_name == "red":
                red = 255
                green = 0
                blue = 0
            elif col_name == "green":
                red = 0
                green = 255
                blue = 0
            elif col_name == "blue":
                red = 0
                green = 0
                blue = 255
            elif col_name == "yellow":
                red = 255
                green = 255
                blue = 0
            elif col_name == "cyan":
                red = 0
                green = 255
                blue = 255
            elif col_name == "magenta":
                red = 255
                green = 0
                blue = 255
            elif col_name == "white":
                red = 255
                green = 255
                blue = 255
            elif col_name == "black":
                red = 0
                green = 0
                blue = 0
            elif col_name == "orange":
                red = 255
                green = 155
                blue = 0
            elif col_name == "turquoise":
                red = 173
                green = 234
                blue = 234
            elif col_name == "maroon":
                red = 176
                green = 48
                blue = 96
            elif col_name == "aquamarine":
                red = 127
                green = 255
                blue = 212
            elif col_name == "azure":
                red = 240
                green = 255
                blue = 255
            elif col_name == "beige":
                red = 245
                green = 245
                blue = 220
            elif col_name == "brown":
                red = 166
                green = 42
                blue = 42
            elif col_name == "tan":
                red = 210
                green = 180
                blue = 140
            elif col_name == "olive":
                red = 128
                green = 128
                blue = 0
            elif col_name == "chartreuse":
                red = 127
                green = 255
                blue = 0
            elif col_name == "khaki":
                red = 240
                green = 230
                blue = 140
            elif col_name == "bisque":
                red = 255
                green = 228
                blue = 196
            elif col_name == "coral":
                red = 255
                green = 127
                blue = 0
            elif col_name == "pink":
                red = 255
                green = 192
                blue = 203
            elif col_name == "lavender":
                red = 230
                green = 230
                blue = 250
            elif col_name == "purple":
                red = 160
                green = 32
                blue = 240
            elif col_name == "gold":
                red = 255
                green = 215
                blue = 0
            else:
                raise ValueError("Invalid color " + "'" + col_name + "'" + "." + " Only named primaries supported now. \n")
            self.color.set_red(red)
            self.color.set_blue(blue)
            self.color.set_green(green)
        else:
            self.color.set_red(r)
            self.color.set_blue(b)
            self.color.set_green(g)
            self.color.set_alpha(a)

    ##
    #
    #	Get the color of the link in the Bridges Visualization
    #
    #	@return the Color object representing the color of the link
    #
    #
    def get_color(self):
        return self.color

    ##
    # Sets the opacity of the link in the Bridges Visualization
    #
    # @param opacity a float between 0 and 1 representing how transparent
    #	the node
    #            should be on the Bridges Visualization. 0 for invisible, 1 for
    #            fully visible, a decimal between 0 and 1 for varying
    #            transparency.
    #
    def set_opacity(self, opacity):
        self.color.set_alpha(opacity)

    ##
    #
    # 	Get the opacity of the link in the Bridges Visualization
    #
    # 	@return the opacity value (in the range 0.0-1.0
    #
    #
    def get_opacity(self):
        return self.color.get_alpha()

    def get_link_properties(self):
        link_props = self.QUOTE + "color" + self.QUOTE + self.COLON + self.OPEN_BOX + str(self.get_color().get_red()) + self.COMMA + str(self.get_color().get_green()) + self.COMMA + str(self.get_color().get_blue()) + self.COMMA + str(self.get_color().get_alpha()) + self.CLOSE_BOX + self.COMMA + self.QUOTE + "thickness" + self.QUOTE + self.COLON + str(self.get_thickness()) + self.COMMA + self.QUOTE + "weight" + self.QUOTE + self.COLON + str(self.get_weight())
        return link_props
