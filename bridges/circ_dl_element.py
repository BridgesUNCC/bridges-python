from bridges.dl_element import *

class CircDLelement(DLelement):
    """
    @brief This class can be used to instantiate Circular Doubly Linked List Elements.
    
    Structurally they are the same as doubly linked elements
    except that each node constructed with the next and the previous pointers
    points to itself.
    
    User's implementation of the circularly linked list needs to ensure that
    the last node's next pointer points to the first node and the first node's
    previous pointer points to the last node, as the visualization generation
    is dependent on this.
    
    Elements have labels (string) that are displayed on the visualization.
    Elements take an generic object E as a user defined parameter, which can be
    any native type or object.
    
    Elements contain a visualizer (ElementVisualizer) object for setting visual
    attributes (color, shape, opacity, size), necessary for displaying them in a web
    browser.
    
    Elements also have a LinkVisualizer object that is used when they are
    linked to another element, appropriate for setting link attributes, between
    the element and its previous or next nodes.
    
    @author Kalpathi Subramanian, Mathhew McQuaigue
    
    @date   7/17/16, 1/16/17 7/23/19, 2021
    
    Circular doubly linked list tutorial: https://bridgesuncc.github.io/tutorials/CircularDoublyLinkedList.html
    """


    def __init__(self, **kwargs) -> None:
        """
        Constructor for an Circularly Doubly Linked Element
        Args:
            label: THe label for this CircDLelement
            e: the generic element object that this CircDLelement will hold
            next: the next DLelement that should be assigned to the next pointer
            prev: THe previous DLelement that should be assigned to the next pointer
        Returns:
            None
        """
        if 'e' in kwargs:
            if 'next' in kwargs and 'prev' in kwargs:
                if 'label' in kwargs:
                    super(CircDLelement, self).__init__(e=kwargs['e'], label=kwargs['label'],
                                                        next=kwargs['next'], prev=kwargs['prev'])
                else:
                    super(CircDLelement, self).__init__(e=kwargs['e'], next=kwargs['next'],
                                                        prev=kwargs['prev'])
            elif 'label' in kwargs:
                super(CircDLelement, self).__init__(e=kwargs['e'], label = kwargs['label'])
                self.next = self.prev = self
            else:
                super(CircDLelement, self).__init__(e=kwargs['e'])
                self.next = self.prev = self
        else:
            super(CircDLelement, self).__init__()
            self.next = self.prev = self

    def get_data_structure_type(self) -> str:
        """
        Gets the data structure type
        Returns:
            None
        """
        return "CircularDoublyLinkedList"

    @property
    def next(self):
        """
        Getter for the next element of this CircDLelement
        Returns:
            DLelement: the following element
        """
        return super(CircDLelement, self).next

    @next.setter
    def next(self, next) -> None:
        """
        Setter for the next element for this CircDLelement
        Args:
            (DLelement) next: the next element to be set
        Returns:
            None
        """
        DLelement.next.fset(self, next)

    @property
    def prev(self):
        """
        Getter for the prev element of this CircDLelement
        Returns:
            DLelement: the prev element in the list
        """
        return super(CircDLelement, self).prev

    @prev.setter
    def prev(self, prev) -> None:
        """
        Setter for the prev element of this CircDLelement
        Args:
            (DLelement) prev: The prev element to be set
        Returns:
            None
        """
        DLelement.prev.fset(self, prev)

    def iterator(self):
        """
        list iterator to be used with range loops 
        """
        return CircDLelementIterator(self)

    def reverse_iterator(self):
        """
        list reverse iterator to be used with range loops 
        """
        return CircDLelementReverseIterator(self)

class CircDLelementIterator():
    def __init__(self, current):
        self.current = current
        self.first = current
        self.at_start = True

    def has_next(self):
        if ((self.current == self.first) and not self.at_start):
            return False

        return True

    def next(self):
        ret = self.current.value
        self.current = self.current.next
        self.at_start = False
        return ret

class CircDLelementReverseIterator():

    def __init__(self, current):
        self.current = current
        self.first = current
        self.at_start = True

    def has_next(self):

        if ((self.current == self.first) and not self.at_start):
            return False

        return True

    def next(self):
        ret = self.current.value
        self.current = self.current.prev
        self.at_start = False
        return ret

