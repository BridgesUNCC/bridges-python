#!/usr/bin/env python
from bridges.element import *

##
# @brief This class can be used to create arrays of type Element<E>.
#
# @author 	Matthew McQuaigue
#
# @date  	10/8/16, 6/09/19
#
#	This class can be used to create arrays of type Element<E>  where E
#	is a generic object representing application specific data.
#
#	Arrays are internally represented as 1D arrays; currently 1D, 2D  and
#	3D arrays are supported.
#
#
#
class Array():
    QUOTE = "\""
    COMMA = ","
    COLON = ":"
    OPEN_CURLY = "{"
    CLOSE_CURLY = "}"
    OPEN_PAREN = "("
    CLOSE_PAREN = ")"
    OPEN_BOX = "["
    CLOSE_BOX = "]"

    dims = [1,1,1]


    def __init__(self, num_dims, **kwargs):
        """
        Array constructor
        Args:
            num_dims: The dimensions of the array (1-3). Defaults to 1 dimension (int)
        Kwargs:
            dims: size of each dimension (array)
            x_dim: number of elements on the x dimension (int)
            y_dim: number of elements on the y dimension (int)
            z_dim: number of elements on the z dimension (int)
        Returns:
            None
        """
        self.array_data = []
        self.num_dims = num_dims
        self.dims = [1, 1, 1]
        if kwargs:
            if 'dims' in kwargs:
                self._set_dimensions(kwargs['dims'])
                self.dims = kwargs['dims']
            else:
                self.dims[0] = self.dims[1] = self.dims [2] = self.size = 0
            if 'x_dim' in kwargs and num_dims >= 1:
                self.dims[0] = kwargs['x_dim']
            if 'y_dim' in kwargs and num_dims >= 2:
                self.dims[1] = kwargs['y_dim']
            if 'z_dim' in kwargs and num_dims == 3:
                self.dims[2] = kwargs['z_dim']

    @property
    def num_dims(self) -> int:
        """
        Getter for representing the number of dimensions in the array
        Returns:
            int
        """
        return self.num_dims

    @num_dims.setter
    def num_dims(self, value: int) -> None:
        """
        Setter function for the number of dimensions for the array
        Args:
            value: An integer for the number of dimensions (Between 1 and 3 inclusive)
        Returns:
            None
        Raises:
            ValueError
        """
        if value > 3:
            raise ValueError("Invalid number of dimensions. Only 1D, 2D and 3D arrays supported at this time")
        self.num_dims = value

    @num_dims.deleter
    def num_dims(self) -> None:
        """
        Deleter function for the number of dimensions in array
        Returns:
             None
        """
        del self.num_dims

    @property
    def size(self) -> int:
        """
        Getter for representing the size of array
        Returns:
            int
        """
        return self.size

    @size.setter
    def size(self, sz) -> None:
        """
        Setter for representing the size of the array
        Args:
            sz: The size to be set for array (int)
        Returns:
            None
        """
        self.size = sz

    @size.deleter
    def size(self) -> None:
        """
        Deleter function for the size property
        Returns:
            None
        """
        del self.size

    def _get_data_structure_type(self) -> str:
        """
        Gets the data structure type
        Raises:
            ValueError
        Returns:
            str
        """
        if (self.num_dims >= 1) and (self.num_dims <= 3):
            return "Array"
        else:
            raise ValueError("Invalid number of dimensions. Only 1D, 2D and 3D arrays supported at this time")

    def _set_dimensions(self, dim) -> None:
        """
        Sets the size of each dimension and allocates array space
        Args:
            dim: size of each dimension in array
        Returns:
             None
        """
        sz = 1
        k = 0
        while k < self.num_dims:
            Array.dims[k] = dim[k]
            sz = sz * dim[k]
            k += 1
        #  first check the dimensions are all positive
        if sz < 0:
            raise ValueError("Invalid dimension value, must be  positive")
        self.size = sz
        #  allocate space for the array
        k = 0
        while k < self.size:
            self.array_data.append(Element())
            k += 1



    @property
    def element(self, **kwargs) -> Element:
        """
        Getter function for an element in the array at given position
        Kwargs:
            index: the index of array to get in array (int)
            x: column index into array (int)
            y: row index into array (int)
            z: slice index into array (int)
        Returns:
            Element
        """
        if 'index' in kwargs:
            return self.array_data[kwargs['index']]
        if 'x' in kwargs and 'y' in kwargs:
            if 'z' in kwargs:
                return self.array_data[kwargs['z']*self.dims[0]*self.dims[1] + kwargs['y']*self.dims[0] + kwargs['x']]
            else:
                return self.array_data[kwargs['y']*self.dims[1]+ kwargs['x']]

    @element.setter
    def element(self, el: Element, **kwargs) -> None:
        """
        Setter function for an element in the array at given position
        Args:
            el: element object to be assigned to index
        Kwargs:
            index: the index of array to get in array (int)
            x: column index into array (int)
            y: row index into array (int)
            z: slice index into array (int)
        Returns:
            None
        """
        if 'index' in kwargs:
            self.array_data[kwargs['index']] = el
        if 'x' in kwargs and 'y' in kwargs:
            if 'z' in kwargs:
                self.array_data[kwargs['z']*self.dims[0]*self.dims[1] + kwargs['y']*self.dims[0] + kwargs['x']] = el
            else:
                self.array_data[kwargs['y']*self.dims[1]+ kwargs['x']] = el


    def _get_data_structure_representation(self) -> str:
        """
        Generating the JSON string for a bridges array object (Array<E>[])
        Returns:
            str
        """
        nodes_JSON = str()

        i = 0
        while i < self.size:
            if self.array_data[i] is not None:
                nodes_JSON += (self.array_data[i].get_element_representation() + ",")
            i += 1
        #  remove last comma
        nodes_JSON = nodes_JSON[:-1]
        json_str = self.QUOTE + "nodes" + self.QUOTE + self.COLON + self.OPEN_BOX
        json_str += nodes_JSON
        json_str += self.CLOSE_BOX + self.CLOSE_CURLY
        return json_str
