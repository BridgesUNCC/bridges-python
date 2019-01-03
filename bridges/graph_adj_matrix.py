from bridges.element import *
import traceback
##
#
#  @brief The GraphAdjMatrix class can be used to represent adjacency matrix based
#      graphs in BRIDGES
#
#  The GraphAdjMatrix class can be used to represent adjacency matrix based  graphs
#  in BRIDGES; it takes 2 generic parameters: (1) K, which is an orderable
#  key value used in accessing vertices (in constant time) using a hashmap. This
#  permits data sets that need to be accessed by keys that are strings, and
#  (2) E, an application defined type, and used in the Edge representation.
#  The class is simply a wrapper  around the Java Hashmap class
#  and, thus, derives all its operations from it.
#  BRIDGES provides methods to visualize the graph  and its contents.
#
#  The vertices of the graph are held in a Java hashmap, for near constant time access;
#  this lets us use strings or integral ids for vertices. The edges are accessed
#	by a second hashmap from each vertex, again assuring near constant access time.
#  Each edge contains the terminating vertex id and weight, as defined by  the Edge
#	class structure.
#
#  Convenience methods are provided to add vertices and edges to the graph. Edges
#  are retrieved by using the dual hashmap, given the vertex ids of the edge.
#
#  @author Kalpathi Subramanian, Mihai Mehedint
#
#
#  \sa Example tutorial at <p>
#      ?? TO DO
#
#
class GraphAdjMatrix():
    #graph vertices list
    # vertices = dict()

    #holds the adjacency list of edges
    # matrix = dict()

    #holds edge information for graph edges
    # edge_data = dict()

    QUOTE = "\""
    COMMA = ","
    COLON = ":"
    OPEN_CURLY = "{"
    CLOSE_CURLY = "}"
    OPEN_PAREN = "("
    CLOSE_PAREN = ")"
    OPEN_BOX = "["
    CLOSE_BOX = "]"

    ##
    # 	Constructor
    #
    def __init__(self, size = None):
        self.vertices = dict()
        self.matrix = dict()
        self.edge_data = dict()

    ##
    #
    #	This method gets the data structure type
    #
    #	@return  The date structure type as a string
    #
    #
    def get_data_structure_type(self):
        return "GraphAdjacencyMatrix"

    ##
    # 	Adds a new vertex to the graph, initializes the  adjacency
    # 	list; user is responsible for checking if the vertex already
    # 	exists. This method will replace the value for this key
    #
    # 	@param k - vertex key value
    # 	@param 3 - user specified data, part of the vertex data
    #
    #
    def add_vertex(self, k, e):
        #  note: it is the user's responsibility to  check
        #  for duplicate vertices
        self.vertices[k] = Element(val = e)
        self.vertices.get(k).set_label(str(k))

        #  create a hashmap for this vertex
        self.matrix[k] =  dict()
        #  fill up this vertex's row and column elements
        for k, element in self.vertices.items():
            (self.matrix.get(k))[element.get_label()] = 0 #  row
            (self.matrix.get(element.get_label()))[k] =  0 #  col

    ##
    #	Adds a new edge to the graph, adds it to the index corresponding to
    #	the source, destination vertex ids;  this version of the method assumes
    #	an edge weight of 1 (unweighted graph); user is responsible for checking if the
    #	vertices already exist, else an exception is thrown.
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
            (self.matrix.get(src))[dest] = weight
        else:
            (self.matrix.get(src))[dest] =  1


    ##
    #
    #	This method returns the graph nodes
    #
    #	return -- vertices held in an unordered  map
    #
    #
    def get_vertices(self):
        return self.vertices

    ##
    #
    #	Gets the adjacency matrix
    #
    #	@return - the graph's adjacency matrix
    #
    def get_adjacency_matrix(self, key = None):
        if key is None:
            return self.matrix
        else:
            return self.matrix.get(key)

    ##
    #
    #	 This is a convenience method to simplify access to the link visualizer;
    #	 the method assumes the vertex names point to existing vertices, else an exception
    #	 is thrown
    #
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
    # 	Get the JSON representation of the the data structure
    #
    def get_data_structure_representation(self):
        #  map to reorder the nodes for building JSON
        node_map = dict()
        #  get teh list nodes
        nodes = []

        for key, value in self.vertices.items():
            nodes.append(value)

        #  remap  map these nodes to  0...MaxNodes-1
        #  and build the nodes JSON
        nodes_JSON = str()
        k = 0
        while k < len(nodes):
            node_map[nodes[k]] = k
            nodes_JSON+=(nodes[k].get_element_representation())
            nodes_JSON+=(self.COMMA)
            k += 1

        #  remove the last comma
        if len(nodes) != 0:
            nodes_JSON = nodes_JSON[:-1]
        #  build the links JSON - traverse the adj. lists

        links_JSON = str()
        for el_src in self.matrix.items():
            src_vert = self.vertices.get(el_src[0])
            src_indx = node_map.get(src_vert)
            for el_dest in el_src[1].items():
                dest_vert = self.vertices.get(el_dest[0])
                if el_dest[1] > 0:
                    dest_indx = node_map.get(dest_vert)
                    links_JSON+=(src_vert.get_link_representation(src_vert.get_link_visualizer(dest_vert), str(src_indx), str(dest_indx)))
                    links_JSON+=self.COMMA
        #  remove the last comma
        if len(links_JSON) > 0:
            links_JSON = links_JSON[:-1]
        json_str = self.QUOTE + "nodes" + self.QUOTE + self.COLON + self.OPEN_BOX + nodes_JSON.__str__() + self.CLOSE_BOX + self.COMMA + self.QUOTE + "links" + self.QUOTE + self.COLON + self.OPEN_BOX + links_JSON.__str__() + self.CLOSE_BOX + self.CLOSE_CURLY
        return json_str
