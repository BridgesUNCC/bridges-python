from bridges.link_visualizer import *

class Edge():
    """
    @brief This class is used to represent the edges in a graph and will appear as links in the BRIDGES graph visualization.

    This object is used in graphs and graph algorithms such as DFS, BFS and shortest
    path algorithms that need to visit graph edges. The adjacency list
    representation uses them as the generic paramter, as SLelement<Edge>
    bridges represents Edges as links between pairs of elements

    @author Matthew McQuaigue, Kalpathi Subramanian

    @date 2019, 2020, 2021
    """


    def __init__(self, v1, v2, data=None, label: str = None, color: Color = None, thickness: float = None) -> None:
        """
        @brief Constructor for a edge
        Args:
            v1: first vertex of the edge
            v2: second vertex of the edge
            data: the data the edge will hold
            label: edge label
            color: edge color
            thickness: edge thickness
        """
        self._from_vertex = v1
        self._to_vertex = v2
        self._edge_data = data
        self._lvis = LinkVisualizer()

        if label:
            self.label = label

        if color:
            self.color = color

        if thickness:
            self.thickness = thickness

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
    def destination(self):
        """
        Getter for the to vertex
        Returns:
            vertex: terminating vertex of edge
        """
        return self._to_vertex

    @property
    def source(self):
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

    @property
    def opacity(self):
        """
        Getter for the edge opacity
        Returns:
            opacity : edge opacity
        """
        return self.color.alpha

    @opacity.setter
    def opacity(self, opacity):
        """
        Setter for the edge opacity
        Args:
            opacity : opacity value (0-1.0) to set
        Returns:
            None
        """
        self.color.alpha = opacity

    @property
    def label(self):
        """
        Getter for the edge label
        Returns:
            (string) : edge label
        """
        return self._lvis.label

    @label.setter
    def label(self, l):
        """
        Setter for the edge label
        Args:
            l : lavel value (string) to set
        Returns:
            None
        """
        self._lvis.label = l

    def get_edge(self):
        """
        Get this edge object
        Returns:
            self: this edge object
        """
        return self
