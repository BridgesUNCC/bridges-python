#!/usr/bin/env python
# package: bridges.base
from Element import *

##
# @brief This class can be used to create arrays of type Element<E>.
#
# @author 	Kalpathi Subramanian
#
# @date  	10/8/16, 5/17/17
#
#	This class can be used to create arrays of type Element<E>  where E
#	is a generic object representing application specific data.
#
#	Arrays are internally represented as 1D arrays; currently 1D, 2D  and
#	3D arrays are supported.
#
# @param <E> The generic parameter object that is part of this element, representing
#          application specific data.
#
#  \sa Example Tutorial at <br>
#		http://bridgesuncc.github.io/Hello_World_Tutorials/ARRAY1D.html (1D Array)<br>
#		http://bridgesuncc.github.io/Hello_World_Tutorials/ARRAY2D.html (2D Array)<br>
#		http://bridgesuncc.github.io/Hello_World_Tutorials/ARRAY3D.html (3D Array)
#
#
class Array(object):
    QUOTE = "\""
    COMMA = ","
    COLON = ":"
    OPEN_CURLY = "{"
    CLOSE_CURLY = "}"
    OPEN_PAREN = "("
    CLOSE_PAREN = ")"
    OPEN_BOX = "["
    CLOSE_BOX = "]"

    array_data = []
    num_dims = int()

    #  only 2D and 3D arrays supported
    dims = [1, 1, 1]

    #  array dimensions
    size = int()


    ##
    # Construct a default array object
    #
    def __init__(self, num_dims = None, dims = None, num_elements = None, x_dim = None, y_dim = None, z_dim = None):
        if num_dims is None and dims is None and num_elements is None and x_dim is None and y_dim is None and z_dim is None:
            self.array_data = []
            self.num_dims = 1
            self.dims[0] = self.dims[1] = self.dims[2] = self.size = 0
        elif num_dims is not None and dims is not None:
            self.set_num_dimensions(num_dims)
            self.set_dimensions(dims)
        elif num_elements is not None:
            self.set_num_dimensions(1)
            self.dims[0] = num_elements
            self.dims[1] = self.dims[2] = 1
            self.set_dimensions(self.dims)
        elif x_dim is not None and y_dim is not None and z_dim is not None:
            self.set_num_dimensions(3)
            self.dims[0] = x_dim
            self.dims[1] = y_dim
            self.dims[2] = z_dim
            self.set_dimensions(self.dims)
        elif x_dim is not None and y_dim is not None and z_dim is None:
            self.set_num_dimensions(2)
            self.dims[0] = x_dim
            self.dims[1] = y_dim
            self.dims[2] = 1
            self.set_dimensions(self.dims)



    ##
    #	This method gets the data structure type
    #
    #	@return  The date structure type as a string
    #
    def get_data_structure_type(self):
        if (self.num_dims >= 1) and (self.num_dims <= 3):
            return "Array"
        else:
            raise ValueError("Invalid number of dimensions. Only 1D, 2D and 3D arrays supported at this time")

    ##
    #
    #	Set the number of dimensions of the array;
    #
    #	@param nd  number of dimensions
    #
    def set_num_dimensions(self, nd):
        if nd > 3:
            raise ValueError("Invalid number of dimensions. Only 1D, 2D and 3D arrays supported at this time")
        self.num_dims = nd

    ##
    #
    #	Get the number of dimensions of the array;
    #
    #	@return   number of dimensions
    #
    def get_num_dimensions(self):
        if self.num_dims > 3:
            raise ValueError("Invalid number of dimensions. Only 1D, 2D and 3D  arrays supported at this time")
        return self.num_dims

    ##
    #
    #	Set the size of each dimensions; also allocates  array space
    #
    #	@param dim[]  size of each dimension
    #
    def set_dimensions(self, dim):
        sz = 1
        k = 0
        while k < self.num_dims:
            self.dims[k] = dim[k]
            sz *= dim[k]
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

    ##
    #
    #	Get the size of each dimensions;
    #
    #	@param dims[]  size of each dimension is returned
    #
    def get_dimensions(self, dim):
        dim[0] = self.dims[0]
        dim[1] = self.dims[1]
        dim[2] = self.dims[2]

    ##
    #
    #	Get the array size
    #
    #	@return size
    #
    def get_size(self):
        return self.size

    def get_element(self, indx = None, x= None, y = None, z= None):
        if indx is not None:
            return self.array_data[indx]
        elif x is not None and y is not None and z is None:
            return self.array_data[y*self.dims[1]+ x]
        elif x is not None and y is not None and z is not None:
            return self.array_data[z*self.dims[0]*self.dims[1] + y*self.dims[0] + x]

    def set_element(self, indx = None, el = None, x = None, y = None, z = None):
        if indx is not None and el is not None:
            self.array_data[indx] = el
        elif el is not None and x is not None and y is not None and z is not None:
            self.array_data[z * self.dims[0] * self.dims[1] + y * self.dims[0] + x] = el
        elif el is not None and x is not None and y is not None and z is None:
            self.array_data[y * self.dims[0] + x] = el


    ##
    #
    #	Get the object at 'indx'
    #
    #	@param indx  index into the array
    #	@return Element<E>  object at 'indx'
    #
    def get_value(self, indx = None, col = None, row = None, slice = None):
        if col is not None and row is not None and slice is None:
            return self.array_data[row * self.dims[0] + col]
        if col is not None and row is not None and slice is not None:
            return self.array_data[slice * self.dims[0] * self.dims[1] + row * self.dims[0] + col]
        if col is None and row is None and slice is None and indx is not None:
            return self.array_data[indx]

    ##
    #
    #	Set the input object at 'indx'
    #
    #	@param indx  index into the array
    #	@param el  element object to be assigned at 'indx'
    #
    #
    #
    def set_value(self, indx = None, col = None, row = None, slice = None, el = None):
        if indx is not None and el is not None:
            self.array_data[indx] = el
        if col is not None and row is not None and el is not None and indx is None:
            self.array_data[row * self.dims[0] + col] = el
        if col is not None and row is not None and el is not None and slice is not None and indx is None:
            self.array_data[slice* self.dims[0] * self.dims[1] + row * self.dims[0] + col] = el


    ##
    # Generating the JSON string for a Bridges array object (Array<E>[])
    #
    # @param Bridges Array object
    #
    # @return JSON string
    #
    def get_data_structure_representation(self):
        nodes_JSON = str()
        links_JSON = str()

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
