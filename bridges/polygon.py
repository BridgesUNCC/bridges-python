from bridges.polyline import *


class Polygon(Polyline):

    def __init__(self, pts = None):
        if pts is not None:
            super(Polygon, self).__init__(pts = pts)
        else:
            super(Polygon, self).__init__()
        self.shape_type = "polygon"

    def get_name(self):
        return "polygon"
