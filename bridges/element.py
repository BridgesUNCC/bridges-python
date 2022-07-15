from bridges.element_visualizer import *
from bridges.link_visualizer import *
import re
from decimal import Decimal
import traceback
import sys


class Element:
    """
    @brief  This is the main superclass in BRIDGES for  deriving a number of
    elements used  in building data structures.
    
    This is the main superclass in BRIDGES for  deriving a number of
    elements used  in building data structures, viz., arrays, lists, trees and graphs.
    SLelement, DLelement, CircSLelement, CircDLelement, MLelement, TreeElement, BinTreeElement,
    BSTElement, AVLTreeElement and KDTreeElement are all subclasses
    (see class hierarchy above).  Element contains  two
    visualizer objects (ElementVisualizer, LinkVisualizer) for specifying
    visual attributes for nodes and links respectively. It also contains a label that
    that can be displayed in BRIDGES visualizations.
    
    All the tutorials under
    
    https://bridgesuncc.github.io/tutorials/Overview.html
    
    illustrate examples of using different types of Element objects and how to
    manipulate their visual attributes.
    
    @author Matthew Mcquaigue,  Kalpathi Subramanian
    
    2017, 2018, 6/24/19, 2020, 2021
    
    """
    ids = 0

    def get_data_structure_type(self) -> str:
        """
        Get the data structure representation
        Returns:
            str: representing the data structure type
        """
        return "Element"

    def __init__(self, **kwargs) -> None:
        """
        Element constructor. Creates an Element Visualizer and unique identifier for the current element.
        Args:
            (0) : "label" - the string label that is visible on the bridges Visualization
            (1) : "value" - data value (or object) E  used to construct Element
            (2) : "original" - element object to copy (if named "original")
            (3) : "color"  - color of element
            (4) : "opacity" - opacity of element
        Returns:
            None
        """
        Element.ids += 1
        self._link_visualizer = dict()
        self._ids = Element.ids
        self._identifier = str(self._ids)
        self._visualizer = ElementVisualizer()
        self._value = kwargs.get('val')
        self._label = kwargs.get('label') if kwargs.get('label') else "Default"

        if kwargs.get("color"):
            self.color = kwargs['color']

        if kwargs.get("opacity"):
            self.opacity = kwargs['opacity']

        if kwargs.get("original"):
            self._visualizer = ElementVisualizer(kwargs['original'].get_visualizer())
            self._label = str(kwargs['original'].label)
            self._value = kwargs['original']._value

    @property
    def value(self) -> object:
        """
        Getter for the value this element is holding
        Returns:
            generic object (application specific)
        """
        return self._value

    @value.setter
    def value(self, val) -> None:
        """
        Setter for the value of an element
        Args:
            val: the value (generic, application specific object)  this element will hold
        Returns:
            None
        """

        self._value = val

    @property
    def identifier(self) -> str:
        """
        Getter for the element identifier
        Return:
            str: element identifier (for internal use)
        """
        return self._identifier

    @identifier.setter
    def identifier(self, id: int) -> None:
        """
        Setter for the element identifier
        Args:
            id: the identifier (for internal use)
        Returns:
            None
        """
        self._identifier = id

    @property
    def visualizer(self) -> ElementVisualizer:
        """
        Getter for the element visualizer

        Returns:
            ElementVisualizer 
        """
        return self._visualizer

    @visualizer.setter
    def visualizer(self, vis: ElementVisualizer) -> None:
        """
        Setter function for this element visualizer

        Args:
            vis: the element visualizer

        Returns:
            None
        """
        self._visualizer = vis

    def get_link_visualizer(self, el) -> LinkVisualizer:
        """
        Getter for  the link visualizer object that links this element to 
        another element specified by the argument.
        Args:
            el: the element terminating the link
        Returns:
            LinkVisualizer: of this element
        Raises:
            ValueError: if an element is not passed in
        """
        if el in self._link_visualizer:
            return self._link_visualizer[el]
        else:
            self._link_visualizer[el] = LinkVisualizer()
            return self._link_visualizer[el]

    def set_link_visualizer(self, el) -> None:
        """
        Setter for the link visualizer of this element
        Args:
            (Element) el: the terminating element of this link;
             creates a new link visualizer for this link
        Returns:
            None
        """
        self._link_visualizer[el] = LinkVisualizer()

    def remove_link_visualizer(self, el) -> None:
        """
        Deleter function for the lik visualizer of this element
        Args:
            (Element) el: the terminating element of the link; the link visualizer 
            for this link will be deleted
        Returns:
            None
        """
        self._link_visualizer.pop(el)

    @property
    def label(self):
        """
        Getter for the element's label
        Returns:
           str: the element's label 
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Setter for the element's label
        Args:
           label: the element's label 
        Returns:
           None
        """
        self._label = label

    @property
    def size(self):
        """
        Getter for the element's size
        Returns:
           float: element size (0-50)
        """
        return self.visualizer.size

    @size.setter
    def size(self, sz):
        """
        Setter for the element's size
        Args:
           sz: the element's size (0.-50.)
        Returns:
           None
        """
        self.visualizer.size = sz

    @property
    def color(self):
        """
        Getter for the element's color
        Returns:
           Color: element's color
        """
        return self.visualizer.color

    @color.setter
    def color(self, col):
        """
        Setter for the element's size
        Args:
           col: the element's color
        Returns:
           None
        """
        self.visualizer.color = col

    @property
    def opacity(self):
        """
        Getter for the element's opacity
        Returns:
           float: element size (0-1.0)
        """
        return self.visualizer.opacity

    @opacity.setter
    def opacity(self, op):
        """
        Setter for the element's opacity
        Args:
           op: the element's size (0-1.0)
        Returns:
           None
        """
        self.visualizer.opacity = op

    @property
    def shape(self):
        """
        Getter for the element's shape type
        Returns:
           element shape
        """
        return self.visualizer.shape

    @shape.setter
    def shape(self, shp):
        """
        Setter for the element's shape
        Args:
           shp: the element's size (0-1.0)
        Returns:
           None
        """
        self.visualizer.shape = shp

    @property
    def id(self) -> int:
        """
        Get numer of ids of element object
        Returns:
           (int) number of ids of element
        """
        return self._ids

    def set_location(self, locX, locY):
        """
        Setter for the element's location
        Args:
           locX: the element's location in X
           locY: the element's location in Y
        Returns:
           None
        """
        self.visualizer.set_location(locX, locY)

    def get_locationX(self):
        """
        Getter for the element's location in X
        Returns:
           float: X coordinate of element's location
        """
        return self.visualizer.location_x

    def get_locationY(self):
        """
        Getter for the element's location in Y
        Returns:
           float: Y coordinate of element's location
        """
        return self.visualizer.location_y

    def get_element_representation(self):
        """
        Getter for the element's JSON representation (for internal use)
        Returns:
           str: JSON of element
        """
        json = {
            "name": str(self.label),
            "shape": str(self.visualizer.shape),
            "size": self.visualizer.size,
            "color": [str(self.visualizer.color.red), str(self.visualizer.color.green),
                      str(self.visualizer.color.blue), str(self.visualizer.color.alpha)]
        }
        loc_flag = not ((self.visualizer.location_x == Decimal('Infinity')) or (self.visualizer.location_y == Decimal('Infinity')))
        if loc_flag:
            json['location'] = [self.visualizer.location_x, self.visualizer.location_y]
        return json

    def get_link_representation(self, lv, src, dest):
        """
        Getter for the JSON representation of  the element's link  (for internal use)
        Args:
           lv : link visualizer
           src: source vertex of link
           dest: destination vertex of link
        Returns:
           str: JSON of element's link from src to dest
        """
        link_json = lv.get_link_properties()
        link_json["source"] = src
        link_json["target"] = dest
        return link_json
