import math
from bridges.graph_adj_list import *

##
#    @brief  Class that hold Open Street Map edges
#    
#    Class that holds Open Street Map edges from https://openstreetmap.org
#    
#    @author Erik Saule, Matthew Mcquaigue, Jay Strahler, Kalpathi Subramanian
#    @date 2019, 12/28/20
#

class OsmEdge:
    ##
    # @brief Get source vertex (int)
    #
    @property
    def source(self) -> int:
        return self._source

    ##
    # @brief Set source vertex 
    # @param source  source vertex to set (int)
    #
    @source.setter
    def source(self, source: int):
        try:
            value = int(source)
        except ValueError:
            raise ValueError("Source must be an int")

        self._source = value

    ##
    # @brief delete source vertex
    #
    @source.deleter
    def source(self):
        del self._source

    ##
    # @brief Get destination vertex
    #
    @property
    def destination(self) -> int:
        return self._destination

    ##
    # @brief Set destination vertex 
    # @param source  destination vertex to set (int)
    #
    @destination.setter
    def destination(self, destination: int):
        try:
            value = int(destination)
        except ValueError:
            raise ValueError("Destination must be an int")

        self._destination = value

    ##
    # @brief Delete destination vertex
    #
    @destination.deleter
    def destination(self):
        del self._destination

    ##
    # @brief Get distance between two vertices of the edge (float)
    #
    @property
    def distance(self) -> float:
        return self._distance

    ##
    # @brief Set distance between source and destination
    # @param distance  distance to set (float)
    #
    @distance.setter
    def distance(self, distance: float):
        try:
            value = float(distance)
        except ValueError:
            raise ValueError("Distance must be a float")

        self._distance = value

    ##
    # @brief Delete distance between edge vertices
    #
    @distance.deleter
    def distance(self):
        del self._distance


    ## @brief Constructor
    #    @param source source vertex of edge
    #    @param destination destination vertex of edge
    #    @param distance distance between the source and destination vertices
    #
    def __init__(self, source: int, destination: int, distance: float):
        """OsmEdge, represents edge between two OsmVertex points
        :param source: int, ID of source vertex
        :param destination: ID of destination vertex
        :param distance: float, distance between the vertices
        """
        self._source = 0
        self._destination = 0
        self._distance = 0.0
        self.source = source
        self.destination = destination
        self.distance = distance


##
#    @brief  Class that hold Open Street Map vertices
#    
#    Class that holds Open Street Map vertices from https://openstreetmap.org
#    
#    @author Jay Strahler, Matthew Mcquaigue, Erik Saule, Kalpathi Subramanian
#    @date 2/14/19, 12/29/20

class OsmVertex:
    ##
    #    @brief Get latitude of vertex position
    #    @return float
    #
    @property
    def latitude(self) -> float:
        return self._latitude

    ##
    #    @brief Set latitude of vertex position
    #    @param latitude latitude to set (float)
    #
    @latitude.setter
    def latitude(self, latitude: float):
        try:
            value = float(latitude)
        except ValueError:
            raise ValueError("latitude must be a float")

        self._latitude = value
        self._to_cartesian_coord()

    ##
    #    @brief Delete latitude of vertex position
    #
    @latitude.deleter
    def latitude(self):
        del self._latitude

    ##
    #    @brief Get longitude of vertex position
    #    @return float
    @property
    def longitude(self) -> float:
        return self._longitude

    ##
    #    @brief Set longitude of vertex position
    #    @param longitude to set (float)
    #
    @longitude.setter
    def longitude(self, longitude: float):
        try:
            value = float(longitude)
        except ValueError:
            raise ValueError("longitude must be a float")

        self._longitude = value
        self._to_cartesian_coord()

    ##
    #    @brief Delete longitude of vertex position
    #
    @longitude.deleter
    def longitude(self):
        del self._longitude

    ## 
    #  @brief convert lat/long to Cartesian coordinates
    #
    def _to_cartesian_coord(self):
        earth_radius = 6378
        lat_rad = self.latitude * math.pi/180
        longit_rad = self.longitude * math.pi/180
        self.cartesian_coord[0] = earth_radius * math.cos(lat_rad) * math.cos(longit_rad)
        self.cartesian_coord[1] = earth_radius * math.cos(lat_rad) * math.sin(longit_rad)

    def __init__(self, latitude: float, longitude: float):
        """OSM vertex, represents vertex using open street map data
        :param latitude: float, latitude of vertex
        :param longitude: float, longitude of vertex
        """
        self._latitude = 0
        self._longitude = 0
        self.cartesian_coord = [0, 0]
        self.latitude = latitude
        self.longitude = longitude
        self._to_cartesian_coord()


##
#    @brief  Class that hold Open Street Map Data
#    
#    Class that holds Open Street Map data, from https://openstreetmap.org
#    
#    @author Jay Strahler, Matthew Mcquaigue, Erik Saule, Kalpathi Subramanian
#    @date 2/16/19, 12/28/20
#    

class OsmData:
    from typing import List
    VertexList = List[OsmVertex]
    EdgeList = List[OsmEdge]

    ##
    #    get vertices of the dataset (list)
    #   @return list of vertices
    #
    @property
    def vertices(self) -> VertexList:
        """List of OsmVertex objects
        :return List[OsmVertex]
        """
        return self._vertices

    ##
    #    Set vertices of the dataset (VertexList)
    #   @param vertices (VertexList) 
    #
    @vertices.setter
    def vertices(self, vertices: VertexList):
        if not isinstance(vertices, list):
            raise ValueError("vertices must be a list of OsmVertex objects")

        lat_range = [math.inf, -math.inf]
        lon_range = [math.inf, -math.inf]
        cart_range_x = [math.inf, -math.inf]
        cart_range_y = [math.inf, -math.inf]
        # find the ranges of lat/lon and cartesian coordinates from new vertices
        for vertex in vertices:
            if not isinstance(vertex, OsmVertex):
                raise ValueError("vertices must be a list of OsmVertex objects")

            lat = vertex.latitude
            lon = vertex.longitude
            cart_x = vertex.cartesian_coord[0]
            cart_y = vertex.cartesian_coord[1]

            lat_range[0] = lat if lat_range[0] > lat else lat_range[0]
            lat_range[1] = lat if lat_range[1] < lat else lat_range[1]

            lon_range[0] = lon if lon_range[0] > lon else lon_range[0]
            lon_range[1] = lon if lon_range[1] < lon else lon_range[1]

            cart_range_x[0] = cart_x if cart_range_x[0] > cart_x else cart_range_x[0]
            cart_range_x[1] = cart_x if cart_range_x[1] < cart_x else cart_range_x[1]

            cart_range_y[0] = cart_y if cart_range_y[0] > cart_y else cart_range_y[0]
            cart_range_y[1] = cart_y if cart_range_y[1] < cart_y else cart_range_y[1]

        self.latitude_range = lat_range
        self.longitude_range = lon_range
        self.cartesian_range_x = cart_range_x
        self.cartesian_range_y = cart_range_y
        self._vertices = vertices

    ##
    #    Delete  vertices of the dataset
    #
    @vertices.deleter
    def vertices(self):
        del self._vertices

    ##
    #    @brief Get edges  of the dataset (EdgeList)
    #    @return edges (EdgeList)
    @property
    def edges(self) -> EdgeList:
        """List of OsmEdge objects
        :return: List[OsmEdge]
        """
        return self._edges

    ##
    #    @brief Set edges of the dataset
    #    @return edges (EdgeList)
    @edges.setter
    def edges(self, edges: EdgeList):
        if not isinstance(edges, list):
            raise ValueError("edges must be a list of OsmVertex objects")
        for edge in edges:
            if not isinstance(edge, OsmEdge):
                raise ValueError("edges must be a list of OsmEdge objects")
        self._edges = edges

    ##
    #    Delete  edges of the dataset
    #
    @edges.deleter
    def edges(self):
        del self._edges

    ##
    #      @brief Construct an adjacency list graph from the data
    #    @return graph (GraphAdjList)
    #
    def get_graph(self) -> GraphAdjList:
        """Construct a graph out of the vertex and edge
        data of the OSM object. The graph will associate the length
        of the edge to the graph edge. No data is bound to the vertices

        The vertices of the graph will be located at
        the location where given in the data set
        converted to cartesian coordinates
        :return: GraphAdjList
        """
        ret_graph = GraphAdjList()
        for k, vertex in enumerate(self.vertices):
            ret_graph.add_vertex(k, data=vertex)
            ret_graph.get_vertex(k).visualizer.set_location(vertex.cartesian_coord[0], vertex.cartesian_coord[1])
            ret_graph.get_vertex(k).visualizer.color = ("green")

        for k, edge in enumerate(self.edges):
            ret_graph.add_edge(edge.source, edge.destination, data=edge.distance)

        return ret_graph

    def __init__(self):
        self._vertices = []
        self._edges = []
        self.latitude_range = []
        self.longitude_range = []
        self.cartesian_range_x = []
        self.cartesian_range_y = []
        self.name = None
