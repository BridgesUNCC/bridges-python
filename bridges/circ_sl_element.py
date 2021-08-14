from bridges.sl_element import *

class CircSLelement(SLelement):
    """
    @brief This class can be used to instantiate Singly Linked Circular List Elements.
    
    Structurally they are the same as singly linked elements
    except that each node constructed with the next point pointing to itself;
    User's implementation of the circularly linked list needs to ensure that
    the last node points to first node of the list, as the visualization generation is
    dependent on this.
    
    Elements have labels (string) that are displayed on the visualization.
    Elements take an generic object as a user defined parameter, E, which
    can be any native type or object.
    
    Elements contains a visualizer (ElementVisualizer) object for setting visual
    attributes (color, shape, opacity, size), necessary for displaying them in a web
    browser.
    
    Elements also have a LinkVisualizer object that is used when they are
    linked to another element, appropriate for setting link attributes, between
    an element and its next element.
    
    @author Kalpathi Subramanian, Matthew McQuaigue
    
    @date 6/22/16, 1/7/17, 5/17/17, 7/23/19, 12/29/20
    
    Circular singly linked list tutorial: https://bridgesuncc.github.io/tutorials/CircularSinglyLinkedList.html
    """

    def __init__(self, **kwargs) -> None:
        """
        The constructor for a Circular Singly Linked Element
        Args:
            e: the generic object that this CircSLelement will hold
            label: The label of this CircSLelement
            next: The CircSLelement that should be assigned to the next pointer
        Returns:
            None
        """
        if 'e' in kwargs:
            if 'label' in kwargs:
                if 'next' in kwargs:
                    super(CircSLelement, self).__init__(e=kwargs['e'], label=kwargs['label'],
                                                        next = kwargs['next'])
                else:
                    super(CircSLelement, self).__init__(e=kwargs['e'], label=kwargs['label'])
                    self.next = self
            else:
                super(CircSLelement, self).__init__(e=kwargs['e'])
                self.next = self
        else:
            super(CircSLelement, self).__init__()
            self.next = self

    def get_data_structure_type(self) -> str:
        """
        Gets the data structure type
        Returns:
            str: representing the data structure type
        """
        return "CircularSinglyLinkedList"

    @property
    def next(self):
        """
        Getter for the next element of this CircSLelement
        Returns:
            CircSLelement:  the element that follows this element
        """
        return super(CircSLelement, self).next

    @next.setter
    def next(self, n) -> None:
        """
        Setter for the next element in Circular list
        Args:
            n: the next element to be set
        Returns:
            None:
        """
        SLelement.next.fset(self, n)

    def iterator(self):
        """
        list iterator  for use in range loops
        """
        return CircSlelementIterator(self)

class CircSlelementIterator():

    def __init__(self, current):
        self. current = current
        self. first = current
        self.at_start = True

    def has_next(self):
        if((self.current == self.first) and not self.at_start):
            return False

        return True

    def next(self):
        ret = self.current.value
        self.current = self.current.next
        self.at_start = False
        return ret
