#!/usr/bin/env python
from bridges.tree_element import *


class BinTreeElement(TreeElement):
    """
    @brief This class is extended from the TreeElement class  and can be used to create binary tree element objects.
    
    The BinTree element class is the building block for creating binary tree structures.
    It contains two children (viz., left, right).
    
    BinTreeElement contains a visualizer (ElementVisualizer) object for setting visual
    attributes (color, shape, opacity, size), necessary for displaying them in a
    web browser.
    
    Elements also have a LinkVisualizer object, that is used when they are linked to
    another element, appropriate for setting link attributes, for instance, between
    the current element and its left or  right child
    
    @author Kalpathi Subramanian, Mihai Mehedint, Matthew McQuaigue
    
    @date   2018, 7/23/19, 1/6/21
    
    \sa Binary tree tutorial, https://bridgesuncc.github.io/tutorials/BinTree.html
    """

    def __init__(self, **kwargs) -> None:
        """
        Constructor for an empty Binary Tree Element
        kwargs:
            label: The label for the tree element that is displayed in the visualization
            e: the generic object that the binary tree element will hold
            left: the binary tree element assigned to child 0
            right: the binary tree element assigned to child 1
        Returns:
            None
        """
        if 'e' in kwargs:
            if 'e' in kwargs and 'label' in kwargs:
                super(BinTreeElement, self).__init__(label=kwargs['label'], e=kwargs['e'])
            else:
                super(BinTreeElement, self).__init__(e=kwargs['e'])
        else:
            super(BinTreeElement, self).__init__()
        if 'left' in kwargs and 'right' in kwargs:
            super(BinTreeElement, self).add_child(kwargs['left'])
            super(BinTreeElement, self).add_child(kwargs['right'])
        else:
            super(BinTreeElement, self).add_child(None)
            super(BinTreeElement, self).add_child(None)


    def get_data_structure_type(self) -> str:
        """
        Get the data structure type
        Returns:
            str: representing the data structure type
        """
        return "BinaryTree"

    @property
    def left(self):
        """
        Getter for the left element for the binary tree
        Returns:
            TreeElement: left child of this element
        """
        return self.get_child(0)

    @left.setter
    def left(self, l) -> None:
        """
        Setter for the left element of a binary tree
        Args:
            l: the left element to set
        Returns:
            None
        """
        self.set_child(0, l)

    @property
    def right(self):
        """
        Getter for the right element for the binary tree
        Returns:
            TreeElement: the right child of this element
        """
        return self.get_child(1)

    @right.setter
    def right(self, r) -> None:
        """
        Setter for the right element of a binary tree
        Args:
            r: the right element to set
        Returns:
            None
        """
        self.set_child(1, r)
