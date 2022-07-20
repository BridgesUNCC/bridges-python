from bridges.array import *

class Array1D(Array):
    """
    @brief This is a class can be used to create 1 dimensional arrays of type Element.
    
    @author 	Kalpathi Subramanian, Matthew McQuaigue
    
    @date  	7/18/19
    
    This class can be used to create 1D arrays of type Element. Element
    enables to store objects of any types and provide styling features
    for visualization purposes.

    Array1D has iterator semantic to enable range for loops. For instance,
    
    \code{java}
    arr = Array1D(3)
    arr[0] = Element("a")
    arr[1] = Element("b")
    arr[2] = Element("c")
    for el in arr:
        print(el.label)
    \endcode
    
    Example Tutorial at: https://bridgesuncc.github.io/tutorials/Array.html (1D, 2D, and 3D Array)<br>
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
