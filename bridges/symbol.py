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


    def __init__(self):
        """
        Constructor for a Symbol
        """
        self._label = None
        self._fill_color = None
        self._stroke_color = None
        self._opacity = None
        self._stroke_width = None
        self._stroke_dash = None
        self._layer = None
        self._transform = None
        self._xform = [[0.0 for i in range(3)] for j in range(3)] #3x3
        self._xform_flag = False
        self.identity(self._xform)

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

    def get_shape_type(self):
        return ""

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
    def layer(self) -> int:
        return self._layer

    @layer.setter
    def layer(self, l: int):
        self._layer = l

    @property
    def xform(self):
        return self._xform


    def print_mat(self, m: list):
        """
        print the current matrix for debugging
        :param m: 3x3 matrix as 2d list to be printed
        """
        for i in range(3):
            for j in range(3):
                print(m[i][j] + ",")
        print("\n")

    def identity(self, m: list) -> list:
        """
        create the identity matrix
        :param m: is a 3x3 input matrix as a 2d list
        :return: a 2d list as a 3x3 identity matrix
        """
        for i in range(3):
            for j in range(3):
                if i == j:
                    m[i][j] = 1.0
                else:
                    m[i][j] = 0.0

        return m

    def mat_mult(self, m1: list, m2: list) -> list:
        result = [[0.0 for i in range(3)] for j in range(3)]
        print(m2)
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += m1[i][k] * m2[k][j]

        print(result)

        return result

    def vec_mat_mult(self, m: list, v: list) -> list:
        v_out = [m[0][0]*v[0] + m[0][1]*v[1] + m[0][2] * v[2],
				m[1][0]*v[0] + m[1][1]*v[1] + m[1][2] * v[2],
				1.0]

        return v_out


    def translate(self, tx: float, ty: float):
        transl = [[0.0 for i in range(3)] for j in range(3)]

        self.identity(transl)

        #apply transform
        transl[0][2] = tx
        transl[1][2] = ty

        #update symbol transform matrix
        self._xform = self.mat_mult(self._xform, transl)

        self._xform_flag = True

    def scale(self, *args):
        """
        scale the symbol from a particular center location

        if args is a single float, then scale both dimensions from the origin (what you want in 99% of cases)

        if args is two floats, scale x based on args[0] and y based on args[1] from the origin

        if args is four float, scale x based on args[0] and y based on args[1] from point args[2],args[3]
        """        
        if len(args) == 1:
            scale_m = [[args[0], 0.0, 0.0], [0.0, args[0], 0.0], [0.0, 0.0, 1.0]]
            
            self._xform = self.mat_mult(self._xform, scale_m)
        elif len(args) == 2:

            scale_m = [[args[0], 0.0, 0.0], [0.0, args[1], 0.0], [0.0, 0.0, 1.0]]
            
            self._xform = self.mat_mult(self._xform, scale_m)
        elif len(args) == 4:
            scale_m = [[args[0], 0.0, 0.0], [0.0, args[1], 0.0], [0.0, 0.0, 1.0]]

            transl_pre = [[1.0, 0.0, -args[2]], [0.0, 1.0, -args[3]], [0.0, 0.0, 1.0]]
            transl_post = [[1.0, 0.0, args[2]], [0.0, 1.0, args[3]], [0,0, 0.0, 1.0]]

            scale_comp = self.mat_mult(transl_post, self.mat_mult(scale_m, transl_pre))

            self._xform =self.mat_mult(self._xform, scale_comp)


        self._xform_flag = True

    def rotate(self, *args):
        if len(args) == 1:
            rotate_m = [[0.0 for i in range(3)] for j in range(3)]

            self.identity(rotate_m)

            angle_r = args[0] * (math.pi / 180.0)
            cos_a = math.cos(angle_r)
            sin_a = math.sin(angle_r)

            rotate_m[0][0] = rotate_m[1][1] = cos_a
            rotate_m[0][1] = -sin_a
            rotate_m[1][0] = sin_a

            self._xform = self.mat_mult(self._xform, rotate_m)
        elif len(args) == 3:
            angle_r = args[0] * (math.pi / 180.0)
            cos_a = math.cos(angle_r)
            sin_a = math.sin(angle_r)

            rotate_m = [[cos_a, -sin_a, 0.0], [sin_a, cos_a, 0.0], [0.0, 0.0, 1.0]]
            transl_pre = [[1.0, 0.0, -args[1]], [0.0, 1.0, -args[2]], [0.0, 0.0, 1.0]]
            transl_post = [[1.0, 0.0, args[1]], [0.0, 1.0, args[2]], [0, 0, 0.0, 1.0]]

            rot_comp = self.mat_mult(transl_post, self.mat_mult(rotate_m, transl_pre))

            self._xform = self.mat_mult(self._xform, rot_comp)


        self._xform_flag = True

    def set_transform(self, a:float, b:float, c:float, d:float, e:float, f:float):
        self._xform[0][0] = a
        self._xform[0][1] = c
        self._xform[0][2] = e
        self._xform[1][0] = b
        self._xform[1][1] = d
        self._xform[1][2] = f
        self._xform[2][0] = 0.0
        self._xform[2][1] = 0.0
        self._xform[2][2] = 1.0

        self._xform_flag = True


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
        ds["type"] = self.get_shape_type()
        if self.fill_color is not None:
            ds['fill-color'] = [self.fill_color.red, self.fill_color.green, self.fill_color.blue, self.fill_color.alpha]
        if self.opacity is not  None:
            ds['opacity'] = self.opacity
        if self._xform_flag:
            ds['transform'] = [self._xform[0][0], self._xform[1][0], self._xform[0][1], self._xform[1][1], self._xform[0][2], self._xform[1][2]]
        if self.label is not None:
            ds['label'] = self.label
        if self.stroke_color is not None:
            ds['stroke-color'] = [self.stroke_color.red, self.stroke_color.green, self.stroke_color.blue, self.stroke_color.alpha]
        if self.stroke_width is not None:
            ds['stroke-width'] = self.stroke_width
        if self.stroke_dash is not None:
            ds['stoke-dasharray'] = self.stroke_dash
        if self.layer is not None:
            ds['layer'] = self.layer
        return ds

    def add_all_json(self, symbol_json, parent):
        id = len(symbol_json)

        obj = self.get_json_representation()

        obj['ID'] = id

        if parent is not None:
            obj['parentID'] = parent

        symbol_json.append(obj)

