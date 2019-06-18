from bridges.color import *

class Symbol:
    _ids = 0 #id for this symbol. Class level so each object has unique id

    def __init__(self):
        """
        Constructor for a Symbol
        """
        self.identifier = str(Symbol._ids)
        self.label = ""
        self.fill_color = Color("blue")
        self.stroke_color = Color("white")
        self.opacity = 1.0
        self.stroke_width = 1.0
        self.stroke_dash = 1
        self.location_y = 0.0
        self.location_x = 0.0
        Symbol._ids += 1

    def _get_data_structure_type(self) -> str:
        """
        Get the data structure type
        Returns:
            str
        """
        return "Symbol"

    @property
    def label(self) -> str:
        """
        Getter for symbol label
        Returns:
            str
        """
        return self.label

    @label.setter
    def label(self, label: str) -> None:
        """
        Setter for symbol label
        Args:
            label: String to be label
        Returns:
            str
        """
        self.label = label

    @label.deleter
    def label(self) -> None:
        """
        Deleter for label
        Returns:
            None
        """
        del self.label

    @property
    def identifier(self) -> str:
        """
        Getter for the symbols identifier
        Returns:
            str
        """
        return self.identifier

    @property
    def fill_color(self) -> Color:
        """
        Getter for the fill color
        Returns:
            Color
        """
        return self.fill_color

    @fill_color.setter
    def fill_color(self, color: Color) -> None:
        """
        Setter for the fill color
        Args:
            color: the color for the fill (Color Object)
        Returns:
            None
        """
        self.fill_color = color

    @property
    def stroke_color(self) -> Color:
        """
        Getter for the stroke color
        Returns:
            Color
        """
        return self.stroke_color

    @stroke_color.setter
    def stroke_color(self, color: Color) -> None:
        """
        Setter for the stroke color
        Args:
            color: the color for the stroke (Color Object)
        Returns:
            None
        """
        self.stroke_color = color

    @property
    def stroke_width(self) -> float:
        """
        Getter for the stroke width
        Returns:
            float
        """
        return self.stroke_width

    @stroke_width.setter
    def stroke_width(self, width: float) -> None:
        """
        Setter for the stroke width
        Args:
            width: the value for the width
        Returns:
            None
        Raises:
            value error
        """
        if width <= 0.0 or width > 10.0:
            raise ValueError("Stroke width must be between 0 and 10")
        else:
            self.stroke_width = width

    @property
    def opacity(self) -> float:
        """
        Getter for opacity
        Returns:
             float
        """
        return self.opacity

    @opacity.setter
    def opacity(self, o: float):
        """
        Setter for opacity
        Args:
            o: the opacity value
        Returns:
            None
        Raises: value error
        """
        if o <= 0.0 or o > 1.0:
            raise ValueError("Opacity must be between 0.0 and 1.0")
        else:
            self.opacity = o

    @property
    def stroke_dash(self) -> float:
        """
        Getter for stroke_dash
        Returns:
             float
        """
        return self.stroke_dash

    @stroke_dash.setter
    def stroke_dash(self, dash: float):
        """
        Setter for stroke_dash
        Args:
            dash: the stroke_dash value
        Returns:
            None
        Raises: value error
        """
        if dash < 0 or dash > 10:
            raise ValueError("Dash must be between 0 and 10 (inclusive)")
        else:
            self.stroke_dash = dash

    def set_location(self, x: float, y: float) -> None:
        """
        Setter for the location of a symbol
        Args:
            x: x location
            y: y location
        Returns:
            None
        Raises:
            Value error
        """
        if x > float('-inf') and x < float('inf') and y > float('-inf') and y < float('inf'):
            self.location_x = x
            self.location_y = y
        else:
            raise ValueError("Coordinates must be real numbers")

    def get_location(self) -> list:
        """
        Getter for the location of a symbol
        Returns:
            list
        """
        return [self.location_x, self.location_y]

    def get_dimensions(self) -> list:
        """
        Getter for the dimensions
        Returns:
            list
        """
        return [0.0, 0.0, 0.0, 0.0]

    def _get_json_representation(self) -> dict:
        """
        Get the json representation of the Symbol class
        Returns:
            dict
        """
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

