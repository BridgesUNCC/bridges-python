import json
from bridges.symbol import *

class Label(Symbol):
    """
    @brief This class provides support for text labels to be associated with shapes. 
    
    Labels have width, height, font size.
    
    \sa Shape collection tutorial, http://bridgesuncc.github.io/tutorials/Symbol_Collection.html
    
    
    \sa Shape collection tutorial, http://bridgesuncc.github.io/tutorials/Symbol_Collection.html
    """
    def __init__(self, label = None):
        super(Label, self).__init__()
        if label is not None:
            super(Label, self).label = label
        self._width = 100
        self._height = 50
        self._font_size = 12

    @property
    def width(self) -> int:
        """
        Getter for the width of label
        Returns:
            int: the width
        """
        return self._width

    @width.setter
    def width(self, w: int) -> None:
        """
        Setter for the width of label
        Args:
            (int) w: the width
        Returns:
            None
        """
        self._width = w

    @property
    def height(self) -> int:
        """
        Getter for the height of label
        Returns:
            int: the height
        """
        return self.height

    @height.setter
    def height(self, h: int) -> None:
        """
        Setter for the height of label
        Args:
            (int) h: the height
        Returns:
            None
        """
        self.height = h

    @property
    def font_size(self) -> int:
        """
        Getter for the font size
        Returns:
            int: representing the font size
        """
        return self._font_size

    @font_size.setter
    def font_size(self, size: int) -> None:
        """
        Setter for the font size
        Args:
            size: the size of the font
        Returns:
            None
        Raises:
            ValueError: if the size of the font is <= 0 or > 200
        """
        if size <= 0 or size > 200:
            raise ValueError("Please use font size between 0 and 200")
        else:
            self._font_size = size

    def get_dimensions(self):
        """
        Get the dimensions of the label
        Returns:
            list: representing the label dimensions
        """
        length = 0.09 * self.font_size * len(super(Label, self).label)
        x = self.get_location()[0]
        y = self.get_location()[1]

        return [x - length/2, x + length/2, y, y]

    def get_json_representation(self) -> dict:
        """
        Getter for the json representation
        Returns:
            dict: JSON represnted as a dict before the dump
        """
        ds_json = super(Label,self).get_json_representation()
        ds_json["name"] = super(Label, self).label
        ds_json["shape"] = "text"
        ds_json["font-size"] = self.font_size

        return ds_json
