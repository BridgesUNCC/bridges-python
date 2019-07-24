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
#  \sa http://bridgesuncc.github.io/tutorials/AVL.html
#
#
class AVLTreeElement(BSTElement):

    def __init__(self, *args, **kwargs) -> None:
        """
        AVL Tree constructor
        args:
            key, element
        kwargs:
            key: the search key
            e : the the specific object that the element is holding
        Returns:
            None
        """
        if len(args) != 0:
            if len(args) != 2:
                raise ValueError("Must contain 0 or 2 positional parameters")
            super(AVLTreeElement, self).__init__(key=args[0], e=args[1])

        if 'key' in kwargs and 'e' in kwargs:
            super(AVLTreeElement, self).__init__(key=kwargs['key'], e=kwargs['e'])
        elif 'key' in kwargs:
            super(AVLTreeElement, self).key = kwargs['key']
        elif 'e' in kwargs:
            super(AVLTreeElement, self).__init__(e=kwargs['e'])
        else:
            super(AVLTreeElement, self).__init__()
        self._height = self._bal_factor = 0

    def _get_data_structure_type(self) -> str:
        """
        Get the data structure type
        Returns:
             str: the type of data structure
        """
        return "AVLTree"

    @property
    def key(self) -> str:
        """
        Getter for the search keys
        Returns:
            str: represeting the key
        """
        return super(AVLTreeElement, self).key

    @property
    def height(self) -> int:
        """
        Getter for height of the avl tree at this node
        Returns:
            int: the height of the tree
        """
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        """
        Setter function for the height of the avl tree
        Args:
            (int) value: An integer for the height at this node
        Returns:
            None
        """
        self._height = value

    @property
    def balance_factor(self) -> int:
        """
        Getter for the balance factor  of the tree at this node
        Returns:
            int: representing the balance factor
        """
        return self._bal_factor

    @balance_factor.setter
    def balance_factor(self, value: int) -> None:
        """
        Setter for the balance factor of the tree at this node
        Args:
            (int) value: An integer for the balance factor at this node
        Returns:
            None
        """
        self._bal_factor = value

    @property
    def left(self):
        """
        Getter for the left child of the avl tree
        Returns:
            child
        """
        return super(AVLTreeElement, self).get_child(0)

    @left.setter
    def left(self, value):
		"""
        Setter for the left child of this node
        Args:
            value:  left child to be set
        Returns:
            None
        """
        super(AVLTreeElement, self.__class__).set_child(0, value)

    @property
    def right(self):
        """
        Getter for the right child of the avl tree
        Returns:
            right child of this tree element
        """
        return super(AVLTreeElement, self).get_child(1)

    @right.setter
    def right(self, value):
		"""
        Setter for the right child of this node
        Args:
            value:  right child to be set
        Returns:
            None
		"""
        super(AVLTreeElement, self.__class__).set_child(1, value)
