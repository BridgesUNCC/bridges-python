import json
import math
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
        self._font_size = 12.
        self._rotation_angle = 0.

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

    def rotation_angle(self) -> float:
        """
        Returns the rotation angle of the label

        Returns:
            rotation angle (in degrees)
        """
        print("calling rotation angle getter..")
        return self._rotation_angle

    def rotation_angle(self, angle: float) -> None:
        """
        Set the orientation of the label text
        Only, horizontal, vertical and 45 deg. text is supported

        Args:
            angl: rotation angle (in degrees)
        Returns:
            None
        """
        print("calling rotation angle setter..")
        print ("Angle1:" + str(angle))
        self._rotation_angle = angle

    def get_bounding_box(self):
        """
        Get the bounding box of the label. Only single line, upper, lower
        case alphabetical characters and spaces supported
        Returns:
            list: representing the label bounding box
        """
        label_text = super(Label, self).label
        length = 0.
        upper_case_exists = False

        for ch in label_text:
            if ch.islower():
                if (ch == 'm' or ch == 'w'):
                    length += 0.6
                elif (ch == 'i' or ch == 'l' or ch == 'j'):
                    length += 0.4
                else: 
                    length += 0.5
            elif ch.isupper():
                upper_case_exists = True
                if (ch == 'M' or ch == 'W'):
                    length += 0.72
                elif  (ch == 'I'): 
                    length += 0.52
                else:
                    length += 0.62
            else:  
                #support spaces only, no special chars
                length += 0.55

            length *= self._font_size;

            width = length
            height = self._font_size
            if upper_case_exists: 
                height += 0.3*self._font_size
            else:
                height += 0.1*self._font_size

            # account for text orientation to compute bounding box
            # support for 0, 45 and 90 deg. only
            bbox_width = length
            bbox_height = height
            angle = self._rotation_angle
            print ("Angle:" + str(self._rotation_angle))
            if (angle == 90. or angle == -90.):
                bbox_width = height
                bbox_height = length
            elif (angle == -45. or angle == 45.): 
                bbox_width  = length/math.sqrt(2.0)
                bbox_height = length/math.sqrt(2.0);

            x = self.get_location()[0]
            y = self.get_location()[1] 

            # return bounding box as a list
            return [x - bbox_width/2., y - bbox_height/2., 
                    x + bbox_width/2., y + bbox_height/2.] 

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
