from bridges.bst_element import *


class KDTreeElement(BSTElement):
    """
    @brief The This class can be used to create K-d Tree  elements, derived
    from BSTElement. K-D trees can be thought of as the spatial equivalent
    binary search trees and operate on multiple dimensions (2D and 3D are
    most common). These trees serve as a representation of the underlying
    geometrically defined spaces. Specialized versions of these trees
    include quadtrees and octrees, which subdivide into equal sized quadrants or
    octants at each level, respectively.
    This class extends the BSTElement class by adding a dimension property.
    It also includes a thickness property for displaying the partitioning
    lines generated by the convex decomposition.
    
    @author Kalpathi Subramanian, Matthew McQuaigue
    @date 12/26/18, 7/23/19
    
    \sa Kd Tree tutorial, https://bridgesuncc.github.io/tutorials/KdTree.html
    """
    def __init__(self, **kwargs):
        """
        Constructor for a kdTreeElement with the provided value, label, key, left and right kdTree elements.
        The defaults will be used if not provided
        Args:
            (object) key: The key for the ordering
            val: the data this element will hold
            (str) label: the label to show during visualization
            left: the left kdTree element
            right:  the right kdTree element
            (float) th: thickness of KDTree partition lines
            (int) dim: partition dimension
        Returns:
            None
        """
        if 'val' in kwargs:
            if 'label' in kwargs:
                if 'left' and 'right' in kwargs:
                    super(KDTreeElement, self).__init__(e = kwargs['val'], label = kwargs['label'],
                                                        left = kwargs['left'], right = kwargs['right'])
                else:
                    super(KDTreeElement, self).__init__(e=kwargs['val'], label=kwargs['label'])
            else:
                if 'left' and 'right' in kwargs:
                    super(KDTreeElement, self).__init__(e=kwargs['val'], left=kwargs['left'], right=kwargs['right'])
                else:
                    super(KDTreeElement, self).__init__(e=kwargs['val'])
        else:
            super(KDTreeElement, self).__init__()
        if 'key' in kwargs:
            super(KDTreeElement, self.__class__).key.fset(self, kwargs['key'])
        if 'th' in kwargs:
            self._thickness = kwargs['th']
        else:
            self._thickness = 0.0
        if 'dim' in kwargs:
            self._dimension = kwargs['dim']
        else:
            self._dimension = 0

    def get_data_structure_type(self) -> str:
        """
        Getter for the data structure type
        Returns:
            str: of the the data structure type
        """
        return "KdTree"

    @property
    def dimension(self) -> int:
        """
        Getter for the dimensions of the partition lines
        Returns:
            int: dimension (0, 1, 2, etc)
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dim: int) -> None:
        """
        Setter for the dimension of th partitioning at this tree node
        Args:
            (int) dim: dimension value to set
        Returns:
            None
        """
        self._dimension = dim

    @property
    def thickness(self) -> float:
        """
        Getter for the thickness to the KDTree partitions
        Returns:
            float: the thickness
        """
        return self._thickness

    @thickness.setter
    def thickness(self, th) -> None:
        """
        Setter for the thickness of the KDTree partitions - can be used in the visualization
        Args:
            (float) th: thickness of partitions
        Returns:
            None
        """
        self._thickness = th

    @property
    def left(self):
        """
        Getter for the left child of the tree element
        Returns:
            KdTreeElement: the left child
        """
        return super(KDTreeElement, self).left

    @left.setter
    def left(self, l):
        """
        Set left child
        Args:
            l: left child to set
        Returns:
            None
        """
        self.set_child(0, l)

    @property
    def right(self):
        """
        Getter for the right child of the tree element
        Returns:
            KdTreeElement: the right child
        """
        return super(KDTreeElement, self).right

    @right.setter
    def right(self, r):
        """
        Set right child
        Args:
            r: right child to set
        Returns:
            None
        """
        self.set_child(1, r)

    def get_element_representation(self):
        orig_json_str = super(KDTreeElement, self).get_element_representation()
        kdt_dict = {
            "dimension": str(self.dimension),
            "thickness": str(self.thickness)
        }
        orig_json_str.update(kdt_dict)
        return orig_json_str

