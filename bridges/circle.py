import json
from bridges.symbol import *

class Circle(Symbol):

    def __init__(self, **kwargs) -> None:
        """
        Constructor for a circle symbol
        Args:
            locx: x location of the circle
            locy: y location of the circle
            r: radius of the circle
        Returns:
            None
        Raises:
            value error
        """
        super(Circle, self).__init__()
        if 'locx' in kwargs and 'locy' in kwargs:
            self.set_location(kwargs['locx'], kwargs['locy'])
        if 'r' in kwargs:
            if r < 0:
                raise ValueError("Radius value needs to be positive")
            self.radius = kwargs['r']
        else:
            self.radius = 10

    def _get_name(self) -> str:
        """
        Gets the name of the shape/symbol
        Returns:
            str
        """
        return "circle"

    @property
    def radius(self) -> float:
        """
        Getter function for the radius of this circle
        Returns:
            float
        """
        return self.radius

    @radius.setter
    def radius(self, r) -> None:
        """
        Setter for the radius of this circle
        Args:
            r: radius to be set
        Returns:
            None
        Raises:
            value error
        """
        if r < 0:
            raise ValueError("Illegal value for radius. Must be positive")
        self.radius = r

    def set_circle(self, locx, locy, r) -> None:
        """
        Set the location and size of the circle
        Args:
            locx: x location of the circle
            locy: y location of the circle
            r: radius of the circle
        Returns:
            None
        Raises:
            value error
        """
        self.set_location(locx, locy)
        if r < 0:
            raise ValueError("Radius value needs to be positive")
        self.radius = r

    ################################################

    def get_dimensions(self):
        dims = []
        location = self.get_location()

        dims.append(location[0] - self.radius)
        dims.append(location[0] + self.radius)
        dims.append(location[1] - self.radius)
        dims.append(location[1] + self.radius)

        return dims

    def _get_json_representation(self) -> dict:
        """
        Get the json representation of the Circle object
        Returns:
            dict
        """
        ds_json = super(Circle, self)._get_json_representation()
        ds_json["name"] = self.label
        ds_json["shape"] = self._get_name()
        ds_json["r"] = self.radius

        return ds_json