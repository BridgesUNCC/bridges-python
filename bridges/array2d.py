from bridges.array import *

class Array2D(Array):
    """
    brief This class can be used to create 2D arrays of type Element<E>.
    
    @author 	Kalpathi Subramanian, Matthew McQuaigue
    
    @date  	10816, 51717, 53018
    
    This class can be used to create arrays of type Element<E>  where E
    is a generic object representing application specific data.
    
    Arrays are internally represented as 1D arrays; currently 1D, 2D  and
    3D arrays are supported.
    
    Example Tutorial at: http:bridgesuncc.github.iotutorialsArray.html 
    (1D, 2D, and 3D Array)<br>
    """

    def __init__(self, rows=None, cols=None):
		##
		# @brief Create an array object with the specified dimensions
		# @param rows  number of rows in array (int)
        # @param cols  number of cols in array (int)
        super(Array2D, self).__init__()
        if rows is not None and cols is not None:
            dim = [cols, rows, 1]
            self.num_rows = rows
            self.num_cols = cols
            self.set_size(2, dim)
        else:
            self.size = 0
            self.num_rows = 0
            self.num_cols = 0
