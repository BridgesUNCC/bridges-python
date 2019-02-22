import math
from bridges.graph_adj_list import *


class OsmEdge:
    """OSM edge, represents edge between OsmVertex points
    """
    @property
    def source(self) -> int:
        """ID of source vertex
        :return: int
        """
        return self._source

    @source.setter
    def source(self, source: int):
        try:
            value = int(source)
        except ValueError:
            raise ValueError("Source must be an int")

        self._source = value

    @source.deleter
    def source(self):
        del self._source

    @property
    def destination(self) -> int:
        """ID of destination vertex
        :return: int
        """
        return self._destination

    @destination.setter
    def destination(self, destination: int):
        try:
            value = int(destination)
        except ValueError:
            raise ValueError("Destination must be an int")

        self._destination = value

    @destination.deleter
    def destination(self):
        del self._destination

    @property
    def distance(self) -> float:
        """Distance between two vertices
        :return: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance: float):
        try:
            value = float(distance)
        except ValueError:
            raise ValueError("Distance must be a float")

        self._distance = value

    @distance.deleter
    def distance(self):
        del self._distance

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


class OsmVertex:
    """OSM vertex, represents vertex using open street map data
    """

    @property
    def latitude(self) -> float:
        """Latitude of vertex
        :return: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float):
        try:
            value = float(latitude)
        except ValueError:
            raise ValueError("latitude must be a float")

        self._latitude = value
        self._to_cartesian_coord()

    @latitude.deleter
    def latitude(self):
        del self._latitude

    @property
    def longitude(self) -> float:
        """Longitude of vertex
        :return: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float):
        try:
            value = float(longitude)
        except ValueError:
            raise ValueError("longitude must be a float")

        self._longitude = value
        self._to_cartesian_coord()

    @longitude.deleter
    def longitude(self):
        del self._longitude

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
    @property
    def vertices(self):
        """List of OsmVertex objects
        :return List[OsmVertex]
        """
        return self._vertices

    @vertices.setter
    def vertices(self, vertices: list):
        if not isinstance(vertices, list):
            raise ValueError("vertices must be a list of OsmVertex objects")
        if not isinstance(vertices[0], OsmVertex):
            raise ValueError("vertices must be a list of OsmVertex objects")

        lat_range = [math.inf, -math.inf]
        lon_range = [math.inf, -math.inf]
        cart_range_x = [math.inf, -math.inf]
        cart_range_y = [math.inf, -math.inf]
        for vertex in vertices:
            lat = vertex.latitude
            lon = vertex.longitude

            if lat_range[0] > lat:
                lat_range[0] = lat

            if lat_range[1] < lat:
                lat_range[1] = lat

            if lon_range[0] > lon:
                lon_range[0] = lon

            if lon_range[1] < lon:
                lon_range[1] = lon

            if cart_range_x[0] > vertex.cartesian_coord[0]:
                cart_range_x[0] = vertex.cartesian_coord[0]

            if cart_range_x[1] < vertex.cartesian_coord[0]:
                cart_range_x[1] = vertex.cartesian_coord[0]

            if cart_range_y[0] > vertex.cartesian_coord[1]:
                cart_range_y[0] = vertex.cartesian_coord[1]

            if cart_range_y[1] < vertex.cartesian_coord[1]:
                cart_range_y[1] = vertex.cartesian_coord[1]

        self.latitude_range = lat_range
        self.longitude_range = lon_range
        self.cartesian_range_x = cart_range_x
        self.cartesian_range_y = cart_range_y
        self._vertices = vertices

    @vertices.deleter
    def vertices(self):
        del self._vertices

    @property
    def edges(self):
        """List of OsmEdge objects
        :return: List[OsmEdge]
        """
        return self._edges

    @edges.setter
    def edges(self, edges: list):
        if not isinstance(edges, list):
            raise ValueError("edges must be a list of OsmVertex objects")
        if not isinstance(edges[0], OsmEdge):
            raise ValueError("edges must be a list of OsmEdge objects")
        self._edges = edges

    @edges.deleter
    def edges(self):
        del self._edges

    def get_graph(self) -> GraphAdjList:
        ret_graph = GraphAdjList()
        for k, vertex in enumerate(self.vertices):
            ret_graph.add_vertex(k, vertex)
            ret_graph.get_vertex(k).get_visualizer().set_location(vertex.cartesian_coord[0], vertex.cartesian_coord[1])
            ret_graph.get_vertex(k).get_visualizer().set_color("green")

        for k, edge in enumerate(self.edges):
            ret_graph.add_edge(edge.source, edge.destination, edge.distance)

        return ret_graph

    def __init__(self):
        self._vertices = []
        self._edges = []
        self.latitude_range = []
        self.longitude_range = []
        self.cartesian_range_x = []
        self.cartesian_range_y = []
        self.name = None
