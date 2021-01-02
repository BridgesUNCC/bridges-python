from bridges.polyline import *


class Polygon(Polyline):

    def __init__(self, pts = None):
        """
        Constructor. Sets the number of points in the polygon
        Args:
            pts: number of points to be used in constructing the polygon
        """
        if pts is not None:
            super(Polygon, self).__init__(pts = pts)
        else:
            super(Polygon, self).__init__()
        self.shape_type = "polygon"

    def get_name(self):
        """
        Get the name of this symbol
        """
        return "polygon"
