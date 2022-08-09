import json
from bridges.symbol import *
from typing import Tuple


class Circle(Symbol):
    """
    @brief This class defines a circle and is part of the symbol collection.
    A circle  has a radius and a center, which is also its location
    
    @author Matthew Mcquaigue
    @date 2018, 7/23/19
    
    Shape collection tutorial, https://bridgesuncc.github.io/tutorials/Symbol_Collection.html
    """

    def __init__(self, **kwargs) -> None:
        """
        Constructor for a circle symbol
        Args:
            (int) locx: x location of the circle
            (int) locy: y location of the circle
            (float) r: radius of the circle
        Returns:
            None
        Raises:
            ValueError: if the radius is not a positive number
        """
        super(Circle, self).__init__()
        if 'locx' in kwargs and 'locy' in kwargs:
            self._locx = kwargs['locx']
            self._locy = kwargs['locy']
        else:
            self._locx = 0.0
            self._locy = 0.0
        if 'r' in kwargs:
            if kwargs['r'] < 0:
                raise ValueError("Radius value needs to be positive")
            self.radius = kwargs['r']
        else:
            self.radius = 10

    def get_shape_type(self) -> str:
        """
        Gets the name of the shape/symbol
        Returns:
            str: representing the name
        """
        return "circle"

    @property
    def radius(self) -> float:
        """
        Getter function for the radius of this circle
        Returns:
            float: representing radius
        """
        return self._radius

    @radius.setter
    def radius(self, r) -> None:
        """
        Setter for the radius of this circle
        Args:
            (float) r: radius to be set
        Returns:
            None
        Raises:
            ValueError: if the radius is not a positive number
        """
        if r < 0:
            raise ValueError("Illegal value for radius. Must be positive")
        self._radius = r

    def set_circle(self, locx, locy, r) -> None:
        """
        Set the location and size of the circle
        Args:
            (float) locx: x coordinate of the center of the circle
            (float) locy: y coordinate of the center of the circle
            (float) r: radius of the circle
        Returns:
            None
        Raises:
            ValueError: if the radius is not a positive number
        """
        self._locx = locx
        self._locy = locy
        self.radius = r

    @property
    def center(self) -> Tuple[float, float]:
        return (self._locx, self._locy)

    @center.setter
    def center(self, l: Tuple[float, float]) -> None :
        self._locx = l[0]
        self._locy = l[1]
                
    
    def get_json_representation(self) -> dict:
        """
        Get the json representation of the Circle object
        Returns:
            dict: representing the JSON 
        """
        ds_json = super(Circle, self).get_json_representation()
        ds_json["r"] = self.radius
        ds_json['center'] = [self._locx, self._locy]

        return ds_json
