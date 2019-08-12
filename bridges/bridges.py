from bridges.connector import *
from bridges import ColorGrid
import json
##
#     @brief The bridges class is the main class that provides interfaces to datasets,
#    maintains user and assignment information, and connects to the bridges server.
#
#      The bridges class is responsible  for initializing the bridges system, specifying
#      parameters (user id, assignment id, title, description, data structure
#     type, etc) for the student assignment, generating the data structure representation
#     and transmission to the bridges server. In addition, it provides interfaces to
#     a number of real-world datasets, that makes it easy to access the data for use
#      algorithms/data structure assignments. <br>
#
#   <b>Datasets.</b> The datasets that are currently supported through the BRIDGES API
#     include USGS Earthquake Data, IMDB Actor/Movie Data (2 versions), Gutenberg Book
#     Collection Meta Data, a Video Game Dataset and Shakespeare Dataset. More information
#     is found in the respective methods (below) and at <p>
#     http://bridgesuncc.github.io/datasets.html <p>
#
#     A typical bridges program includes creating the bridges object, followed by creation
#   of the data structure by the user, assigning visual attributes to elements of the
#     data structure, followed by specification of teh data structure type  and the
#     call to visualize the data structure (bridges::setDataStructure() and visualize()
#     methods).
#
#      @author Sean Gallagher, Kalpathi Subramanaian, Mihai Mehedint, David Burlinson, Matthew Mcquaigue
#
#

class Bridges:
    _MaxTitleSize = 50
    _MaxDescSize = 250
    _projection_options = {"cartesian", "albersusa", "equirectangular", "window"}

    @property
    def window(self) -> [float]:
        """
        his function enables specifying the window that will rendered by default in the view.
        This only works for graph data types. And the coordinate system need to be set to "window"
         using set_coord_system_type(), setting this value will set "window" for you.
        :return: list of 4 floats [x1, x2, y1, y2]
        """
        return self._window

    @window.setter
    def window(self, value: [float]) -> None:
        try:
            new_window = [float(x) for x in value]
        except ValueError:
            raise ValueError("Value for window should be a list of 4 numbers")
        except TypeError:
            raise TypeError("Value for window should be a list of 4 numbers")

        self.set_coord_system_type("window")
        self._window = new_window

    def __init__(self, assignment, username, appl_id):
        """
        Bridges constructor
        Args:
            (int) assignment: the number your bridges assignment will have
            (str) username: your bridges username
            (str) appl_id: your appl authentication key from bridges acc
        Returns:
            None
        """
        self._assignment_part = 0
        self._assignment = 0
        self._title = str()
        self._description = str()
        self._set_assignment(assignment)
        self._key = appl_id
        self.connector = Connector(appl_id, username, assignment)
        self._username = username
        self._coord_system_type = "cartesian"
        self._json_flag = False
        self._map_overlay = False
        self._window = [0.0, 0.0, 0.0, 0.0]
        self.ds_handle = None
        self.vis_type = ""

    def set_data_structure(self, ds):
        """
        This method sets the handle to the current data structure; this can
        be an array, the head of a linked list, root of a tree structure, a graph
        Arrays of upto 3 dimensions are suppported. It can be any of the data
        structures supported by BRIDGES. Polymorphism and type casting is used
        to determine the actual data structure and extract its representtion.
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

    def set_visualize_JSON(self, flag):
        self._json_flag = flag

    def visualize(self) -> None:
        """
        Method for generating the representation of the data structure in the form of JSON
        and sends the information to the bridges server for generating the visualization
        Returns:
            None
        """
        nodes_links_str = ""

        if self.vis_type == "Tree" or self.vis_type == "BinaryTree" or self.vis_type == "AVLTree" or\
                self.vis_type == "SinglyLinkedList" or self.vis_type == "DoublyLinkedList" or \
                self.vis_type == "MultiList" or self.vis_type == "CircularSinglyLinkedList" or \
                self.vis_type == "CircularDoublyLinkedList" or self.vis_type == "Array" or \
                self.vis_type == "GraphAdjacencyList" or self.vis_type == "ColorGrid" or self.vis_type == "GraphAdjacencyMatrix" or \
                self.vis_type == "largegraph" or self.vis_type == "KdTree" or self.vis_type == "SymbolCollection" or \
                self.vis_type == "GameGrid" or self.vis_type == "BinarySearchTree" or self.vis_type == "LineChart":
            nodes_links_str = self.ds_handle.get_data_structure_representation()

        ds = {
            "visual": self.vis_type,
            "title": self._title,
            "description": self._description,
            "coord_system_type": self._coord_system_type,
            "map_overlay": self._map_overlay,
        }
        if self.window is not None and len(self.window) == 4:
            ds['window'] = self.window

        ds.update(nodes_links_str)

        ds_json = json.dumps(ds)
        if self._json_flag:
            print(ds_json)

        response = self.connector.post("/assignments/" + self.get_assignment(), ds_json)

        if response == 200:
            print("\nCheck Your Visualization at the following link:\n\n" +
                  self.connector.get_server_url() + "/assignments/" + str(self._assignment) +
                  "/" + self._username + "\n\n")

            self._assignment_part = self._assignment_part + 1


    def _set_assignment(self, assignment):
        """
        Setter for assignment id (must be positive)
        Args: 
           assignment: assignment number to be set
        Returns:
           None
        """
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

    def set_title(self, title) -> None:
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

    def set_description(self, description) -> None:
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

    def set_map_overlay(self, flag):
        """
        Setter for if the visualization will have a map overlay
        Args:
            (bool) flag: boolean for if map overlay
        Returns:
            None
        """
        self._map_overlay = flag

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

    def get_username(self):
        """
        Getter for the assignment user name (BRIDGES credentials)
        Returns:
            str: user name
        """
        return self._username.replace(" ", "+")

    def get_assignment_id(self):
        """
        Getter for the assignment number
        Returns:
            int: assignment number
        """
        return self._assignment

    def get_key(self):
        """
        Getter for the API key (BRIDGES credentials)
        Returns:
            str: user's API key
        """
        return self._key


