from bridges.map import *

class USMap(Map):
    """
    @brief This class provides an API to building, displaying and
    manipulating  US maps and counties in BRIDGES

    In the current implementation, we can draw a US map  with all state
    boundaries, a map with all US state and county boundaries, or
    specify a set of states  and display the state and/or county
    boundaries.

    Functions are provided to access each US state or county and color
    its boundary or its interior using the stroke color  and fill color
    functions. This lets us build map based applications where the fill
    fill color can be used to represent different data attributes, such
    population counts, election statistics or any attribute at the state
    or county level.

    See the Maps  tutorials for examples of the usage of the US Map API at
    https://bridgesuncc.github.io/tutorials/Map.html

    """
    def get_projection(self):
        return "albersusa"
	
    def get_overlay(self):
        return True


    def get_data_structure_type(self):
        """
        Getter for the data structure type as a JSON string
        Returns
            str: the data structure type
        """
        return "us_map"

    def get_data_structure_representation(self):
        """
        Getter for the data structure's JSON representatoin
        Returns:
            str: the data structure representation
        """
        #This is only used to make a dummy data structure for use when
        #the map is passed as a datastructure and not as an overlay
        return {"map_dummy": True}

    def _county_to_obj(self, co):
        return {
            "_geoid" : co.geoid,
            "_fips_code" : co.fips_code,
            "_county_name": co.county_name,
            "_state_name": co.state_name,
            "_stroke_color": co.stroke_color._get_representation(),
            "_stroke_width": co.stroke_width,
            "_fill_color": co.fill_color._get_representation(),
            "_hide" : co.hide
            
        }
    
    def _state_to_obj(self, st):
        return {
            "_state_name" : st.state_name,
            "_stroke_color" : st.stroke_color._get_representation(),
            "_stroke_width": st.stroke_width,
            "_fill_color": st.fill_color._get_representation(),
            "_view_counties": st.view_counties,
            "_counties": [self._county_to_obj(st.counties[i]) for i in range(0,len(st.counties)) ]
        }
    
    def get_map_representation(self):
        """
        @brief gets the JSON representation of the map data

        Uses functions to convert the state and country attributes to objects
        before serialization into a JSON string
        """
        data = [ self._state_to_obj(self._states[i]) for i in range(0,len(self._states)) ]
        
        return data

    def __init__(self,states = []):
        """
        @brief Constructor: creates an objecdt with the given state data

        @param states state and county information for a set of states 
        """
        self._states = states

    @property
    def states(self):
        '''
        Returns a list of USState objects
        '''
        return self._states

    @states.setter
    def states(self, value):
        '''
        value: a list of USState objects
        '''
        self._states = value

