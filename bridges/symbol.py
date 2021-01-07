from bridges.color import *
import math


class Symbol:
    """
    @brief  This is the base class for constructing simple shapes in BRIDGES.
    
    This is an abstract class for deriving a
    number of Symbol shape objects, for use in a SymbolCollection.
    Symbols correspond to a simplified subset of SVG paths
    and shapes for custom visual representations in BRIDGES.
    
    Users will typically one of the subclasses of this object for creating shapes
    
    Currently shapes supported are rectangle, circle, polygon, polyline and label; each shape
    has a name, location (x, y) and appropriate geometric and non-geometric attributes
    
    @author David Burlinson, Kalpathi Subramanian
    @date 12/24/18, 7/12/19
    """

    _ids = 0 #id for this symbol. Class level so each object has unique id

    def __init__(self):
        """
        Constructor for a Symbol
        """
        self._identifier = str(Symbol._ids)
        self._label = ""
        self._fill_color = Color("white")
        self._stroke_color = Color("white")
        self._opacity = 1.0
        self._stroke_width = 1.0
        self._stroke_dash = 1
        self._location_y = 0.0
        self._location_x = 0.0
        self._shape_type = "circle"
        Symbol._ids += 1

    @property
    def label(self) -> str:
        """
        Getter for symbol label
        Returns:
            str : the label of this shape
        """
        return self._label

    @label.setter
    def label(self, label: str) -> None:
        """
        Setter for symbol label
        Args:
            label: to be set
        Returns:
            str
        """
        self._label = label

    @property
    def identifier(self) -> str:
        """
        Getter for the symbols identifier
        Returns:
            str
        """
        return self._identifier

    @property
    def fill_color(self) -> Color:
        """
        Getter for the fill color
        Returns:
            Color : the current fill color of this symbol
        """
        return self._fill_color

    @fill_color.setter
    def fill_color(self, *args, **kwargs) -> None:
        """
        Setter for the fill color
        Args:
            color: the color to set for the fill
        Returns:
            None
        """
        self._fill_color = Color(*args, **kwargs)

    @property
    def stroke_color(self) -> Color:
        """
        Getter for the stroke color
        Returns:
            the stroke (boundary) color of the shape
        """
        return self._stroke_color

    @stroke_color.setter
    def stroke_color(self, *args, **kwargs) -> None:
        """
        @brief Setter for the stroke color
        Args:
            color: the stroke (boundary) color to set
        Returns:
            None
        """
        self._stroke_color = Color(*args, **kwargs)

    @property
    def stroke_width(self) -> float:
        """
        Getter for the stroke width
        Returns:
            float : the stroke width of the shape
        """
        return self._stroke_width

    @stroke_width.setter
    def stroke_width(self, width: float) -> None:
        """
        Setter for the stroke width
        Args:
            width: the stroke width to set
        Returns:
            None
        Raises:
            value error
        """
        if width <= 0.0 or width > 10.0:
            raise ValueError("Stroke width must be between 0 and 10")
        else:
            self._stroke_width = width

    @property
    def opacity(self) -> float:
        """
        Getter for opacity
        Returns:
             float : opacity of the shape
        """
        return self._opacity

    @opacity.setter
    def opacity(self, o: float):
        """
        Setter for opacity
        Args:
            o: the opacity value to set (must be in 0-1.0 range) 
        Returns:
            None
        Raises: value error
        """
        if o <= 0.0 or o > 1.0:
            raise ValueError("Opacity must be between 0.0 and 1.0")
        else:
            self._opacity = o

    @property
    def stroke_dash(self) -> float:
        """
        Getter for stroke_dash
        Returns:
             float : the stroke texture
        """
        return self._stroke_dash

    @stroke_dash.setter
    def stroke_dash(self, dash: float):
        """
        Setter for stroke_dash
        Args:
            dash: the stroke_dash value to set (0-10 range)
        Returns:
            None
        Raises: value error
        """
        if dash < 0 or dash > 10:
            raise ValueError("Dash must be between 0 and 10 (inclusive)")
        else:
            self._stroke_dash = dash

    @property
    def shape_type(self):
        """
        Get the shape type (string)
        Returns:
            shape name (string)
        """
        return self._shape_type

    @shape_type.setter
    def shape_type(self, shape):
        """
        Set the shape type (string)
        Args:
            shape: shape name to set
        """
        self._shape_type = shape

    def set_location(self, x: float, y: float) -> None:
        """
        Setter for the location of the  center of the symbol
        Args:
            x: x location 
            y: y location
        Returns:
            None
        Raises:
            Value error
        """
        if x > float('-inf') and x < float('inf') and y > float('-inf') and y < float('inf'):
            self._location_x = x
            self._location_y = y
        else:
            raise ValueError("Coordinates must be real numbers")

    def get_location(self) -> list:
        """
        Getter for the location of a symbol
        Returns:
            list : the x and y coordinates of the shape's current location
        """
        return [self._location_x, self._location_y]

    def get_dimensions(self) -> list:
        """
        Getter for the dimensions
        Returns:
            list : the bounding box of this shape (xmin, xmax, ymin, ymax)
        """
        return [0.0, 0.0, 0.0, 0.0]

    def translate_point(self, pt, tx, ty):
        """
        Translate a point by tx, ty along X and Y respectively
        Args:
            pt: 2D point to be translated
            tx: translation factor in X
            ty: translation factor in Y
        """
        pt[0] += tx
        pt[1] += ty
        return pt

    def scale_point(self, pt, sx, sy):
        """
        Scale a point by sx, sy along X and Y respectively
        Args:
            pt: 2D point to be scaled
            sx: scale factor in X
            sy: scale factor in Y
        """
        pt[0] *= sx
        pt[1] *= sy
        return pt

    def rotate_point(self, pt, angle):
        """
        Rotate a point by 'angle' (2D rotation)
        Args:
            pt: 2D point to be rotated
            angle: rotation angle
        """
        angle_r = math.radians(angle)
        c = math.cos(angle_r)
        s = math.sin(angle_r)

        tmp = [pt[0] * c - pt[1] * s, pt[0] * s + pt[1] * c]
        pt[0] = float(tmp[0])
        pt[1] - float(tmp[1])
        return pt

    def get_json_representation(self) -> dict:
        """
        Get the json representation of the Symbol class
        Returns:
            dict : the JSON representation
        """
        ds = {
            # "fill": [self.fill_color.red, self.fill_color.green, self.fill_color.blue, self.fill_color.alpha],
            # "opacity": self.opacity,
            # "stroke": [self.stroke_color.red, self.stroke_color.green, self.stroke_color.blue, self.stroke_color.alpha],
            # "stroke-width": self.stroke_width,
            # "stroke-dasharray": self.stroke_dash,
            # "location": {
            #     "x": self._location_x,
            #     "y": self._location_y
            # }
        }
        if self.fill_color != Color("white"):
            ds['fill'] = [self.fill_color.red, self.fill_color.green, self.fill_color.blue, self.fill_color.alpha]
        if self.opacity != 1.0:
            ds['opacity'] = self.opacity
        if self.stroke_color != Color("white"):
            ds['stroke'] = [self.stroke_color.red, self.stroke_color.green, self.stroke_color.blue, self.stroke_color.alpha]
        if self.stroke_width != 1.0:
            ds['stroke-width'] = self.stroke_width
        if self.stroke_dash != 1:
            ds['stoke-dasharray'] = self.stroke_dash
        if self._location_x != 0.0 or self._location_y != 0.0:
            ds['location'] = {
                "x": self._location_x,
                "y": self._location_y
            }
        return ds

