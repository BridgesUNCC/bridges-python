#!/usr/bin/env python
from bridges.tree_element import *
##
# 	@brief This class is extended from the TreeElement class  and can be used to create
#	binary tree element objects.
#
# 	The BinTree element class is the building block for creating binary tree structures.
# 	It contains two children (viz., left, right).
#
#  BinTreeElement contains a visualizer (ElementVisualizer) object for setting visual
#  attributes (color, shape, opacity, size), necessary for displaying them in a
#  web browser.
#
#  Elements also have a LinkVisualizer object, that is used when they are linked to
#  another element, appropriate for setting link attributes, for instance, between
#  the current element and its left or  right child
#
# @author Kalpathi Subramanian, Mihai Mehedint
#
#
#
class BinTreeElement(TreeElement):
    left = object()

    # the left pointer
    right = object()


    ##
    #
    # 	Constructs an empty Binary Tree Element
    # @param e the generic object that TreeElement will hold
    # @param label the label of TreeElement that shows up on the bridges visualization
    # @param left the TreeElement to be assigned to the left pointer of this TreeElement
    # @param right the TreeElement to be assigned to the right pointer of this TreeElement
    #
    def __init__(self, label=None, e=None, left=None, right=None ):
        if label is None and e is None and left is None and right is None:
            super(BinTreeElement, self).__init__()
            super(BinTreeElement, self).add_child(left)
            super(BinTreeElement, self).add_child(right)
        elif e is not None and left is not None and right is not None:
            super(BinTreeElement, self).__init__(e = e)
            super(BinTreeElement, self).add_child(left)
            super(BinTreeElement, self).add_child(right)
        elif e is not None and label is not None and left is None and right is None:
            super(BinTreeElement, self).__init__(label = label, e = e)
            super(BinTreeElement, self).add_child(None)
            super(BinTreeElement, self).add_child(None)
        elif e is not None and label is None and left is None and right is None:
            super(BinTreeElement, self).__init__(e=e)
            super(BinTreeElement, self).add_child(None)
            super(BinTreeElement, self).add_child(None)




    ##
    #
    #	This method gets the data structure type
    #
    #	@return  The date structure type as a string
    #
    #
    def get_data_structure_type(self):
        return "BinaryTree"

    ##
    #
    # This method returns the left tree element pointer
    # @return the left child of this TreeElement
    #
    #
    def get_left(self):
        return super(BinTreeElement, self).get_child(0)

    ##
    #
    # This method sets the left tree element pointer
    # @param left the TreeElement that should be assigned to the left child
    #
    #
    def set_left(self, left):
        super(BinTreeElement, self).set_child(0, left)

    ##
    #
    # This method returns the right tree element pointer
    #
    # @return the right child of this TreeElement
    #
    #
    def get_right(self):
        return super(BinTreeElement, self).get_child(1)

    ##
    #
    # This method sets the right tree element pointer
    #
    # @param right the TreeElement that should be assigned to the right child
    #
    #
    def set_right(self, right):
        super(BinTreeElement, self).set_child(1, right)
