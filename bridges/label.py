import json
import math
from bridges.symbol import *

class Label(Symbol):
    """
    @brief This class provides support for text labels to be associated with shapes. 
    
    Labels have width, height, font size.
    
    \sa Shape collection tutorial, https://bridgesuncc.github.io/tutorials/Symbol_Collection.html
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

    @property
    def rotation_angle(self) -> None:
        """
        Returns the rotation angle of the label

        Returns:
            rotation angle (in degrees)
        """
        return self._rotation_angle

    @rotation_angle.setter
    def rotation_angle(self, angle: float) -> None:
        """
        Set the orientation of the label text
        Only, horizontal, vertical and 45 deg. text is supported

        Args:
            angle: rotation angle (in degrees)
        Returns:
            None
        """
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
        bbox_width = length
        bbox_height = height
        angle = self._rotation_angle
        loc_x = self.get_location()[0]
        loc_y = self.get_location()[1] 
        bbox = [0., 0., 0., 0.]
        pt = [0., 0.]
        bbox[0] = bbox[1] = float("inf")
        bbox[2] = bbox[3] = float("-inf")

         # rotate  the four corners of the bounding box
         # only need to rotate the 3 points of the box
        for k in range(4):
             if k == 0:       # lower left
                 pt[0] = pt[1] = 0.
             elif k == 1:     # upper left
                 pt[0] = 0. 
                 pt[1] = bbox_height;
             elif k == 2:     # lower right
                 pt[0] = bbox_width 
                 pt[1] = 0.;
             elif k == 3:     # upper right
                 pt[0] = bbox_width;
                 pt[1] = bbox_height; 

             self.rotate_point (pt, angle);
             # update bounding box
             if pt[0] < bbox[0]: 
                 bbox[0] = pt[0]
             if pt[1] < bbox[1]:
                 bbox[1] = pt[1]
             if pt[0] > bbox[2]:
                 bbox[2] = pt[0]
             if pt[1] > bbox[3]: 
                 bbox[3] = pt[1]

        #translate center of box to center of label
        tx = loc_x - (bbox[0] + (bbox[2]-bbox[0])/2.);
        ty = loc_y - (bbox[1] + (bbox[3]-bbox[1])/2.);
        bbox[0] += tx; 
        bbox[1] += ty; 
        bbox[2] += tx;
        bbox[3] += ty;

        return bbox

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
        ds_json["angle"] = self._rotation_angle
        ds_json["font-size"] = self.font_size

        return ds_json
