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
    
    \sa Shape collection tutorial, http://bridgesuncc.github.io/tutorials/Symbol_Collection.html
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
        self._shape_type = "polyline"

    def get_name(self):
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

    def get_dimensions(self):
        """
        Get the bounding box of the polyline.
        """
        minx = float('inf')
        miny = float('inf')
        maxx = float('-inf')
        maxy = float('-inf')

        for i in range(0, len(self.points), 2):
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

    def translate(self, tx, ty):
        """
        Translate the polyline by tx, ty along X and Y respectively
        Args:
           tx: translation factor in X
           ty: translation factor in Y
        """
        for k in range(0, len(self.points), 2):
            self.points[k] = self.points[k] + tx
            self.points[k + 1] = self.points[k+1] + ty

    def rotate(self, angle):
        """
        Rotat the polyline by 'angle' (2D rotation) 
        Args:
           angle: angle of rotation in degrees
        """
        center = []
        center = self.get_center(center)
        transl = []
        transl[0] = -center[0]
        transl[1] = -center[1]
        self.translate(transl[0], transl[1])
        for k in range(0, len(self.points), 2):
            tmp = []
            tmp[0] = self.points[k]
            tmp[1] = self.points[k+1]
            tmp = self.rotate_point(tmp, angle)
            self.points[k] = tmp[0]
            self.points[k+1] = tmp[1]
        transl[0] = center[0]
        transl[1] = center[1]
        self.translate(transl[0], transl[1])

    def scale(self, sx, sy):
        """
        Scale the polyline by sx, sy along X and Y respectively
        Args:
           sx: scale factor in X
           sy: scale factor in Y
        """
        center = []
        center = self.get_center(center)
        transl = []
        transl[0] = -center[0]
        transl[1] = -center[1]
        self.translate(transl[0], transl[1])
        for k in range(0, len(self.points), 2):
            self.points[k] = self.points[k] * sx
            self.points[k+1] = self.points[k+1] * sy
        transl[0] = center[0]
        transl[1] = center[1]
        self.translate(transl[0], transl[1])

    def get_center(self, center):
        """
        Get the center of the polyline (use the bounding box center)
        Args:
            center : [output] returns the computed center as a 2 element list
        """
        bbox = []
        bbox[0] = bbox[1] = 100000.0
        bbox[2] = bbox[3] = -10000.0
        for k in range(0, len(self.points), 2):
            if self.points[k] < bbox[0]:
                bbox[0] = self.points[k]
            if self.points[k] > bbox[2]:
                bbox[2] = self.points[k]
            if self.points[k+1] < bbox[1]:
                bbox[1] = self.points[k+1]
            if self.points[k+1] > bbox[3]:
                bbox[3] = self.points[k+1]
        center[0] = bbox[0] + (bbox[2] - bbox[0]) / 2.0
        center[1] = bbox[1] + (bbox[3] - bbox[1]) / 2.0
        return center

    def get_json_representation(self):

        ds_json = super(Polyline, self).get_json_representation()
        ds_json["name"] = self.label
        ds_json["shape"] = self.shape_type
        ds_json["points"] = self.points

        return ds_json
