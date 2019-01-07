import json
from bridges.symbol import *

class Label(Symbol):

    def __init__(self, label = None):
        super(Label, self).__init__()
        if label is not None:
            self.set_label(label)
        self.width = 100
        self.height = 50
        self.font_size = 12

    def set_font_size(self, size):
        if size <= 0 or size > 200:
            raise ValueError("Please use font size between 0 and 200")
        else:
            self.font_size = size

    def get_dimensions(self):
        length = 0.09 * self.font_size * len(self.get_label())
        x = self.get_location()[0]
        y = self.get_location()[1]

        return [x - length/2, x + length/2, y, y]

    def get_json_representation(self):
        ds_json = super(Label,self).get_json_representation()
        ds_json["name"] = super(Label,self).get_label()
        ds_json["shape"] = "text"
        ds_json["font-size"] = self.font_size

        return ds_json
