import json
from bridges.symbol import *
from typing import Tuple

class Rectangle(Symbol):
    """@brief This class defines a rectangle and is part of the symbol collection.
    
    A rectangle is defined by the location of teh lower left corner
    (smaller values of x and y) and by height and width
    
    @author Matthew Mcquaigue
    @date 2018, 7/23/19
    
    \sa Shape collection tutorial, https://bridgesuncc.github.io/tutorials/Symbol_Collection.html

    """

    def __init__(self, **kwargs) -> None:
        """
        Constructor for the rectangle symbol
        Kwargs:
            (float) w: width of the rectangle
            (float) h: height of the rectangle
            (float) locx: x location of the lower left of the rectangle
            (float) locy: y loaction of the lower left of the rectangle
        Returns:
            None
        Raises:
            ValueError: if the width or height is less than 0
        """
        super(Rectangle, self).__init__()
        self._width = 1.0
        self._height = 1.0
        if 'w' in kwargs and 'h' in kwargs:
            if kwargs['w'] < 0 or kwargs['h'] < 0:
                raise ValueError("Illegal height or width! Height and Width values need to be positive")
            self._width = kwargs['w']
            self._height = kwargs['h']
        if 'locx' in kwargs and 'locy' in kwargs:
            self._locx = kwargs['locx']
            self._locy = kwargs['locy']
        else:
            self._locx = 0.0
            self._locy = 0.0


    def get_shape_type(self) -> str:
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
            ValueError: if the width is < 0
        """
        if w <= 0:
            raise ValueError("Width needs to be positive")
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
            ValueError: if the height is < 0
        """
        if h <= 0:
            raise ValueError("Height needs to be positive")
        self._height = h

    def set_rectangle(self, locx, locy, w, h):
        """
        Setter function for setting the rectangles size and location from scratch
        Args:
            (float) locx: the x location of the lower left of the rectangle
            (float) locy: the y location of the lower left of the rectangle
            (float) w: the width of rectangle
            (float) h: the height of rectangle
        Returns:
            None
        Raises:
            ValueError: if the height or width is < 0
        """
        self._locx = locx
        self._locy = locy
        self.width = w
        self.height = h

    @property
    def lower_left(self) -> Tuple[float, float]:
        return (self._locx, self._locy)

    @lower_left.setter
    def lower_left(self, ll: Tuple[float, float]):
        self._locx=ll[0]
        self._locy=ll[1]
        
    def get_json_representation(self) -> dict:
        """
        Getter function for the json representation of the data structure/shape
        Returns:
            dict: representing the json 
        """
        ds_json = super(Rectangle, self).get_json_representation()

        loc = [self._locx, self._locy]
        ds_json['lowerleftcorner'] = loc
        ds_json["width"] = self.width
        ds_json['height'] = self.height

        return ds_json



