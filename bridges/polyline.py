import json
from bridges.symbol import *

class Polyline(Symbol):
    """
    @brief This class defines a polygon and is part of the symbol collection.
    
    A polygon has a set of vertices, with vertices connected by line
    segments. It differs from the polyline in the sense that the last
    and first vertex are connect to close the shape.
    
    @author David Burlinson, Kalpathi Subramanian
    
    @date 2018, 7/23/19, 1/2/21
    
    \sa Shape collection tutorial, https://bridgesuncc.github.io/tutorials/Symbol_Collection.html
    """

    def __init__(self, pts = None):
        """
        Constructor. Sets the number of points in the polyline
        Args:
            pts: number of points to be used in constructing the polyline
        """
        super(Polyline, self).__init__()
        if pts is not None:
            self._points = pts
        else:
            self._points = []

    def get_shape_type(self):
        """
        Get the name of the symbol
        Returns:
            the symbol name
        """
        return "polyline"

    def add_point(self, x, y):
        """
        Add  a point to the polyline
        Args:
            x:  point's x coordinate
            y:  point's y coordinate
        """
        fx = float(x)
        fy = float(y)

        if(fx > float('-inf') and fx < float('inf') and fy > float('-inf') and fy < float('inf')):
            self._points.append(fx)
            self._points.append(fy)

    @property
    def points(self):
        """
        Get the number of points in polyline
        Returns:
            the number of points in symbol.
        """
        return self._points

    @points.setter
    def points(self, pts):
        """
        Set the number of points in polyline
        Args:
            pts: the number of points in symbol.
        """
        self._points = pts


    def get_json_representation(self):

        ds_json = super(Polyline, self).get_json_representation()
        ds_json["points"] = self.points

        return ds_json
