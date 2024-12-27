from bridges.map import *

class USMap(Map):
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

    
    def get_map_representation(self):
        print("HERE")
        return self._states #this is actually the format expected. We should probably eventually build a proper JSON object rather than serialize whatever happens to be in there.

    def __init__(self,states = []):
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

