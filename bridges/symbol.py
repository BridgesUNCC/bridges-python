import json
from bridges.color import *

class Symbol:

    ids = 0

    def __init__(self):
        self.identifier = str(Symbol.ids)
        self.label = ""
        self.fill_color = Color("blue")
        self.stroke_color = Color("white")
        self.opacity = 1.0
        self.stroke_width = 1.0
        self.stroke_dash = 1
        self.location_y = 0.0
        self.location_x = 0.0
        Symbol.ids += 1

    def get_data_structure_type(self):
        return "Symbol"

    def set_label(self, label):
        self.label = label

    def get_label(self):
        return self.label

    def get_identifier(self):
        return self.identifier

    def set_fill_color(self, c):
        self.fill_color = c

    def get_fill_color(self):
        return self.fill_color

    def set_stroke_color(self,c):
        self.stroke_color = c

    def get_stroke_color(self):
        return self.stroke_color

    def set_stroke_width(self, stroke_width):
        if stroke_width <= 0.0 or stroke_width > 10.0:
            raise ValueError("Stroke width must be between 0 and 10")
        else:
            self.stroke_width = stroke_width

    def get_stroke_width(self):
        return self.stroke_width

    def set_opacity(self, o):
        if o <= 0.0 or o > 1.0:
            raise ValueError("Opacity must be between 0.0 and 1.0")
        else:
            self.opacity = 0

    def get_opacity(self):
        return self.opacity

    def set_stroke_dash(self, dash):
        if dash < 0 or dash > 10:
            raise ValueError("Dash must be between 0 and 10 (inclusive)")
        else:
            self.stroke_dash = dash

    def get_stroke_dash(self):
        return self.stroke_dash

    def set_location(self, x, y):
        float(x)
        float(y)
        if x > float('-inf') and x < float('inf') and y > float('-inf') and y < float('inf'):
            self.location_x = x
            self.location_y = y
        else:
            raise ValueError("Coordinates must be real numbers")
    def get_location(self):
        return [self.location_x, self.location_y]

    def get_dimensions(self):
        return [0.0, 0.0, 0.0, 0.0]

    def get_json_representation(self):

        ds = {
            "fill": [self.fill_color.get_red(), self.fill_color.get_green(), self.fill_color.get_blue(), self.fill_color.get_alpha()],
            "opacity": self.opacity,
            "stroke": [self.stroke_color.get_red(), self.stroke_color.get_green(), self.stroke_color.get_blue(), self.stroke_color.get_alpha()],
            "stroke-width": self.stroke_width,
            "stroke-dasharray": self.stroke_dash,
            "location": {
                "x": self.location_x,
                "y": self.location_y
            }
        }
        return ds

