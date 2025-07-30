from bridges.map import *
import json
from bridges.data_src_dependent.country import Country

class WorldMap(Map):
    """
    @brief This class provides an API to building, displaying and
    manipulating  World maps in BRIDGES

    In the current implementation, we can draw a World map  with all 
    country boundaries, or specify a set of countries  and display the 
    country boundaries.
    
    Functions are provided to access each country county and color
    its boundary, its interior using stroke and fill color
    functions. This lets us build map based applications where the 
    fill color can be used to represent different data attributes, such
    as population counts, election statistics or any attribute at the 
    country level. We stop at the country level as each country has its own 
    subdivisions, such as discticts, states, regions, counties, etc.

    See the Maps tutorials for examples of the usage of the World Map API
    at https://bridgesuncc.github.io/tutorials/WorldMap.html
    
    Authors: Kalpathi Subramanian
    Last modified : May 22, 2025
    """
    def get_projection(self):
        return "equirectangular"
	
    def get_overlay(self):
        return True


    def get_data_structure_type(self):
        """
        Getter for the data structure type as a JSON string
        Returns
            str: the data structure type
        """
        return "world_map"

    def get_map_representation(self):
        """
        Getter for the data structure's JSON representation
        Returns:
            str: the data structure representation
        """
        #This is only used to make a dummy data structure for use when
        #the map is passed as a datastructure and not as an overlay
        return {"map_dummy": True}

    def get_map_representation(self):
        """
        @brief gets the JSON representation of the map data

        Uses functions to convert the state and country attributes to objects
        before serialization into a JSON string
        """
        if self._all:
            return ["all"]
        
        country_data = []
        for i in range(0,len(self._countries)):
            #obj = json.dumps({})
            obj = {}
            c = self._countries[i]
            obj["_country_name"] = c.name
            obj["_alpha2"] = c.alpha2_id
            obj["_alpha3"] = c.alpha3_id
            obj["_numeric"] = c.numeric3_id
            obj["_stroke_color"] = c.stroke_color._get_representation()
            obj["_fill_color"] = c.fill_color._get_representation()
            obj["_stroke_width"] = c.stroke_width
            country_data.append(obj) 
 
        country_json = json.dumps(country_data)
        
        return country_data

    def __init__(self, countries = None):
        """
        @brief Constructor: creates an object with the given country data

        @param countries country information for a set of countries
        """
        self._all = True
        if countries is not None:
            self._all = False
        self._countries = countries

    @property
    def countries(self) -> list[Country]:
        '''
        Returns a list of country objects
        '''
        return self._countries

    @countries.setter
    def countries(self, countries: list[Country]):
        '''
        value: a list of country objects
        '''
        if countries is not None:
            self._all = False
        self._countries = countries

