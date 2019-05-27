#!/usr/bin/env python
from bridges.element import *
from bridges.link_visualizer import *

##
# @brief This class is used to represent the edges in a graph and will
# 	appear as links in the BRIDGES graph visualization.
# This object is used in graphs and graph algorithms such as DFS, BFS and shortest
# path algorithms that need to visit graph edges. The adjacency list
# representation uses them as the generic paramter, as SLelement<Edge>
# bridges represents Edges as links between pairs of elements
#
# @author Matthew McQuaigue
#
#
class Edge(object):

    ##
    #
    # Constructors
    # @param wt integer, representing  edge weight
    # @param v the terminating vertex of the edge
    #
    def __init__(self, v1, v2, data, lv):
        self.from_vertex = v1
        self.to_vertex = v2
        self.set_edge_data(data)
        self.link_vis(lv)

    def fromv(self):
        return self.from_vertex

    def tov(self):
        return self.to_vertex

    def set_thickness(self, th):
        self.lvis.set_thickness(th)

    def get_thickness(self):
        return self.lvis.get_thickness()

    def set_color(self, color):
        self.lvis.set_color(color)

    def get_color(self):
        return self.lvis.get_color()

    def link_vis(self, lv):
        self.lvis = LinkVisualizer()


    ##
    # Set Edge data (represented as a string for now)
    #
    # @param string: application data
    #
    def set_edge_data(self, data):
        self.edge_data = data

    ##
    # Get edge data
    #
    # @return the edge data
    #
    def get_edge_data(self):
        return self.edge_data

    ##
    # Returns this edge
    #
    def get_edge(self):
        return self
