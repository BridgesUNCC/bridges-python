import json
from bridges.symbol import *

##
# @brief This class defines a circle and is part of the symbol collection.
# A circle  has a radius and a center, which is also its location
#
# @author Matthew Mcquaigue
# @date 2018, 7/23/19
#
# Shape collection tutorial, http://bridgesuncc.github.io/tutorials/Symbol_Collection.html
#
#
class Circle(Symbol):

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
            self.set_location(kwargs['locx'], kwargs['locy'])
        else:
            self.set_location(0.0, 0.0)
        if 'r' in kwargs:
            if kwargs['r'] < 0:
                raise ValueError("Radius value needs to be positive")
            self.radius = kwargs['r']
        else:
            self.radius = 10
        self.shape_type = "circle"

    def get_name(self) -> str:
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
            (int) locx: x coordinate of the center of the circle
            (int) locy: y coordinate of the center of the circle
            (float) r: radius of the circle
        Returns:
            None
        Raises:
            ValueError: if the radius is not a positive number
        """
        self.set_location(locx, locy)
        if r < 0:
            raise ValueError("Radius value needs to be positive")
        self.radius = r

    def get_dimensions(self) -> list:
        """
        Getter for the dimensions for the circle
        Returns:
            list: bounding box of the circle (xmin, xmax, ymin, ymax)
        """
        dims = []
        location = self.get_location()

        dims.append(location[0] - self.radius)
        dims.append(location[0] + self.radius)
        dims.append(location[1] - self.radius)
        dims.append(location[1] + self.radius)

        return dims

    def translate(self, tx:float, ty:float):
        """
        translate the circle
        Arrgs:
            (float) tx: x translation
            (float) ty: y translation
        """
        center = self.get_location()
        center = self.translate_point(center, tx, ty)
        self.set_location(center[0], center[1])

    def scale(self, scale:float):
        """
        Scale the circle. Only the radius needs to be scaled, using a single scale value
        Args:
            (float) scale: scale factor
        """
        # scale onlt the radius
        # center stays the same
        self.radius *= scale

    def get_json_representation(self) -> dict:
        """
        Get the json representation of the Circle object
        Returns:
            dict: representing the JSON 
        """
        ds_json = super(Circle, self).get_json_representation()
        ds_json["name"] = self.label
        ds_json["shape"] = self.shape_type
        ds_json["r"] = self.radius

        return ds_json
