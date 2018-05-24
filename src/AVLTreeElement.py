#!/usr/bin/env python
# package: bridges.base

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
#  @param E he generic parameter object that is part of this element, representing
#      application specific data.
#  @param K is the search key parameter in the AVL tree node; K must be orderable, such
#      as integer, float, string, etc., on which relational operators work.
#
#  @author Kalpathi Subramanian, Mihai Mehedint
#
#  @date 6/22/16, 1/7/17, 5/17/17
#
#  \sa Example tutorial using AVLTreeElement at <br>
#      http://bridgesuncc.github.io/Hello_World_Tutorials/AVL.html
#
#
class AVLTreeElement(BSTElement):
    height = int()
    bal_factor = int()

    ##
    #
    #  Construct an AVLTreeElement with default values
    #
    #
    @overloaded
    def __init__(self):
        super(AVLTreeElement, self).__init__()
        self.height = balFactor = 0

    ##
    #
    #  Construct an AVLTreeElement holding a key value  "k" and an object "e"
    #
    #  @param k the search key
    #  @param e the appl specific object that Element is holding
    #
    #
    @__init__.register(object, K, E)
    def __init___0(self, k, e):
        """ generated source for method __init___0 """
        super(AVLTreeElement, self).__init__(e)
        setKey(k)
        self.height = balFactor = 0

    ##
    #	This method gets the data structure type
    #
    #	@return  The date structure type as a string
    #
    #
    def get_data_struct_type(self):
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
    def set_balanceFactor(self, bf):
        self.bal_factor = bf

    ##
    #
    # This method returns the left child of the tree node
    #
    # @return the left child of this node
    #
    #
    def get_left(self):
        return AVLTreeElement(super(AVLTreeElement, self).getLeft())

    ##
    #
    #  This method returns the right child of tree node
    #
    # @return the right child of this node
    #
    #
    def getRight(self):
        """ generated source for method getRight """
        return AVLTreeElement(super(AVLTreeElement, self).getRight())
