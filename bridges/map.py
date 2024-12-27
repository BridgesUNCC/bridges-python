
class Map:
    '''This is meant to be a base class for all map visualization'''
    '''Likely never instantiated explicitly'''
    def __init__(self):
        pass

    def get_projection(self):
        return None
	
    def get_overlay(self):
        return None

    def get_map_representation(self):
        return None
