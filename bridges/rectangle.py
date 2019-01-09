import json
from bridges.symbol import *

class Rectangle(Symbol):

    def __init__(self, w = None, h = None, locx = None, locy = None):
        super(Rectangle, self).__init__()
        if w is not None and h is not None:
            if w < 0 or h < 0:
                raise ValueError("Illegal height or width! Height and Width values need to be positive")
            self.width = w
            self.height = h
        if locx is not None and locy is not None:
            self.set_location(locx, locy)

    def get_name(self):
        return "rect"

    def set_width(self, w):
        if w <= 0 or w > 300:
            raise ValueError("Width need to be in the range(0-300)")
        self.width = w

    def set_height(self, h):
        if h <= 0 or h > 300:
            raise ValueError("Height need to be in the range(0-300)")
        self.height = h

    def get_dimensions(self):

        dims = []
        location = self.get_location()

        dims.append(location[0] - self.width/2)
        dims.append(location[0] - self.width/2)
        dims.append(location[1] - self.height/2)
        dims.append(location[1] - self.height/2)

        return dims

    def set_rectangle(self, locx, locy, w, h):
        self.set_location(locx, locy)
        if w <= 0 or w > 300 or h <= 0 or h > 300:
            raise ValueError("Height, Width need to be in the range(0-300)")
        self.width = w
        self.height = h

    def get_json_representation(self):

        ds_json = super(Rectangle, self).get_json_representation()
        ds_json["name"] = self.get_label()
        ds_json["shape"] = self.get_name()
        ds_json["width"] = self.width
        ds_json['height'] = self.height

        return ds_json



