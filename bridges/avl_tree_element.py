from bridges.bst_element import *
##
#  @brief This class extends the BSTElement class by adding a height and balance factor
#	fields that are useful in AVL trees.
#
#	AVL tree elements include a 'height' and a 'balFactor' value,
#	representing the height and balance factor of the AVL tree at
#  that node, respectively. This is useful in representing
#	AVL trees.
#
#	AVLTree elements contain a visualizer (ElementVisualizer) object for setting visual
#  attributes (color, shape, opacity, size), necessary for displaying them in a
#  web browser.
#
#  AVLTree elements also have a LinkVisualizer object, that is used when they are
#	linked to another element, appropriate for setting link attributes, for instance,
#	between *  the current element and its left or right child
#
#
#  @author Kalpathi Subramanian, Mihai Mehedint
#
#  @date 6/22/16, 1/7/17, 5/17/17
#
#
#
class AVLTreeElement(BSTElement):

    height = int()
    bal_factor = int()

    ##
    #
    # Construct an AVLTreeElement
    # @param k the search key
    # @param e the appl specific object that Element is holding
    #
    def __init__(self, k = None, e = None):
        if k is not None:
            super(AVLTreeElement, self).set_key(k)
        if e is not None:
            super(AVLTreeElement, self).__init__(key = k,e = e)
        else:
            super(AVLTreeElement, self).__init__()
        self.height = balFactor = 0


    ##
    #	This method gets the data structure type
    #
    #	@return  The date structure type as a string
    #
    #
    def get_data_structure_type(self):
        return "AVLTree"

    ##
    #	This method returns the height of the tree at this node
    #
    #	@return  height
    #
    #
    def get_height(self):
        return self.height

    ##
    #  This method sets the height of the tree at this node
    #
    #  @param   height h
    #
    #
    def set_height(self, h):
        self.height = h

    ##
    #	This method returns the balance factor  of the tree at this node
    #
    #   @return  balance factor
    #
    #
    def get_balance_factor(self):
        return self.bal_factor

    ##
    #	This method sets the balance factor of the tree at this node
    #
    #  @param   balance factor  bf
    #
    def set_balance_factor(self, bf):
        self.bal_factor = bf

    ##
    #
    # This method returns the left child of the tree node
    #
    # @return the left child of this node
    #
    #
    def get_left(self):
        return super(AVLTreeElement, self).get_left()

    ##
    #
    #  This method returns the right child of tree node
    #
    # @return the right child of this node
    #
    #
    def get_right(self):
        return super(AVLTreeElement, self).get_right()
