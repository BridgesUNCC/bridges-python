#!/usr/bin/env python
from typing import Any, Union

from bridges.sl_element import *
from bridges.edge import *
import traceback


class GraphAdjList:
    """
    @brief The GraphAdjList class can be used to represent adjacency list based graphs in BRIDGES
    
    The GraphAdjList class can be used to represent adjacency list based  graphs
    in BRIDGES
    
    Convenience methods are provided to add vertices and edges to 
    the graph as well as
    retrieve the adjacency list of a vertex, given its id.
    Convenience method addVertex() is provided to add vertices to
    the graph, and addEdge() is provided to add edges.  Edges are
    retrieved by using the dual hashmap, given the vertex ids of the
    edge. Vertices can be styled directly from the vertex element
    returned by getVertex(), and edges are styled from a LinkVisualizer
    one can access through getLinkVisualizer(). Here is a simple example:
    
    \code{java}
    graph = GraphAdjList()
    graph.add_vertex("a");
    graph.add_vertex("b");
    graph.add_edge("a", "b");
    graph.get_vertex("a").set_shape("square");
    graph.get_link_visualizer("a", "b").set_color("yellow");
    \endcode
    
    Adjacency lists are singly linked lists using the BRIDGES
    SLelement. Iterators are provided for easy traversal of the
    adjacency lists. For instance,
    
    \code{java}
    graph = GraphAdjList()
    for (e : graph.out_going_edge_set_of("a"))
         print("a -> "+e.tov());
    \endcode
        
    Graphs can have their nodes and links affected by visual attributes. Nodes
    can have color, size, opacity and shape and  detailed in the ElementVisualizer
    class. Edges support attributes such as color, thickness and opacity and are
    detailed in the LinkVisualizer class.  Element and link attributes are set
    using the get_visualizer() and get_link_visualizer() methods.  For instance,
    
    \code{java}
    GraphAdjList graph = something();
    graph.add_vertex("baskin");
    graph.add_vertex("robins");
    graph.add_edge("baskin","robins");
    graph.get_visualizer().set_color("cyan");
    graph.get_visualizer().set_shape("square");
    graph.get_link_visualizer("baskin", "robins").set_color("green");
    graph.get_link_visualizer("baskin", "robins").set_opacity("0.5f");
    \endcode
    
    
    @author Matthew Mcquaigue, Kalpathi Subramanian
    @date 2018,  7/23/19, 1/5/21
    
    \sa graph adjacency list tutorial, https://bridgesuncc.github.io/tutorials/Graph.html
    
    There are two visualization engines available for graph. The small
    graph visualization supports all attributes of vertices and edges
    but is prohibitively slow on large graphs. The large graph
    visualization only supports locations (actually they are mandatory)
    and colors, all other attributes are ignored.
    
    BRIDGES picks the rendering engine automatically. But it can be
    forced to pick one used forceLargeVizualization() and
    forceSmallVizualization
    """

    LargeGraphVertSize = 1000
    force_large_viz = False
    force_small_viz = False

    def __init__(self) -> None:
        """
        Constructor for a graph adj list
        Returns:
            None
        """
        self._vertices = dict()
        self.adj_list = dict()

    def get_data_structure_type(self) -> str:
        """
        Getter for the data structure type
        Returns:
            str: representing the type
        """
        if (GraphAdjList.force_large_viz == True or (GraphAdjList.force_small_viz == False and
                                                     self.LargeGraphVertSize < len(self.vertices) and
                                                     self.are_all_vertices_located())):
            return "largegraph"
        return "GraphAdjacencyList"

    def add_vertex(self, id: str,
        label: str = None,
        data: Any = None,
        color: Union[str, Color] = "blue",
        opacity: float = 1.0,
        original: Element = None
       ) -> Element:
       """
       Adds a new vertex to the graph. Initializes the adjacency list; user is responsible for checking if the vertex already exists.  This method will replace the value for this key.  Note: it is the user's responsibility to  check for duplicate vertices
     
       Args:
            id: the vertex id
            label: vertex label
            data:  the vertex data
            color:  color of vertex
            opacity:  opacity of vertex
            original:  an existing Element instance to copy, this will 
                 nullify other arguments
       Returns:
            newly created Vertex
       """
       self.vertices[id] = Element(val=data, color=color, opacity=opacity, original=original)
       self.vertices.get(id).label = str(label) if label is not None else str(id)
       self.adj_list[id] = None

       return self.vertices[id]

    def add_edge(self,
                 src: Union[str, Element],
                 dest: Union[str, Element],
                 label: str = None,
                 data: any = None,
                 color: Union[str, Color] = "blue",
                 thickness: float = 1.0,
                 opacity: float = 1.0
                 ) -> Edge:
        """
        Adds a new edge to the graph. Adds edge to that vertex's adjacency list; user is responsible for checking if the vertex already exists. This version assumes a default edge weight of 1.
        Args:
            src: source vertex of edge
            dest: destination  vertex of edge
            label: label of edge,
            color: color of edge,
            thickness: thickness of edge,
            opacity: opacity of edge,
            data: data the edge will hold
        Returns:
            newly created Edge
        Raises:
            ValueError: if the src and dest vertices do not exist
        """
        source_id = self._resolve_id(src)
        dest_id = self._resolve_id(dest)
        if source_id is None or dest_id is None:
            raise ValueError("Vertex " + src + " or " + dest +
                             " does not exist! Add the vertex before creating the edge.")
        try:
            if self.vertices.get(source_id) is None or self.vertices.get(dest_id) is None:
                raise ValueError("Vertex " + src + " or " + dest +
                                 " does not exist! Add the vertex before creating the edge.")
        except Exception as e:
            traceback.print_tb(e.__traceback__)
        self.adj_list[source_id] = SLelement(e=Edge(source_id, dest_id, data, label=label, color=color,
                                                    thickness=thickness), next=self.adj_list.get(src))

        return self.adj_list[source_id].value

    def set_vertex_data(self, src, vertex_data) -> None:
        """
        Set for the data for a given vertex.
        Args:
            src: the source vertex
            vertex_data: The data for the vertex
        Returns:
            None
        Raises:
             ValueError: if the source vertex doesnt exist
        """
        try:
            if self.vertices[src] is None:
                raise ValueError("Vertex " + src + " does not exist!")
        except Exception as e:
            traceback.print_tb(e.__traceback__)
        self.vertices[src].value = vertex_data

    def get_vertex_data(self, src):
        """
        Get the data stored as part of this vertex.
        Args:
            src: the source vertex
        Returns:
            data stored at this vertex
        """
        try:
            if self.vertices[src] is None:
                raise ValueError("Vertex " + src + " does not exist!")
        except Exception as e:
            traceback.print_tb(e.__traceback__)
        return self.vertices[src].value

    def set_edge_data(self, src, dest, edge_data):
        """
        Set edge specific data for the edge.
        Args:
            src: source vertex of edge
            dest: destination vertex of edge
            edge_data: edge specific data
        """
        try:
            if self.vertices[src] is None or self.vertices[dest] is None:
                raise ValueError("Vertex " + src + " or " + dest + " does not exist!")
        except Exception as e:
            traceback.print_tb(e.__traceback__)
        sle = self.adj_list[src]
        while sle is not None:
            edge_dest = sle.value.tov
            if edge_dest == dest:
                if edge_data is not None:
                    sle.value.set_edge_data(edge_data)
                    return
                else:
                    return sle.value.edge_data
            sle = sle.next
        if sle is None:
            raise ValueError("VEdge from " + src + " to " + dest + "does not exist!")

    @property
    def vertices(self) -> dict:
        """
        Getter for the graph nodes
        Returns:
            dict
        """
        return self._vertices

    def get_vertex(self, key):
        """
        Getter for a specific vertex in the dictionary of vertices.
        Args:
            key: The associated key for the vertex
        Returns:
            vertex: Element or None
        """
        return self.vertices.get(key)

    def get_adjacency_list(self, vertex=None):
        """
        Gets the adjacency list
        Args:
            vertex: input  vertex 
        Returns:
            list : adjacency list of this vertex
        """
        if vertex is not None:
            return self.adj_list.get(vertex)
        else:
            return self.adj_list

    def key_set(self):
        """
        Gets the keys for all the graph vertices
		Returns:
			the keys for the vertices in the graph; used with iterators
		"""
        return self.vertices.keys()

    def value_set(self):
        return self.vertices.values()

    def out_going_edge_set_of(self, v):
        """
        Get the outgoing set of edges from a given vertex
        Args:
           v: the given vertex 
        Returns:
           outgoing edge set (used in iterartors)
        """
        return SLelement.list_helper(start=self.get_adjacency_list(v))

    def get_edge_data(self, src, dest):
        """
        Get edge specific data from this edge.

        Args:
            src: source vertex of edge
            dest: destination vertex of edge
        Returns:
            data stored on this edge
        """
        sle = self.adj_list[src]
        while sle is not None:
            ed = sle.value
            if ed.destination == dest:
                return ed.edge_data
            sle = sle.next

    def get_edge(self, src: Union[str, Element], dest: Union[str, Element]):
        """
        Get the edge given its vertices.

        Args:
            src: source vertex of edge
            dest: destination vertex of edge
        Returns:
            edge corresponding to the source and dest vertices
        """
        source_id = self._resolve_id(src)
        dest_id = self._resolve_id(dest)
        if source_id is None or dest_id is None:
            raise ValueError("Vertex " + src + " or " + dest +
                             " does not exist! Add the vertex before creating the edge.")

        sle = self.adj_list[source_id]
        while sle is not None:
            ed = sle.value
            if ed.destination == dest_id:
                return ed
            sle = sle.next

    def _resolve_id(self, key_or_element: Union[str, Element]) -> Union[str, None]:
        if type(key_or_element) is str:
            return key_or_element
        elif type(key_or_element) is Element:
            return [key for key, value in self.vertices.items() if value == key_or_element].pop()
        else:
            return key_or_element

    def are_all_vertices_located(self):
        """
        Check if all vertices in the graph have a valid location
        Returns:
            a boolean
        """
        for element in self.vertices.items():
            el = element[1]
            elvis = el.visualizer
            if(elvis.location_x == float('inf') or elvis.location_y == float('inf')):
                return False
        return True

    def force_large_visualization(self, f):
        """
        Force the rendering engine to use large graph visualization. This forces the rendering to a more bandwidth efficient at the cost of having less features. The large graph visualization only renders vertices that have specified locations. The only usable attribute for vertices and edges are colors.

        Args:
          f: boolean set to true to force the visualization engine to use large graphs visualization. Setting to false does not prevent large visualization to be used, just does not force it.
        Returns:
          None

        """
        if f:
            GraphAdjList.force_large_viz = True
            GraphAdjList.force_small_viz = False
        else:
            GraphAdjList.force_large_viz = False

    def force_small_visualization(self, f):
        """
        Force the rendering engine to use small graph visualization
        
        The small visualization uses more bandwidth, have more
        features, and support a force directed layout for vertices
        which do not have a specified location.

        Args:
           f: boolean set to true to force the visualization engine to use small graphs visualization. Setting to false does not prevent small visualization to be used, just does not force it.
        Returns:
            None

        """
        if f:
            GraphAdjList.force_small_viz = True
            GraphAdjList.force_large_viz = False
        else:
            GraphAdjList.force_small_viz = False

    def get_link_visualizer(self, src, dest):
        """
        This is a convenience method to simplify access to the link visualizer; the method assumes the vertex names point to existing vertices, else an exception is thrown
       Args:
            src - source vertex of edge
            dest - destination vertex of edge
        """
        #  get the source and destination vertex elements
        #  and check to see if they exist
        return self.get_edge(src, dest)

    def get_visualizer(self, vertex):
        """
        This is a convenience method to simplify access to the element visualizer.
	
        The method assumes the vertex name points to an existing vertex, else an exception is thrown
       Args:
            vertex - The vertex for which visualizer is wanted
       """
        v = self.vertices.get(vertex)
        try:
            if v is None:
                raise ValueError("Vertex " + vertex + " does not exist! First add the vertices to the graph.")
        except Exception as e:
            traceback.print_tb(e.__traceback__)
        return v.visualizer

    def get_data_structure_representation(self) -> dict:
        """
        Get the data structure representation
        Returns:
              dict, a JSON representation of the structure 
        """
        node_map = dict()  # map to reorder the nodes for building JSON
        nodes = []  # get the list nodes
        nodes_JSON = []  # array for list of nodes in json
        links_JSON = []  # array for building the links JSON - traverse the adj. lists

        # redirect for large graphs
        if (GraphAdjList.force_large_viz == True or (GraphAdjList.force_small_viz == False and
                                                     self.LargeGraphVertSize < len(self.vertices) and
                                                     self.are_all_vertices_located())):
            return self.get_data_structure_large_graph()

        # get the objects and add them to the array
        for elements in self.vertices.items():
            nodes.append(elements[1])

        # append all nodes representation to list of nodes
        for i in range(0, len(nodes)):
            node_map[nodes[i]] = i
            nodes_JSON.append(nodes[i].get_element_representation())

        # get all nodes in adj_list
        for a_list in self.adj_list.items():
            links_list = a_list[1]
            src_vert = self.vertices.get(a_list[0])
            #  get the source vertex index for the JSON (int)
            while links_list is not None:
                src_indx = node_map.get(src_vert)
                #  get the destination vertex index for the JSON (int)
                edge = links_list.value
                dest_vert = self.vertices.get(edge.tov)
                dest_indx = node_map.get(dest_vert)
                #  get link representation
                links_JSON.append((links_list.get_link_representation(
                                   edge._lvis,
                                   str(src_indx),
                                   str(dest_indx))))
                links_list = links_list.next
        json_str = {
            "nodes": nodes_JSON,
            "links": links_JSON
        }
        return json_str

    def get_data_structure_large_graph(self) -> dict:
        """
        Gets the JSON of the large graph representation
        Returns:
            the data structure representation 
        """
        nodes = []
        node_map = dict()

        for element in self.vertices.items():
            nodes.append(element[1])

        nodes_json = []
        for k in range(0, len(nodes)):
            nodes_json.append([])
            node_map[nodes[k]] = k
            elvis = nodes[k].visualizer
            loc_str = []
            if elvis.location_x != float('inf') and elvis.location_y != float('inf'):
                loc_str.append(elvis.location_x)
                loc_str.append(elvis.location_y)
                nodes_json[k].append(loc_str)
            color = elvis.color
            nodes_json[k].append([color.red, color.green, color.blue, color.alpha])

        links_json = []
        for a_list in self.adj_list.items():
            list = a_list[1]
            src_vert = self.vertices.get(a_list[0])
            while list is not None:
                link_json=[]
                src_indx = node_map.get(src_vert)
                edge = list.value
                dest_vert = self.vertices.get(edge.tov)
                dest_indx = node_map.get(dest_vert)
                color = edge.color
                link_json.append(src_indx)
                link_json.append(dest_indx)
                link_json.append([color.red, color.green, color.blue, color.alpha])
                links_json.append(link_json)
                list = list.next

        graph_alist_json = {
            "nodes": nodes_json,
            "links": links_json
        }

        return graph_alist_json
