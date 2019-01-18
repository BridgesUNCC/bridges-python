#!/usr/bin/env python
from bridges.element import *


##
# @brief This class is used to represent the edges in a graph and will
# 	appear as links in the BRIDGES graph visualization.
# This object is used in graphs and graph algorithms such as DFS, BFS and shortest
# path algorithms that need to visit graph edges. The adjacency list
# representation uses them as the generic paramter, as SLelement<Edge>
# bridges represents Edges as links between pairs of elements
#
# @author K.R. Subramanian
#
#
class Edge(object):
    weight = int()
    # vertex = Element()

    #  refers to a terminating vertex
    edge_data = str()

    ##
    #
    # Constructors
    # @param wt integer, representing  edge weight
    # @param v the terminating vertex of the edge
    #
    def __init__(self, wt=None, v=None):
        if wt is not None:
            self.weight = wt
        else:
            self.weight = 0
        if v is not None:
            self.vertex = v
        self.edge_data = ""

    ##
    #
    # Set edge weight to "wt"
    #
    # @param wt  -  graph edge weight
    #
    #
    def set_weight(self, wt):
        self.weight = wt

    ##
    #
    # Get edge weight
    #
    # @return the weight of edge
    #
    #
    def get_weight(self):
        return self.weight

    ##
    #
    # Set terminating Element of the edge
    #
    # @param v the identifier of the terminating Element
    #
    #
    def set_vertex(self, v):
        self.vertex = v

    ##
    #
    # Get identifer of the terminating Element of edge
    #
    # @return the string identifier of the terminating Element
    #
    #
    def get_vertex(self):
        return self.vertex

    ##
    #
    # Set edge to weight  of "wt" and terminating Elememt of "v".
    #
    # @param wt edge weight
    # @param v the identifier of the terminating Element
    #
    #
    def set_edge(self, wt, v):
        self.weight = wt
        self.vertex = v

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
