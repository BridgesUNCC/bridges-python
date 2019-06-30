import json
from bridges.symbol import *

class Rectangle(Symbol):

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
        if w <= 0 or w > 300:
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
        if h <= 0 or h > 300:
            raise ValueError("Height needs to be in the range(0-300)")
        self._height = h

    def get_dimensions(self) -> list:
        """
        Getter for the dimensions of the rectangle
        Returns:
            list: representing the dimensions
        """
        dims = []
        location = self.get_location()

        dims.append(location[0] - self.width/2)
        dims.append(location[0] - self.width/2)
        dims.append(location[1] - self.height/2)
        dims.append(location[1] - self.height/2)

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
        if w <= 0 or w > 300 or h <= 0 or h > 300:
            raise ValueError("Height, Width need to be in the range(0-300)")
        self.width = w
        self.height = h

    def get_json_representation(self) -> dict:
        """
        Getter function for the json representation of the data structure/shape
        Returns:
            dict: representing the json before dumped
        """
        ds_json = super(Rectangle, self).get_json_representation()
        ds_json["name"] = self.label
        ds_json["shape"] = self.get_name()
        ds_json["width"] = self.width
        ds_json['height'] = self.height

        return ds_json



