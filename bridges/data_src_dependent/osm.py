import math


class OsmEdge:
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
    def __init__(self):
        self._vertices = []
        self._edges = []
        self._latitude_range = []
        self._longitude_range = []
        self._cartesian_range_x = []
        self._cartesian_range_y = []

