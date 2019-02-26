#!/usr/bin/env python
from bridges.element import *
from bridges.sl_element import *
from bridges.edge import *
import traceback
import sys
import json

##
#
#	@brief The GraphAdjList class can be used to represent adjacency list based
#		graphs in BRIDGES
#
#	The GraphAdjList class can be used to represent adjacency list based  graphs
#	in BRIDGES; it takes 2 generic parameters: (1) K, which is an orderable
#	key value used in accessing vertices (in constant time) using a hashmap. This
#	permits data sets that need to be accessed by keys that are strings, and
#	(2) E, an application defined type, and used in the Edge representation.
#	The class is simply a wrapper  around the Java Hashmap class
#	and, thus, derives all its operations from it.
#	BRIDGES provides methods to visualize the graph  and its contents.
#
#	The vertices of the graph are held in a Java hashmap, for near constant time access;
#	this lets us use strings or integral ids for vertices. The adjacency lists,
#	also a Java hashmap  are built for each vertex and contain the edge (terminating
#	vertex id, weight) in the Edge structure, defined separately. Adjacency lists
#	are singly linked lists using the BRIDGES SLelement.
#
#	Convenience methods are provided to add vertices and edges to the graph as well as
#	retrieve the adjacency list of a vertex, given its id.
#
#
class GraphAdjList():

    QUOTE = "\""
    COMMA = ","
    COLON = ":"
    OPEN_CURLY = "{"
    CLOSE_CURLY = "}"
    OPEN_PAREN = "("
    CLOSE_PAREN = ")"
    OPEN_BOX = "["
    CLOSE_BOX = "]"

    LargeGraphVertSize = 1000;
    ##
    #
    # 	Constructor
    #
    def __init__(self):
        self.vertices = dict()
        self.adj_list = dict()

    ##
    # 	This method gets the data structure type
    #
    # 	@return  The date structure type as a string
    #
    #
    def get_data_structure_type(self):
        if self.LargeGraphVertSize < len(self.vertices):
            return "largegraph"
        return "GraphAdjacencyList"

    ##
    # Adds a new vertex to the graph, initializes the adjacency
    # list; user is responsible for checking if the vertex already
    # exists. This method will replace the value for this key
    #
    #	@param k - vertex id
    #	@param E - vertex info, currently used as a label by default
    #
    def add_vertex(self, k, e):
        #  note: it is the user's responsibility to  check
        #  for duplicate vertices
        self.vertices[k] = Element(val = e)
        self.vertices.get(k).set_label(str(k))
        self.adj_list[k] = None

    ##
    #	Adds a new edge to the graph, adds it to that vertex's
    #	adjacency list; user is responsible for checking if the
    #	vertex already exists. This version assumes a default edge
    # 	weight of 1.
    #
    #	@param src - source vertex of edge
    #	@param dest - destination  vertex of edge
    #
    #
    def add_edge(self, src, dest, weight = None):
        #  check to see if the two vertices exist, else
        #  throw an exception
        try:
            if self.vertices.get(src) is None or self.vertices.get(dest) is None:
                raise ValueError("Vertex " + src + " or " + dest + " does not exist! Add the vertex before creating the edge.")
        except Exception as e:
            traceback.print_tb(e.__traceback__)
        if weight is not None:
            self.adj_list[src] = SLelement(e=Edge(weight, dest), next = self.adj_list.get(src))
        else:
            self.adj_list[src] = SLelement(e=Edge(1, dest), next = self.adj_list.get(src))

    ##
    #	This method returns the graph nodes
    #
    #	return - vertices held in  in the hashmap
    #
    #
    def get_vertices(self):
        return self.vertices

    ##
    #	This is a convenience method to retrieve a vertex given
    #	its key
    #
    #   @param key - The key for the value in vertices dict
    #	@return - graph vertex corresponding to its key
    #
    #
    def get_vertex(self, key):
        return self.vertices.get(key)

    ##
    #	Gets the adjacency list (of type SLelement<Edge> )
    #
    #   @param vertex - The vertex in adj_list
    #	@return - the graph's adjacency lists
    #
    #
    def get_adjacency_list(self, vertex = None):
        if vertex is not None:
            return self.adj_list.get(vertex)
        else:
            return self.adj_list

    ##
    #
    #	 This is a convenience method to simplify access to the link visualizer;
    #	 the method assumes the vertex names point to existing vertices, else an exception
    #	 is thrown
    #
    #   @param src - source vertex of edge
    #   @param dest - destination vertex of edge
    #
    def get_link_visualizer(self, src, dest):
        #  get the source and destination vertex elements
        #  and check to see if they exist
        v1 = self.vertices.get(src)
        v2 = self.vertices.get(dest)
        try:
            if v1 is None or v2 is None:
                raise ValueError("Vertex " + src + " or " + dest + " does not exist! First add the vertices to the graph.")
        except Exception as e:
            traceback.print_tb(e.__traceback__)
        return v1.get_link_visualizer(v2)

    ##
    #
    #	This is a convenience method to simplify access to the element visualizer;
    #	the method assumes the vertex name points to an existing vertice, else an
    #	exception is thrown
    #
    #   @param vertex - The vertex for which visualizer is wanted
    #
    def get_visualizer(self, vertex):
        #  get the source and destination vertex elements
        #  and check to see if they exist
        v = self.vertices.get(vertex)
        try:
            if v is None:
                raise ValueError("Vertex " + vertex + " does not exist! First add the vertices to the graph.")
        except Exception as e:
            traceback.print_tb(e.__traceback__)
        return v.get_visualizer()

    ##
    #	Get the JSON representation of the the data structure
    #
    def get_data_structure_representation(self) -> str:

        # redirect for large graphs
        if len(self.vertices) > self.LargeGraphVertSize:
            return self._get_data_structure_large_graph()

        #  map to reorder the nodes for building JSON
        node_map = dict()

        #  get the list nodes
        nodes = []

        # get the objects and add them to the array
        for elements in self.vertices.items():
            nodes.append(elements[1])

        #  remap  map these nodes to  0...MaxNodes-1
        #  and build the nodes JSON
        nodes_JSON = str()

        k = 0
        while k < len(nodes):
            node_map[nodes[k]] = k
            nodes_JSON += (nodes[k].get_element_representation())# get the element object and represent it
            nodes_JSON += self.COMMA
            k += 1
        #  remove the last comma
        if len(nodes) != 0:
            nodes_JSON = nodes_JSON[:-1]
        #  build the links JSON - traverse the adj. lists
        links_JSON = str()
        for a_list in self.adj_list.items():
            list = a_list[1]
            src_vert = self.vertices.get(a_list[0])
            #  get the source vertex index for the JSON (int)
            while list is not None:
                src_indx = node_map.get(src_vert)
                #  get the destination vertex index for the JSON (int)
                edge = list.get_value()
                dest_vert = self.vertices.get(edge.get_vertex())
                dest_indx = node_map.get(dest_vert)
                #  get link representation
                links_JSON+=(list.get_link_representation(src_vert.get_link_visualizer(dest_vert), str(src_indx), str(dest_indx)))
                links_JSON+=(self.COMMA)
                list = list.get_next()
        #  remove the last comma
        if len(links_JSON) > 0:
            links_JSON = links_JSON[:-1]
        json_str = self.QUOTE + "nodes" + self.QUOTE + self.COLON + self.OPEN_BOX + nodes_JSON.__str__() + self.CLOSE_BOX + self.COMMA + self.QUOTE + "links" + self.QUOTE + self.COLON + self.OPEN_BOX + links_JSON.__str__() + self.CLOSE_BOX + self.CLOSE_CURLY
        return json_str

    def _get_data_structure_large_graph(self) -> str:
        nodes_data = []
        node_map = {}
        for i, (key, element) in enumerate(self.vertices.items()):
            node_map[key] = i
            vis = element.get_visualizer()
            this_node_data = []
            if vis.locationX != Decimal("Infinity") and vis.locationY != Decimal("Infinity"):
                this_node_data.append([vis.locationX, vis.locationY])

            color = vis.color
            this_node_data.append([x for x in color.rgba])
            nodes_data.append(this_node_data)

        links_data = []
        for key, element in self.vertices.items():
            adj_ele = self.adj_list.get(key)
            while adj_ele is not None:
                src = node_map[key]
                dest = node_map[adj_ele.get_value().get_vertex()]
                color = element.get_link_visualizer(self.get_vertex(adj_ele.get_value().get_vertex())).color

                links_data.append([src, dest, [x for x in color.rgba]])
                adj_ele = adj_ele.next

        wrapper = {
            "nodes": nodes_data,
            "links": links_data,
        }
        ret = json.dumps(wrapper)
        ret = ret[1:]
        return ret

