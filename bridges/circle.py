import json
from bridges.symbol import *

class Circle(Symbol):

    def __init__(self, locx = None, locy = None, r = None):
        super(Circle, self).__init__()
        if r is not None:
            if r < 0:
                raise ValueError("Radius value needs to be positive")
            self.radius = r
        else:
            self.radius = 10

        if locx is not None and locy is not None:
            self.set_location(locx, locy)

    def get_name(self):
        return "circle"

    def set_radius(self,r):
        if r < 0:
            raise ValueError("Illegal value for radius. Must be positive")
        self.radius = r

    def set_circle(self, locx, locy, r):
        self.set_location(locx, locy)
        if r < 0:
            raise ValueError("Radius value needs to be positive")
        self.radius = r

    def get_dimensions(self):
        dims = []
        location = self.get_location()

        dims.append(location[0] - self.radius)
        dims.append(location[0] + self.radius)
        dims.append(location[1] - self.radius)
        dims.append(location[1] + self.radius)

        return dims

    def get_json_representation(self):

        ds_json = super(Circle, self).get_json_representation()
        ds_json["name"] = self.get_label()
        ds_json["shape"] = self.get_name()
        ds_json["r"] = self.radius

        return ds_json