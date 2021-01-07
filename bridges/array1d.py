from bridges.array import *

class Array1D(Array):
    """
    @brief This is a class can be used to create 1 dimensional arrays of type Element<E>.
    
    @author 	Kalpathi Subramanian, Matthew McQuaigue
    
    @date  	7/18/19
    
    This class can be used to create 1D arrays of type Element<E>  where E
    is a generic object representing application specific data.
    
    Array1D has iterator semantic to enable range for loops. For instance,
    
    \code{java}
    Array1D<Integer> arr = something();
    for (Integer i : arr)
        System.out.println(i);
    \endcode
    
    Example Tutorial at: http://bridgesuncc.github.io/tutorials/Array.html (1D, 2D, and 3D Array)<br>
    """


    def __init__(self, sz=None):
        """
        @brief Create a 1D array object
        @param sz number of elements in the array
        """
        super(Array1D, self).__init__()
        if sz is not None:
            self.size = sz
            dim = [sz, 1, 1]
            self.set_size(1, dim)
        else:
            self.size = 0
