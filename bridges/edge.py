#!/usr/bin/env python
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

    def __init__(self, v1, v2, data) -> None:
        """
        Constructor for a edge
        Args:
            v1: first vertex of the edge
            v2: second vertex of the edge
            data: the data the edge will hold
        Returns:
            None
        """
        self.from_vertex = v1
        self.to_vertex = v2
        self.edge_data = data
        self.link_vis()

    @property
    def tov(self):
        """
        Getter for the to vertex
        Returns:
            vertex
        """
        return self.to_vertex

    @property
    def fromv(self):
        """
        Getter for the from vertex
        Returns:
            vertex
        """
        return self.from_vertex

    @property
    def thickness(self) -> float:
        """
        Getter for the link thickness
        Returns:
             float
        """
        return self.lvis.get_thickness()

    @thickness.setter
    def thickness(self, th: float) -> None:
        """
        Setter for the thickness of edge
        Args:
            th: thickness to be applied
        Returns:
            None
        """
        self.lvis.set_thickness(th)

    @property
    def edge_data(self) -> str:
        """
        Getter for edge data
        Returns:
             str
        """
        return self.edge_data

    @edge_data.setter
    def edge_data(self, data: str) -> None:
        """
        Setter for edge data
        Args:
            data: data for the edge to hold represented as a string
        Returns:
            None
        """
        self.edge_data = data

    def set_color(self, color):
        self.lvis.set_color(color)

    def get_color(self):
        return self.lvis.get_color()

    def link_vis(self):
        self.lvis = LinkVisualizer()

    def get_edge(self):
        return self
