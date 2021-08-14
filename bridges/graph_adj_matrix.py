from bridges.element import *
import traceback

class GraphAdjMatrix():
    """
    @brief The GraphAdjMatrix class can be used to represent adjacency matrix based
    graphs in BRIDGES
    
    The GraphAdjMatrix class can be used to represent adjacency matrix based  graphs
    in BRIDGES; it takes 2 generic parameters: (1) K, which is an orderable
    key value used in accessing vertices (in constant time) using a hashmap. This
    permits data sets that need to be accessed by keys that are strings, and
    (2) E, an application defined type, and used in the Edge representation.
    The class is simply a wrapper  around the Java Hashmap class
    and, thus, derives all its operations from it.
    BRIDGES provides methods to visualize the graph  and its contents.
    
    The vertices of the graph are held in a Java hashmap, for near constant time access;
    this lets us use strings or integral ids for vertices. The edges are accessed
    by a second hashmap from each vertex, again assuring near constant access time.
    Each edge contains the terminating vertex id and weight, as defined by  the Edge
    class structure.
    
    Convenience methods are provided to add vertices and edges to the graph. Edges
    are retrieved by using the dual hashmap, given the vertex ids of the edge.
    
    @author Kalpathi Subramanian, Mihai Mehedint
    
    
    \sa Example tutorial at https://bridgesuncc.github.io/tutorials/Graph_AM.html
    
    """

    ##
    #     Constructor
    #
    def __init__(self):
        self._vertices = dict()
        self._matrix = dict()
        self._edge_data = dict()

    ##
    #
    #    This method gets the data structure type
    #
    #    @return  The date structure type as a string
    #
    #
    def get_data_structure_type(self):
        return "GraphAdjacencyMatrix"

    ##
    #     Adds a new vertex to the graph, initializes the  adjacency
    #     list; user is responsible for checking if the vertex already
    #     exists. This method will replace the value for this key
    #
    #     @param k - vertex key value
    #     @param e - user specified data, part of the vertex data
    #
    #
    def add_vertex(self, k, e):
        #  note: it is the user's responsibility to  check
        #  for duplicate vertices
        self.vertices[k] = Element(val = e)
        self.vertices.get(k).label = str(k)

        #  create a hashmap for this vertex
        self._matrix[k] =  dict()
        #  fill up this vertex's row and column elements
        for k, element in self.vertices.items():
            (self._matrix.get(k))[element.label] = 0 #  row
            (self._matrix.get(element.label))[k] =  0 #  col

    ##
    #    Adds a new edge to the graph, adds it to the index corresponding to
    #    the source, destination vertex ids;  this version of the method assumes
    #    an edge weight of 1 (unweighted graph); user is responsible for checking if the
    #    vertices already exist, else an exception is thrown.
    #
    #    @param src - source vertex of edge
    #    @param dest - destination  vertex of edge
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
            (self._matrix.get(src))[dest] = weight
        else:
            (self._matrix.get(src))[dest] =  1

    @property
    def vertices(self):
        return self._vertices

    def set_vertex_data(self, src, vertex_data):
        try:
            if self.vertices.get(src) is None:
                raise ValueError("Vertex " + src + " does not exist!")
        except Exception as e:
            traceback.print_tb(e.__traceback__)
        self.vertices.get(src).value = vertex_data

    def get_vertex_data(self, src):
        try:
            if self.vertices.get(src) is None:
                raise ValueError("Vertex " + src + " does not exist!")
        except Exception as e:
            traceback.print_tb(e.__traceback__)
        return self.vertices.get(src).value

    def set_edge_data(self, src, dest, data):
        try:
            if self.vertices.get(src) is None or self.vertices.get(dest) is None:
                raise ValueError("Vertex " + src + " or " + dest +
					" does not exist! Add the vertex before creating the edge.")
        except Exception as e:
            traceback.print_tb(e.__traceback__)
        self._edge_data.get(src)[dest] = data

    def get_edge_data(self, src, dest):
        try:
            if self.vertices.get(src) is None or self.vertices.get(dest) is None:
                raise ValueError("Vertex " + src + " or " + dest +
                                 " does not exist! Add the vertex before creating the edge.")
        except Exception as e:
            traceback.print_tb(e.__traceback__)
        return self._edge_data.get(src)[dest]

    ##
    #
    #    Gets the adjacency matrix
    #
    #    @return - the graph's adjacency matrix
    #
    def get_adjacency_matrix(self, key = None):
        if key is None:
            return self._matrix
        else:
            return self._matrix.get(key)

    ##
    #
    #     This is a convenience method to simplify access to the link visualizer;
    #     the method assumes the vertex names point to existing vertices, else an exception
    #     is thrown
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
    #    This is a convenience method to simplify access to the element visualizer;
    #    the method assumes the vertex name points to an existing vertice, else an
    #    exception is thrown
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
        return v.visualizer

    ##
    #     Get the JSON representation of the the data structure
    #
    def get_data_structure_representation(self):
        node_map = dict()
        nodes = []
        nodes_json = []
        for key, value in self.vertices.items():
            nodes.append(value)

        for k in range(0, len(nodes)):
            node_map[nodes[k]] = k
            nodes_json.append(nodes[k].get_element_representation())

        links_json = []
        for el_src in self._matrix.items():
            src_vert = self.vertices.get(el_src[0])
            src_indx = node_map.get(src_vert)

            for el_dest in el_src[1].items():
                dest_vert = self.vertices.get(el_dest[0])
                if el_dest[1] > 0:
                    dest_indx = node_map.get(dest_vert)
                    links_json.append(src_vert.get_link_representation(src_vert.get_link_visualizer(dest_vert),
                                                                       str(src_indx), str(dest_indx)))
        json_str = {
            "nodes": nodes_json,
            "links": links_json
        }

        return json_str
