from bridges.color import *

class Country:
    """
    @brief This object stores a Country and links to information

    This object is used alongside with the WorldMap object. Each country
    has a stroke color and fill color.

    See tutorial at  https://bridgesuncc.github.io/tutorials/WorldMap.html
    
    @author Kalpathi Subramanian
    @date  Last modified June 7, 2025
    """

    def __init__(self, country: str):
        """
        @brief Constructor for a specific state

        @param state sets default values for the state
        """
        self._name = country
        self._alpha2_id = ""
        self._alpha3_id = ""
        self._numeric3_id = 0
        self._stroke_width = 1.
        self._stroke_color = Color('green')
        self._fill_color = Color('lightblue')

    def __init__(self, name: str, alpha2: str, alpha3: str, numeric3: int):
        """
        @brief Constructor for a specific state

        @param sets provided values for the country
        """
        self._name = name
        self._alpha2_id = alpha2 
        self._alpha3_id =  alpha3
        self._numeric3_id = numeric3
        self._stroke_width = 1.
        self._stroke_color = Color('green')
        self._fill_color = Color('lightblue')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

    @property
    def alpha2_id(self):
        return self._alpha2_id

    @alpha2_id.setter
    def alpha2_id(self, id):
        self._alpha2_id = id 

    @property
    def alpha3_id(self):
        return self._alpha3_id

    @alpha3_id.setter
    def alpha3_id(self, id):
        self._alpha3_id = id 

    @property
    def numeric3_id(self):
        return self._numeric3_id

    @numeric3_id.setter
    def numeric3_id(self, id):
        self._numeric3_id = id 

    @property
    def stroke_color(self):
        return self._stroke_color

    @stroke_color.setter
    def stroke_color(self, value):
        self._stroke_color = value

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

