from bridges.connector import *
from bridges import ColorGrid
from bridges.us_map import *
import os

import json

class Bridges:
    """
    @brief The bridges class is the main class that provides interfaces to datasets, maintains user and assignment information, and connects to the bridges server.
    
    The bridges class is responsible  for initializing the bridges system, specifying
    parameters (user id, assignment id, title, description, data structure
    type, etc) for the student assignment, generating the data structure representation
    and transmission to the bridges server. In addition, it provides interfaces to
    a number of real-world datasets, that makes it easy to access the data for use
    algorithms/data structure assignments. <br>
    
    Datasets. The datasets that are currently supported through the BRIDGES API
    include USGS Earthquake Data, IMDB Actor/Movie Data (2 versions), Gutenberg Book
    Collection Meta Data, a Video Game Dataset, Shakespeare Dataset, OpenStreetMap and Elevation map data. More information
    is found in the respective methods (below) and at 
    https://bridgesuncc.github.io/datasets.html <p>
    
    A typical bridges program includes creating the bridges object, followed by creation
    of the data structure by the user, assigning visual attributes to elements of the
    data structure, followed by specification of teh data structure type  and the
    call to visualize the data structure (bridges::setDataStructure() and visualize()
    methods).
    
    @author Sean Gallagher, Kalpathi Subramanaian, Mihai Mehedint, David Burlinson, Matthew Mcquaigue, Erik Saule, Jamie Payton
    
    @date 2015, 2016, 2017, 2018, 2019, 2020, 2021
    """

    _MaxTitleSize = 200
    _MaxDescSize = 1000
    _projection_options = {"cartesian", "albersusa", "equirectangular", "window"}
    _debug = False
    
    @property
    def window(self) -> [float]:
        """
        This function returns the current window size.  This only works for graph data types. And the coordinate system need to be set to "window" using set_coord_system_type(), setting this value will set "window" for you.
        Returns:
           return a list of 4 floats [x1, x2, y1, y2]
        """
        return self._window
    
    @window.setter
    def window(self, value: [float]) -> None:
        """
        This function sets the current window size that will rendered by default in the view.  This only works for graph data types. And the coordinate system need to be set to "window" using set_coord_system_type(), setting this value will set "window" for you.
        """
        try:
            new_window = [float(x) for x in value]
        except ValueError:
            raise ValueError("Value for window should be a list of 4 numbers")
        except TypeError:
            raise TypeError("Value for window should be a list of 4 numbers")

        self.set_coord_system_type("window")
        self._window = new_window

    @property
    def debug(self) -> bool:
        return self._debug

    @debug.setter
    def debug(self, value: bool) -> None:
        self._debug = value
        self.connector.debug = value
        
    def __init__(self, assignment:int, username:str=None, appl_id:str=None):
        """
        Bridges constructor
        Args:
            (int) assignment: the number your bridges assignment will have
            (str) username: your bridges username, optional if BRIDGES_USER_NAME in env
            (str) appl_id: your appl authentication key from bridges acc, optional if BRIDGES_API_KEY in env
        Returns:
            None
        """
        username = username if username is not None else os.getenv("BRIDGES_USER_NAME")
        appl_id = appl_id if appl_id is not None else os.getenv("BRIDGES_API_KEY")

        self._assignment_part = 0
        self._assignment = 0
        self._username = str()
        self._key = str()
        self._title = str()
        self._description = str()
        self.set_assignment(assignment)
        self.set_username(username)
        self.set_key(appl_id)

        self.connector = Connector(self.get_key(), self.get_username(), self.get_assignment())
        self._coord_system_type = "cartesian"
        self._json_flag = False
        self._element_label_flag = False
        self._link_label_flag = False
        self._post_url_flag = True
        self._map_overlay = False
        self.map = {}
        self._window = [0.0, 0.0, 0.0, 0.0]
        self.ds_handle = None
        self.vis_type = ""

    def set_data_structure(self, ds):
        """
        Set the data structure type.  This method sets the handle to the current data structure; this can be an array, the head of a linked list, root of a tree structure, a graph Arrays of upto 3 dimensions are suppported. It can be any of the data structures supported by BRIDGES. Polymorphism and type casting is used to determine the actual data structure and extract its representtion.
        Args:
            ds: the data structure to visualize
        Returns:
            None
        Raises:
            ValueError: if it is not a BRIDGES data structure
        """
        try:
            self.ds_handle = ds
            self.vis_type = ds.get_data_structure_type()
        except ValueError:
            print("Exception Thrown: Data structure passed to BRIDGES is null!\n")


    @property
    def element_label_flag(self)->bool:
        return self._element_label_flag

    @element_label_flag.setter
    def element_label_flag(self, flag:bool):
        """
            This method controls if the labels for the elements of the visualization are to be on or off
            Args:
                flag : flag that controls the labels
            Returns:
                None
            """
        self._element_label_flag = flag

    @property
    def link_label_flag(self)->bool:
        return self._link_label_flag

    @link_label_flag.setter
    def link_label_flag(self, flag:bool):
        """
            This method controls if the labels for the links in the visualization are to be on or off
            Args:
                flag : flag that controls the labels
            Returns:
                None
            """
        self._link_label_flag = flag

    def get_json_flag(self)->bool:
        """
        This method returns the json flag, which controls if the json is to be printed
        """
        return self._json_flag

    def set_json_flag(self, flag:bool):
        """
        This method controls if the data structure's JSON representation is printed to the console or not
        Args:
            flag : flag that controls if the JSON of the data structure representation is output to console
        Returns:
            None
        """
        self._json_flag = flag

    def set_map(self, map_info:list):
        """
        This method serializes all the state and county objects in the map_info for sending to the server
        
        See tutorial at https://bridgesuncc.github.io/tutorials/Map.html

        :param map_info: is a list of state objects with their counties
        :return: none
        """
        if isinstance(map_info, Map):
            self.set_map_overlay(map_info.get_overlay())
            self.set_coord_system_type(map_info.get_projection())
        self.map = map_info


    def post_visualization_link(self, flag:bool):
        """
        This method controls (with a flag) if the visualization url is printed to the console or not.
        Args:
            flag : flag that controls if the url to the visualization is output to console
        """
        self._post_url_flag = flag

    def visualize(self) -> None:
        """
        Method for generating the representation of the data structure in the form of JSON and sends the information to the bridges server for generating the visualization
        Returns:
            None
        """
        if isinstance(self.ds_handle, Map):
            self.set_map(self.ds_handle)
        ds_str = ""

        if self.vis_type == "Tree" or self.vis_type == "BinaryTree" or self.vis_type == "AVLTree" or\
                self.vis_type == "SinglyLinkedList" or self.vis_type == "DoublyLinkedList" or \
                self.vis_type == "MultiList" or self.vis_type == "CircularSinglyLinkedList" or \
                self.vis_type == "CircularDoublyLinkedList" or self.vis_type == "Array" or \
                self.vis_type == "GraphAdjacencyList" or self.vis_type == "ColorGrid" or self.vis_type == "GraphAdjacencyMatrix" or \
                self.vis_type == "largegraph" or self.vis_type == "KdTree" or self.vis_type == "SymbolCollection" or \
                self.vis_type == "GameGrid" or self.vis_type == "BinarySearchTree" or self.vis_type == "LineChart" or self.vis_type == "BarChart" or \
                self.vis_type == "Audio" or self.vis_type == "SymbolCollectionV2" or self.vis_type == "Scene":
            ds_str = self.ds_handle.get_data_structure_representation()

        ds_dict = {
            "visual": self.vis_type,
            "title": self._title,
            "description": self._description,
            "coord_system_type": self._coord_system_type,
            "map_overlay": self._map_overlay,
            "element_label_flag": self._element_label_flag,
            "link_label_flag": self._link_label_flag,
            "map": (self.map.get_map_representation() if isinstance(self.map, Map) else self.map),
        }
        if self.window is not None and len(self.window) == 4:
            ds_dict['window'] = self.window

        ds_dict.update(ds_str)

        #adds default for serializing objects
        ds_json = json.dumps(ds_dict, default = lambda x: x.__dict__)
        if self._json_flag or self._debug:
            print(ds_json)

        response = self.connector.post("/assignments/" + self.get_assignment(), ds_json)

        if response == 200 and self._post_url_flag:
            print("\nCheck Your Visualization at the following link:\n\n" +
                  self.get_visualize_url()
                   + "\n\n")

            self._assignment_part = self._assignment_part + 1
    def get_visualize_url(self):
        return self.connector.get_server_url() + "/assignments/" + str(self._assignment) + "/" + self._username

    def set_assignment(self, assignment:int):
        """
        Setter for assignment id (must be positive)
        Args: 
           assignment: assignment number to be set
        Returns:
           None
        """
        force = os.getenv("FORCE_BRIDGES_ASSIGNMENT", "")
        if (force != ""):
            assignment = int(force)
        if assignment < 0:
            ValueError("Assignment value must be >= 0")
        elif self._assignment >= 0:
            self._assignment_part = 0
        self._assignment = assignment

    def get_assignment(self) -> str:
        """
        Getter for the assignment id
        Returns:
            str: representing the full assignment id including subassignment aspect
        """
        if self._assignment_part < 10:
            return str(self._assignment) + ".0" + str(self._assignment_part)
        else:
            return str(self._assignment) + "." + str(self._assignment_part)

    def set_title(self, title:str) -> None:
        """
        Setter for the title of the bridges visualization
        Args:
            (str) title: representing the title
        Returns:
            None
        """
        if len(title) > self._MaxTitleSize:
            print("Visualization Title restricted to" + str(self._MaxTitleSize) + " characters." + " truncated title...")
            self._title = title[:self._MaxTitleSize]
        else:
            self._title = title

    def set_description(self, description:str) -> None:
        """
        Setter for the description of the bridges visualization
        Args:
            (str) description: representing the assignment description
        Returns:
            None
        """
        if len(description) > self._MaxDescSize:
            print("Visualization Description restricted to " + str(self._MaxDescSize) + " Truncating description..")
            self._description = description[0:self._MaxDescSize]
        else:
            self._description = description

    def set_map_overlay(self, flag:bool):
        """
        Setter for if the visualization will have a map overlay
        Args:
            (bool) flag: boolean for if map overlay
        Returns:
            None
        """
        self._map_overlay = flag

    # @property
    # def map(self)->list:
    #     return self._map

    # @map.setter
    # def map(self, new_map:list) ->None:
    #     """
    #     Setter function for the svg map overlay describing which map to use and the information from that map.
    #     Args:
    #         new_map: is a list with the first element describing which map: "us" or "world", and the second element
    #     describing what part of the map: a state name or country name respectively.
    #     Returns:
    #         None
    #     """
    #     self._map = new_map

    def set_coord_system_type(self, coord):
        """
        Setter for the coordinate system type to use in the visualization
        Args:
           coord: coordinate system type (used in map overlays (can be 
           "cartesian", "albersusa", "equirectangular")
        """
        if coord in self._projection_options:
            self._coord_system_type = coord
        else:
            print("Unrecognized coordinate system \'" + coord + "\', defaulting to cartesian. Options:")
            self._coord_system_type = "cartesian"

    def get_color_grid_from_assignment(self, user: str, assignment: int, subassignment: int = 0) -> ColorGrid:
        """
        Reconstruct a ColorGrid from an existing ColorGrid on the bridges server
        Args:
            user(str): the name of the user who uploaded the assignment
            assignment(int): the ID of the assignment to get
            subassignment(int): the ID of the subassignment to get (default 0)
        Returns:
            ColorGrid: the ColorGrid stored in the bridges server
        """
        from bridges.data_src_dependent.data_source import get_color_grid_from_assignment
        return get_color_grid_from_assignment(self.connector.server_url, user, assignment, subassignment)

    def set_username(self, username):
        """
        Setter for username (must be a string)
        Args: 
           username: username to be set
        Returns:
           None
        """
        force = os.getenv("FORCE_BRIDGES_USERNAME", "")
        if (force != ""):
            username = force
        self._username = username.replace(" ", "+")
    
    def get_username(self):
        """
        Getter for the assignment user name (BRIDGES credentials)
        Returns:
            str: user name
        """
        return self._username

    def get_assignment_id(self):
        """
        Getter for the assignment number
        Returns:
            int: assignment number
        """
        return self._assignment


    def set_key(self, apikey):
        """
        Setter for API Key (BRIDGES Credentials)
        Args: 
           apikey: api key to be set
        Returns:
           None
        """
        force = os.getenv("FORCE_BRIDGES_APIKEY", "")
        if (force != ""):
            apikey = force
        self._key = apikey.replace(" ", "+")

    def get_key(self):
        """
        Getter for the API key (BRIDGES credentials)
        Returns:
            str: user's API key
        """
        return self._key

    def set_server_url(self, server_url: str) -> None:
        """
        Sets url for the output of the visualize method
        Args:
            server_url: string, must be one of {live, clone, local, games}
		Returns:
            None
        """
        self.connector.set_server_url(server_url)


