from bridges.map import *

class WorldMap(Map):
    """
    @brief This class provides an API to displaying world maps in BRIDGES

    See the Maps  tutorials for examples of the usage of the US Map API at
    https://bridgesuncc.github.io/tutorials/Map.html

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

    def get_data_structure_representation(self):
        """
        Getter for the data structure's JSON representatoin
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
        
        return "all"

    def __init__(self):
        """
        @brief Constructor: creates an object

        """
