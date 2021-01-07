import json
from bridges.symbol import *

class Rectangle(Symbol):
    """
    @brief This class defines a rectangle and is part of the symbol collection.
    
    A rectangle has height and width
    
    @author Matthew Mcquaigue
    @date 2018, 7/23/19
    
    \sa Shape collection tutorial, http://bridgesuncc.github.io/tutorials/Symbol_Collection.html
    """

    def __init__(self, **kwargs) -> None:
        """
        Constructor for the rectangle symbol
        Kwargs:
            (float) w: width of the rectangle
            (float) h: height of the rectangle
            (float) locx: x location of rectangle
            (float) locy: y loaction of rectangle
        Returns:
            None
        Raises:
            ValueError: if the width or height is less than 0
        """
        super(Rectangle, self).__init__()
        if 'w' in kwargs and 'h' in kwargs:
            if kwargs['w'] < 0 or kwargs['h'] < 0:
                raise ValueError("Illegal height or width! Height and Width values need to be positive")
            self._width = kwargs['w']
            self._height = kwargs['h']
        if 'locx' in kwargs and 'locy' in kwargs:
            self.set_location(kwargs['locx'], kwargs['locy'])
        else:
            self.set_location(0.0, 0.0)
        self.shape_type = 'rect'

    def get_name(self) -> str:
        """
        Getter for the name of the shape
        Returns:
             str: shape name
        """
        return "rect"

    @property
    def width(self) -> float:
        """
        Getter for the rectangle width
        Returns:
            float: the width
        """
        return self._width

    @width.setter
    def width(self, w) -> None:
        """
        Setter for the width of the rectangles
        Args:
            (float) w: the width to be applied to rectangle
        Returns:
            None
        Raises:
            ValueError: if the width is < 0 or > 300
        """
        if w <= 0:
            raise ValueError("Width needs to be in the range(0-300)")
        self._width = w

    @property
    def height(self) -> float:
        """
        Getter for the height of the rectangle
        Returns:
            float: the height of the rectangle
        """
        return self._height

    @height.setter
    def height(self, h) -> None:
        """
        Setter for the height of the rectangle
        Args:
            (float) h: the height to be applied
        Returns:
            None
        Raises:
            ValueError: if the height is < 0 or > 300
        """
        if h <= 0:
            raise ValueError("Height needs to be in the range(0-300)")
        self._height = h

    def get_dimensions(self) -> list:
        """
        Getter for the dimensions of the rectangle
        Returns:
            list: the bounding box of the shape (xmin, xmax, ymin, ymax)
        """
        dims = []
        location = self.get_location()

        dims.append(location[0])
        dims.append(location[0] + self.width)
        dims.append(location[1])
        dims.append(location[1] + self.height)

        return dims

    def set_rectangle(self, locx, locy, w, h):
        """
        Setter function for setting the rectangles size and location from scratch
        Args:
            (float) locx: the x location of rectangle
            (float) locy: the y location of rectangle
            (float) w: the width of rectangle
            (float) h: the height of rectangle
        Returns:
            None
        Raises:
            ValueError: if the height or width is < 0 or > 300
        """
        self.set_location(locx, locy)
        if w <= 0 or h <= 0:
            raise ValueError("Height, Width need to be in the range(0-300)")
        self.width = w
        self.height = h

    def translate(self, tx, ty):
        """
        Translate the rectangle by tx, ty along X and Y respectively
        Args:
           tx: translation factor in X
           ty: translation factor in Y
        """

        center = self.get_location()
        center = self.translate_point(center, tx, ty)
        self.set_location(center[0], center[1])

    def scale(self, sx, sy):
        """
        Scale the rectangle by sx, sy along X and Y respectively
        Args:
           sx: translation factor in X
           sy: translation factor in Y
        """
        pt = [0., 0.]
        pt[0] = self.width
        pt[1] = self.height
        new_pt = self.scale_point(pt, sx, sy)
        self.width = new_pt[0]
        self.height = new_pt[1]

    def get_json_representation(self) -> dict:
        """
        Getter function for the json representation of the data structure/shape
        Returns:
            dict: representing the json 
        """
        ds_json = super(Rectangle, self).get_json_representation()
        ds_json["name"] = super(Rectangle, self).label
        ds_json["shape"] = self.shape_type
        ds_json["width"] = self.width
        ds_json['height'] = self.height

        return ds_json



