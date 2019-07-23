import json
from bridges.symbol import *

##
# @brief This class defines a polygon and is part of the symbol collection.
#
# A polygon has a set of vertices, with vertices connected by line
# segments. It differs from the polyline in the sense that the last
# and first vertex are connect to close the shape.
#
# @author David Burlinson, Kalpathi Subramanian
#
# @date 2018, 7/23/19
#
# \sa Shape collection tutorial, http://bridgesuncc.github.io/tutorials/Symbol_Collection.html
#
class Polygon(Symbol):

    def __init__(self, pts = None):
        super(Polygon, self).__init__()
        if pts is not None:
            self.points = pts
        else:
            self.points = []
        self.shape = "polygon"

    def get_name(self):
        return "polygon"

    def add_point(self, x, y):
        fx = float(x)
        fy = float(y)

        if(fx > float('-inf') and fx < float('inf') and fy > float('-inf') and fy < float('inf')):
            self.points.append(fx)
            self.points.append(fy)

    def get_points(self):
        return self.points

    def set_polygon(self, pts):
        self.points = pts

    def get_dimensions(self):
        minx = float('inf')
        miny = float('inf')
        maxx = float('-inf')
        maxy = float('-inf')

        x = 0.0
        y = 0.0
        for i in range(0,len(self.points),2):
            x = self.points[i]
            y = self.points[i+1]
            if (x < minx):
                minx = x
            if (x > maxx):
                maxx = x
            if (y < miny):
                miny = y
            if (y > maxy):
                maxy = y

        return [minx, maxx, miny, maxy]

    def get_json_representation(self):

        ds_json = super(Polygon, self).get_json_representation()
        ds_json["name"] = self.get_label()
        ds_json["shape"] = self.get_name()
        ds_json["points"] = self.points

        return ds_json
