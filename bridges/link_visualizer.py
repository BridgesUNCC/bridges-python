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
#  @author Mihai Mehedint, Kalpathi Subramanian
#
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
    # color = Color.Color(None, 70, 130, 180, 1.0)

    #  link thickness
    thickness = float()

    #  link weight
    weight = float()

    def __init__(self):
        # super(LinkVisualizer.LinkVisualizer, self).__init__()
        self.color = Color(70, 130, 180, 1.0)
        self.set_color(70, 130, 180, 1.0)
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
    # Get the thickness of the link in the bridges Visualiation
    #
    # @return the size in pixels of the Element in the bridges Visualization
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
    #	Set the color of the link in the bridges Visualization to "aColor".
    #
    # 	@param col_name the string reprsenting the color of the Element in
    #		the bridges Visualization; supported named colors are
    #  	"red", "green", "blue", "yellow", "cyan", "magenta", "white", "black",
    #  	"orange", "turquoise", "maroon", "aquamarine", "azure", "beige",
    #  	"brown", "tan", "olive", "chartreuse", "khaki", "bisque", "coral",
    #  	"pink", "lavender", "purple", "gold"
    #
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
    #
    #	Get the color of the link in the bridges Visualization
    #
    #	@return the Color object representing the color of the link
    #
    #
    def get_color(self):
        return self.color

    ##
    # Sets the opacity of the link in the bridges Visualization
    #
    # @param opacity a float between 0 and 1 representing how transparent
    #	the node
    #            should be on the bridges Visualization. 0 for invisible, 1 for
    #            fully visible, a decimal between 0 and 1 for varying
    #            transparency.
    #
    def set_opacity(self, opacity):
        self.color.set_alpha(opacity)

    ##
    #
    # 	Get the opacity of the link in the bridges Visualization
    #
    # 	@return the opacity value (in the range 0.0-1.0
    #
    #
    def get_opacity(self):
        return self.color.get_alpha()

    def get_link_properties(self):
        link_props = self.QUOTE + "color" + self.QUOTE + self.COLON + self.OPEN_BOX + str(self.get_color().get_red()) + self.COMMA + str(self.get_color().get_green()) + self.COMMA + str(self.get_color().get_blue()) + self.COMMA + str(self.get_color().get_alpha()) + self.CLOSE_BOX + self.COMMA + self.QUOTE + "thickness" + self.QUOTE + self.COLON + str(self.get_thickness()) + self.COMMA + self.QUOTE + "weight" + self.QUOTE + self.COLON + str(self.get_weight())
        return link_props

    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label

