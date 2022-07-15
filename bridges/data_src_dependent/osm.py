import math
from bridges.graph_adj_list import *

class OsmEdge:
    """
    @brief  Class that hold Open Street Map edges
   
    Class that holds Open Street Map edges from https://openstreetmap.org

    This object is generally not created by the user, to see how its 
    created check out bridges::data_src_dependent::data_source::get_osm_data()

    @sa For an example, check out https://bridgesuncc.github.io/tutorials/Data_OSM.html

    @author Erik Saule, Matthew Mcquaigue, Jay Strahler, Kalpathi Subramanian
    @date 2019, 12/28/20
    """
    @property
    def source(self) -> int:
        """
        @brief Get source vertex (int)

        Returns:
            source vertex of edge
        """ 
        return self._source

    
    @source.setter
    def source(self, source: int):
        """
        @brief Set source vertex 
        Args:
            source: source vertex to set
        """
        try:
            value = int(source)
        except ValueError:
            raise ValueError("Source must be an int")

        self._source = value

    @source.deleter
    def source(self):
        """
        @brief delete source vertex
        """
        del self._source

    @property
    def destination(self) -> int:
        """
        @brief Get destination vertex

        Returns: 
            destination vertex of edge
        """
        return self._destination

    @destination.setter
    def destination(self, destination: int):
        """
        @brief Set destination vertex 
        Args:
             destination:  destination vertex to set (int)
        """ 
        try:
            value = int(destination)
        except ValueError:
            raise ValueError("Destination must be an int")

        self._destination = value

    @destination.deleter
    def destination(self):
        """
        @brief delete destination vertex
        """
        del self._destination

    @property
    def distance(self) -> float:
        """
        @brief Get distance between two vertices of the edge (float)
        Returns:
            edge length
        """
        return self._distance

    @distance.setter
    def distance(self, distance: float):
        """
        @brief Set distance between source and destination
        Args:
            distance:  distance to set (float)
        """
        try:
            value = float(distance)
        except ValueError:
            raise ValueError("Distance must be a float")

        self._distance = value

    @distance.deleter
    def distance(self):
        """
        @brief Delete distance between edge vertices
        """
        del self._distance


    def __init__(self, source: int, destination: int, distance: float):
        """
        @brief Constructor
        Args:
            source: source vertex of edge
            destination: destination vertex of edge
            distance: distance between the source and destination vertices
        """
        self._source = 0
        self._destination = 0
        self._distance = 0.0
        self.source = source
        self.destination = destination
        self.distance = distance


class OsmVertex:
    """
    @brief  Class that hold Open Street Map vertices
    
    Class that holds Open Street Map vertices from https://openstreetmap.org

    This object is generally not created by the user, to see how its created check 
    out bridges::data_src_dependent::data_source::get_osm_data()

    @sa For an example, check out https://bridgesuncc.github.io/tutorials/Data_OSM.html
    
    @author Jay Strahler, Matthew Mcquaigue, Erik Saule, Kalpathi Subramanian
    @date 2/14/19, 12/29/20
    """

    @property
    def latitude(self) -> float:
        """
        @brief Get latitude of vertex position

        Returns:
            latitude of vertex
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float):
        """
        @brief Set latitude of vertex position
        Args:
            latitude: vertex latitude to set (float)
        """ 
        try:
            value = float(latitude)
        except ValueError:
            raise ValueError("latitude must be a float")

        self._latitude = value
        self._to_cartesian_coord()

    @latitude.deleter
    def latitude(self):
        """
        @brief Delete latitude of vertex position
        """
        del self._latitude

    @property
    def longitude(self) -> float:
        """
        @brief Get longitude of vertex position

        Returns:
            longitude of vertex
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float):
        """
        @brief Set longitude of vertex position
        Args:
            longitude: vertex latitude to set (float)
        """ 
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
        """
        @brief Delete longitude of vertex position
        """
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



class OsmData:
    """
    @brief  Class that hold Open Street Map Data
    
    Class that holds Open Street Map data, from https://openstreetmap.org

    This object is generally not created by the user, to see how its created check 
    out bridges::data_src_dependent::data_source::get_osm_data()

    @sa For an example, check out https://bridgesuncc.github.io/tutorials/Data_OSM.html
    
    @author Jay Strahler, Matthew Mcquaigue, Erik Saule, Kalpathi Subramanian
    @date 2/16/19, 12/28/20, 1/6/21
    """
    from typing import List
    VertexList = List[OsmVertex]
    EdgeList = List[OsmEdge]

    @property
    def vertices(self) -> List[OsmVertex]:
        """
        @brief get vertices of the dataset (list)
        Returns:
            list of vertices
        """
        return self._vertices

    @vertices.setter
    def vertices(self, vertices: List[OsmVertex]):
        """
        @brief Set vertices of the dataset (VertexList)
        Args:
             vertices: VertexList  to set
        """
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

    @vertices.deleter
    def vertices(self):
        """
        Delete  vertices of the dataset
        """
        del self._vertices

    @property
    def edges(self) -> List[OsmEdge]:
        """
        @brief Get edges  of the dataset (EdgeList)
        Returns:
           edges of the OSM data
        """
        return self._edges

    ##
    #    @brief Set edges of the dataset
    #    @return edges (EdgeList)
    @edges.setter
    def edges(self, edges: EdgeList):
        """
        @brief Set edges  of the dataset
        Args:
           edges: edges to set
        """
        if not isinstance(edges, list):
            raise ValueError("edges must be a list of OsmVertex objects")
        for edge in edges:
            if not isinstance(edge, OsmEdge):
                raise ValueError("edges must be a list of OsmEdge objects")
        self._edges = edges

    @edges.deleter
    def edges(self):
        """
        @brief delete the edges in the dataset
        """
        del self._edges

    def get_graph(self) -> GraphAdjList:
        """
        @brief Construct a graph out of the vertex and edge data of the OSM object. 

        The graph will associate the length
        of the edge to the graph edge. No data is bound to the vertices

        The vertices of the graph will be located at
        the location where given in the data set
        converted to cartesian coordinates
 
        Returns:
            adjacency list based graph
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
        """
        @brief constructor
        """
        self._vertices = []
        self._edges = []
        self.latitude_range = []
        self.longitude_range = []
        self.cartesian_range_x = []
        self.cartesian_range_y = []
        self.name = None
