#!/usr/bin/env python
from bridges.element import *

class Array():
    """@brief This class can be used to create arrays of type Element.
    
    @author 	Matthew McQuaigue, Erik Saule
    
    @date  	10/8/16, 6/09/19, 7/20/22
    
    This class can be used to create arrays of type Element. Element
    enables to store objects of any types and provide styling features
    for visualization purposes.
    
    Arrays are internally represented as 1D arrays; currently 1D, 2D  and
    3D arrays are supported.
    
    Example Tutorial at: https://bridgesuncc.github.io/tutorials/Array.html (1D, 2D, and 3D Array)

    """

    dims = [1,1,1] #used for setting size of array based on dimensions
    def __init__(self, **kwargs):
        """
        Array constructor
        Kwargs:
            dims: size of each dimension (array)
            num_dims: The dimensions of the array (1-3). Defaults to 1 dimension (int)
        Returns:
            None
        """
        self._dims = [1, 1, 1]
        self._array_data = []
        self._num_dims = 1
        self._size = 0
        if 'num_dims' in kwargs:
            if 'dims' in kwargs:
                self.set_size(kwargs['num_dims'], kwargs['dims'])

    @property
    def num_dims(self) -> int:
        """
        Getter for representing the number of dimensions in the array
        Returns:
            int: number of dimensions
        """
        return self._num_dims

    @num_dims.setter
    def num_dims(self, value: int) -> None:
        """
        Setter function for the number of dimensions for the array
        Args:
            value: An integer for the number of dimensions (Between 1 and 3 inclusive)
        Returns:
            None
        Raises:
            ValueError: if dimension passed in is < 1 or > 3
        """
        if value > 3:
            raise ValueError("Invalid number of dimensions. Only 1D, 2D and 3D arrays supported at this time")
        self._num_dims = value

    @property
    def size(self) -> int:
        """
        Getter for representing the size of array
        Returns:
            int: the size
        """
        return self._size

    @size.setter
    def size(self, sz: int) -> None:
        """
        Setter for representing the size of the array
        Args:
            (int) sz: The size to be set for array
        Returns:
            None
        """
        self._size = sz

    def set_size(self, nd: int, dim: list) -> None:
        """
        Set the size of each dimensions; also allocates  array space
        Args:
            (int) nd: number of dimensions
            (list) dim: size of each dimension
        Returns:
            None
        """
        if dim[0] <=0 or dim[1] <=0 or dim[2] <= 0:
            raise ValueError("Invalid dimension value, must be  positive")

        self._dims[0] = dim[0]
        self._dims[1] = dim[1]
        self._dims[2] = dim[2]
        self.num_dims = nd
        self.size = dim[0]*dim[1]*dim[2]

        for k in range(0, self.size):
            self._array_data.append(Element())


    def get_data_structure_type(self) -> str:
        """
        Gets the data structure type
        Raises:
            ValueError: if number of dimensions is < 1 or > 3
        Returns:
            str: type of data structure
        """
        if (self.num_dims >= 1) and (self.num_dims <= 3):
            return "Array"
        else:
            raise ValueError("Invalid number of dimensions. Only 1D, 2D and 3D arrays supported at this time")

    def get_dimensions(self) -> list[int]:
        """
        Get the size of each dimensions
        Returns:
            list: size of each dimension
        """
        return self._dims

    def get_element(self, *args, **kwargs) -> Element:
        """
        Getter function for an element in the array at given position
        args:
            (int) x,y,z,: indices
        Kwargs:
            (int) index: the index of array to get in array
            (int) x: column index into array
            (int) y: row index into array
            (int) z: slice index into array
        Returns:
            Element: the element at position given
        """
        if len(args) != 0:
            if len(args) != self._num_dims:
                raise IndexError("args must be same length as dims")
            if len(args) == 1:
                return self._array_data[args[0]]
            if len(args) == 2:
                return self._array_data[args[0] * self._dims[0] + args[1]]
            if len(args) == 3:
                return self._array_data[args[0] * self._dims[0] * self._dims[1] + args[1] * self._dims[0] + args[2]]

        elif 'index' in kwargs:
            return self._array_data[kwargs['index']]
        elif 'x' in kwargs and 'y' in kwargs:
            if 'z' in kwargs:
                return self._array_data[kwargs['z'] * self._dims[0] *
                                        self._dims[1] + kwargs['y'] * self._dims[0] + kwargs['x']]
            else:
                return self._array_data[kwargs['y'] * self._dims[0] + kwargs['x']]

    def set_element(self, *args, **kwargs):
        """
        Setter function for an element in the array at given position
        Args:
            (int) x,y,z: indices
            (Element) el: element object to be assigned to index, always last position arg if using unnamed args
        Kwargs:
            (Element) el: element object to be assigned to index
            (int) index: the index of array to get in array
            (int) x: column index into array
            (int) y: row index into array
            (int) z: slice index into array
        Returns:
            None
        """
        if len(args) == 0 and kwargs["element"] is None:
            raise RuntimeError("Must have at least 1 unnamed element parameter or named element parameter")
        if len(args) != self._num_dims + 1 and len(args) != 1:
            raise RuntimeError("Must used proper indices if not using kwargs")
        else:
            if len(args) == 2:
                self._array_data[args[0]] = args[1]
            if len(args) == 3:
                self._array_data[args[1] * self._dims[0] + args[0]] = args[2]
            if len(args) == 4:
                self._array_data[args[2] * self._dims[0] * self._dims[1] + args[1] * self._dims[0] + args[0]] = args[3]

        if 'index' in kwargs:
            self._array_data[kwargs['index']] = args[0]
        if 'x' in kwargs and 'y' in kwargs:
            if 'z' in kwargs:
                self._array_data[kwargs['z']*self._dims[0]*self._dims[1] + kwargs['y']*self._dims[0] + kwargs['x']] = args[0]
            else:
                self._array_data[kwargs['y']*self._dims[1]+ kwargs['x']] = args[0]

    def __getitem__(self, item):
        """
        :param  (tuple) item: indices
        :return: element at index
        """
        if type(item) == int:
            if self._num_dims != 1:
                raise IndexError("invalid index, pass a tuple of same length of number of dimensions of your array")
            return self.get_element(item)
        if len(item) != self._num_dims:
            raise IndexError("invalid index, pass a tuple of same length of number of dimensions of your array")

        return self.get_element(*item)

    def __setitem__(self, key, value):
        if type(key) == int:
            if self._num_dims != 1:
                raise IndexError("invalid index, pass a tuple of same length of number of dimensions of your array")
            self.set_element(key, value)
            return
        if len(key) != self._num_dims:
            raise IndexError("invalid index, pass a tuple of same length of number of dimensions of your array")
        self.set_element(*key, value)

    def get_data_structure_representation(self) -> dict:
        """
        Generating the JSON string for a bridges array object
        Returns:
            dict: the dict that will represent the json when dumped
        """
        #add json representation for each element to dict
        i = 0
        nodes_json = []
        while i < self.size:
            if self._array_data[i] is not None:
                nodes_json.append(self._array_data[i].get_element_representation())
            i += 1
        json_dict = {
            "nodes": nodes_json,
            "dims": [self._dims[0], self._dims[1], self._dims[2]]
        }
        return json_dict
