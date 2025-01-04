from bridges.color import *

class USState:
    """
    @brief Class for USState and its attributes

    Each State object contains its name, stroke color, stroke width, 
    fill color, and a list of counties 
    A tutorial on how to use the these objects is available at:
    https://bridgesuncc.github.io/tutorials/Map.html

    @author Erik Saule, Kalpathi Subramanian
    @date  Last modified Dec 30, 2024
    """

    def __init__(self, state: str):
        """
        @brief Constructor for a specific state

        @param state sets default values for the state
        """
        self._state_name = state
        self._stroke_color = Color('red')
        self._counties = []
        self._view_counties = True
        self._stroke_width = 0.5
        self._fill_color = Color('blue')

    @property
    def state_name(self):
        return self._state_name

    @state_name.setter
    def state_name(self, value):
        self._state_name = value

    @property
    def stroke_color(self):
        return self._stroke_color

    @stroke_color.setter
    def stroke_color(self, value):
        self._stroke_color = value

    @property
    def counties(self):
        return self._counties

    @counties.setter
    def counties(self, value):
        self._counties = value

    @property
    def view_counties(self):
        return self._view_counties

    @view_counties.setter
    def view_counties(self, value):
        self._view_counties = value

    @property
    def stroke_width(self):
        return self._stroke_width

    @stroke_width.setter
    def stroke_width(self, value):
        self._stroke_width = value

    @property
    def fill_color(self):
        return self._fill_color

    @fill_color.setter
    def fill_color(self, value):
        self._fill_color = value

