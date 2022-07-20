from bridges.array import *

class Array2D(Array):
    """
    brief This class can be used to create 2D arrays of type Element.
    
    @author 	Kalpathi Subramanian, Matthew McQuaigue, Erik Saule
    
    @date  	10/8/16, 5/17/17, 5/30/18, 7/20/22
    
    This class can be used to create 2D arrays of type Element. Element
    enables to store objects of any types and provide styling features
    for visualization purposes.
    
    Array2D are internally represented as 1D arrays.
    
    Example Tutorial at: https//:bridgesuncc.github.io/tutorials/Array.html 
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
