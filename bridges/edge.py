from bridges.link_visualizer import *

##
# @brief This class is used to represent the edges in a graph and will
# appear as links in the BRIDGES graph visualization.
# This object is used in graphs and graph algorithms such as DFS, BFS and shortest
# path algorithms that need to visit graph edges. The adjacency list
# representation uses them as the generic paramter, as SLelement<Edge>
# bridges represents Edges as links between pairs of elements
#
# @author Matthew McQuaigue
#
#

class Edge():

    def __init__(self, v1, v2, data = None) -> None:
        """
        Constructor for a edge
        Args:
            v1: first vertex of the edge
            v2: second vertex of the edge
            data: the data the edge will hold
        Returns:
            None
        """
        self._from_vertex = v1
        self._to_vertex = v2
        self._edge_data = data
        self._lvis = LinkVisualizer()

    @property
    def tov(self):
        """
        Getter for the to vertex
        Returns:
            vertex: terminating vertex of edge 
        """
        return self._to_vertex

    @property
    def fromv(self):
        """
        Getter for the from vertex
        Returns:
            vertex : source vertex  of edge
        """
        return self._from_vertex

    @property
    def thickness(self) -> float:
        """
        Getter for the link thickness
        Returns:
             float : link thickness (1.0-10.0 range)
        """
        return self._lvis.thickness

    @thickness.setter
    def thickness(self, th: float) -> None:
        """
        Setter for the thickness of edge
        Args:
            th: thickness to be applied (1.0-10.0 range)
        Returns:
            None
        """
        self._lvis.thickness = th

    @property
    def edge_data(self):
        """
        Getter for edge data
        Returns:
             str : data associated with this edge (generic object)
        """
        return self._edge_data

    @edge_data.setter
    def edge_data(self, data) -> None:
        """
        Setter for edge data
        Args:
            data: data for the edge to hold (generic object)
        Returns:
            None
        """
        self._edge_data = data

    @property
    def color(self):
        """
        Getter for edge color
        Returns:
                color of edge (see link visualizer class for setting options
        """
        return self._lvis.color

    @color.setter
    def color(self, color):
        """
        Setter for edge color
        Args:
            color : color to be set (see link visualizer class for setting options)
        Returns:
            None
        """
        self._lvis.color = color

    def get_edge(self):
        """
        Get this edge object
        Returns:
            self: this edge object
        """
        return self
