

class City:
    """
    @brief Class that holds data of a city
    
    A user would not normally create an City object but
    rather obtain one from calling bridges::data_src_dependent::data_source::get_us_cities_data(),
    bridges::data_src_dependent::data_source::get_world_cities_data() (to come)

    A tutorial on how to use the City objects is available at:
    https://bridgesuncc.github.io/tutorials/Data_USCities.html 

    Each city object contains the city name, state, country, time zone, elevation,
    population and lat/long location information.

    @author Kalpathi Subramanian

    @date 6/7/22
    """
    
    def __init__(self, city:str = None, state:str = None, country:str = None, lat:float = None, lon:float = None, elevation:int = None, population:int = None, timezone:str = None):
        self._city = city
        self._state = state
        self._country = country
        self._lat = lat
        self._lon = lon
        self._elevation = elevation
        self._population = population
        self._timezone = timezone


    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    @property
    def country(self):
        return self._city

    @country.setter
    def country(self, country):
        self._country = country

    @property
    def lat(self):
        return self._lat

    @lat.setter
    def lat(self, lat):
        self._lat = lat

    @property
    def lon(self):
        return self._lon

    @lon.setter
    def lon(self, lon):
        self._lon = lon

    @property
    def elevation(self):
        return self._elevation

    @elevation.setter
    def elevation(self, elevation):
        self._elevation = elevation

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, population):
        self._population = population

    @property
    def timezone(self):
        return self._timezone

    @timezone.setter
    def timezone(self, timeone):
        self._timezone = timezone




