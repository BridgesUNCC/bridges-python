from bridges.bin_tree_element import *
##
#    @brief The BSTElement class is the building block for creating binary search trees.
#
#   The BSTElement class is the building block for creating binary search tree structures.
#    It contains two children (viz., left, right), and a search key, to be used
#    in search operations .
#
#    BSTElement contains a visualizer (ElementVisualizer) object for setting visual
#    attributes (color, shape, opacity, size), necessary for displaying them in a
#    web browser.
#
#    BST Elements also have a LinkVisualizer object, that is used when they are linked to
#    another element, appropriate for setting link attributes, for instance, between
#    the current element and its left or right child
#
#  	@author Kalpathi Subramanian, Mihai Mehedint
#
#  	@date 6/22/16, 1/7/17, 5/17/17
#
#  	@brief This class extends the BinTreeElement class by adding a 'key' value
#  	for use in a binary search tree implementations.
#
#
class BSTElement(BinTreeElement):
    key = object()

    ##
    #
    #  Construct an empty BSTElement with no key assigned and left and
    #  right pointers set to null.
    #  @param key the key to be used in a binary search tree implementation
	#  @param e the object this BSTElement is holding
	#  @param left the BSTElement that should be assigned to the left pointer
	#  @param right the BSTElement that should be assigned to the right pointer
    #
    def __init__(self, key = None, e = None, left = None, right = None, label = None):
        if key is not None:
            self.set_key(key)
        if e is None and left is None and right is None:
            super(BSTElement, self).__init__()
        elif e is None and left is not None and right is not None:
            super(BSTElement, self).__init__(left = left, right = right)
        elif e is not None and label is not None:
            super(BSTElement, self).__init__(label = label, e = e)
        elif e is not None and left is None and right is None:
            super(BSTElement, self).__init__(e = e)
        elif e is not None and left is not None and right is not None:
            super(BSTElement, self).__init__(e = e, left = left, right = right)





    ##
    # 	This method gets the data structure type
    #
    # 	@return  The date structure type as a string
    #
    def get_data_structure_type(self):
        return "BinarySearchTree"


    ##
    # 	Return the key of the BSTElement
    #
    # 	@return the key of this BSTElement
    #
    def get_key(self):
        return self.key

    ##
    #
    # 	Set the key of the BSTElement to key
    #  	@param key the key to set
    #
    def set_key(self, key):
        self.key = key
        #  add this to the element's properties

    ##
    # Return the left child of the  BSTElement
    # @return the left child of this BSTElement
    def get_left(self):
        return super(BSTElement, self).get_left()

    ##
    # Return the right child of the BSTElement
    # @return the right child of this BSTElement
    def get_right(self):
        return super(BSTElement, self).get_right()

