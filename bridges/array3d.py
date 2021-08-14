from bridges.array import *

class Array3D(Array):
    """
    @brief This class can be used to create three dimensional arrays of 
    type Element<E>.
    
    @author 	Matthew Mcquaigue, Kalpathi Subramanian
    
    @date  	7/18/19, 12/29, 20
    
    This class can be used to create three dimensional arrays of 
    type Element<E>  where E is a generic object representing application 
    specific data.
    
    Arrays are internally represented as 1D arrays; currently 1D, 2D  and
    3D arrays are supported.
    
    Example Tutorial at: https://bridgesuncc.github.io/tutorials/Array.html 
    (1D, 2D, and 3D Array)<br>
    """

    def __init__(self, **kwargs):
        """
        Create an array object with the specified dimensions
        Kwargs:
            (list) dims: size of each dimension
            (int) rows: number of rows
            (int) cols: number of columns
            (int) slices: number of slices
        """
        super(Array3D, self).__init__()
        if 'dims' in kwargs:
            self.set_size(3, kwargs['dims'])
            self.num_cols = kwargs['dims'][0]
            self.num_rows = kwargs['dims'][1]
            self.num_slices = kwargs['dims'][2]
        elif 'slices' in kwargs and 'rows' in kwargs and 'cols' in kwargs:
            dims = [kwargs['cols'], kwargs['rows'], kwargs['slices']]
            self.set_size(3, dims)
            self.num_cols = kwargs['cols']
            self.num_rows = kwargs['rows']
            self.num_slices = kwargs['slices']
        else:
            self.num_cols = 0
            self.num_rows = 0
            self.num_slices = 0
            self.size = 0
