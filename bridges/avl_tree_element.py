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
#  @author Kalpathi Subramanian, Mihai Mehedint, Matthew McQuaigue
#
#  @date 6/22/16, 1/7/17, 5/17/17, 6/09/19
#
#
#
class AVLTreeElement(BSTElement):

    def __init__(self, **kwargs) -> None:
        """
        AVL Tree constructor
        kwargs:
            key: the search key
            e : the the specific object that the element is holding
        Returns:
            None
        """
        if 'key' in kwargs and 'e' in kwargs:
            super(AVLTreeElement, self).__init__(key = kwargs['key'], e = kwargs['e'])
        elif 'key' in kwargs:
            super(AVLTreeElement, self).set_key(kwargs['key'])
        elif 'e' in kwargs:
            super(AVLTreeElement, self).__init__(e = kwargs['e'])
        else:
            super(AVLTreeElement, self).__init__()
        self.height = self.balFactor = 0

    def _get_data_structure_type(self) -> str:
        """
        Get the data structure type
        Returns:
             str
        """
        return "AVLTree"

    @property
    def height(self) -> int:
        """
        Getter for height of the avl tree at this node
        Returns:
            int
        """
        return self.height

    @height.setter
    def height(self, value: int) -> None:
        """
        Setter function for the height of the avl tree
        Args:
            value: An integer for the height at this node
        Returns:
            None
        """
        self.height = value

    @height.deleter
    def height(self) -> None:
        """
        Deleter function for the height of the avl tree
        Returns:
             None
        """
        del self.height

    @property
    def bal_factor(self) -> int:
        """
        Getter for the balance factor  of the tree at this node
        Returns:
            int
        """
        return self.bal_factor

    @bal_factor.setter
    def bal_factor(self, value: int) -> None:
        """
        Setter for the balance factor of the tree at this node
        Args:
            value: An integer for the balance factor at this node
        Returns:
            None
        """
        self.bal_factor = value

    @bal_factor.deleter
    def bal_factor(self) -> None:
        """
        Deleter function for the balance factor at this node
        Returns:
             None
        """
        del self.bal_factor

    ##
    #
    # This method returns the left child of the tree node
    #
    # @return the left child of this node
    #
    #
    def get_left(self):
        return super(AVLTreeElement, self).left

    ##
    #
    #  This method returns the right child of tree node
    #
    # @return the right child of this node
    #
    #
    def get_right(self):
        return super(AVLTreeElement, self).get_right()
