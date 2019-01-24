from bridges.connector import *
from bridges import ColorGrid
import json
##
# 	@brief The bridges class is the main class that provides interfaces to datasets,
#	maintains user and assignment information, and connects to the bridges server.
#
#  	The bridges class is responsible  for initializing the bridges system, specifying
#  	parameters (user id, assignment id, title, description, data structure
# 	type, etc) for the student assignment, generating the data structure representation
# 	and transmission to the bridges server. In addition, it provides interfaces to
# 	a number of real-world datasets, that makes it easy to access the data for use
#  	algorithms/data structure assignments. <br>
#
#   <b>Datasets.</b> The datasets that are currently supported through the BRIDGES API
# 	include USGS Earthquake Data, IMDB Actor/Movie Data (2 versions), Gutenberg Book
# 	Collection Meta Data, a Video Game Dataset and Shakespeare Dataset. More information
# 	is found in the respective methods (below) and at <p>
# 	http://bridgesuncc.github.io/datasets.html <p>
#
# 	A typical bridges program includes creating the bridges object, followed by creation
#   of the data structure by the user, assigning visual attributes to elements of the
# 	data structure, followed by specification of teh data structure type  and the
# 	call to visualize the data structure (bridges::setDataStructure() and visualize()
# 	methods).
#
#  	@author Sean Gallagher, Kalpathi Subramanaian, Mihai Mehedint, David Burlinson.
#
#


class Bridges:
    vis_type = ""
    ds_handle = None
    title = str()
    description = str()
    coord_system_type = "cartesian"
    map_overlay = False
    username = ""
    assignment = int()
    assignment_part = int()
    _MaxTitleSize = 50
    _MaxDescSize = 250
    json_flag = False

    projection_options = {"cartesian", "albersusa", "equirectangular"}

    QUOTE = "\""
    COMMA = ","
    COLON = ":"
    OPEN_CURLY = "{"
    CLOSE_CURLY = "}"
    OPEN_PAREN = "("
    CLOSE_PAREN = ")"
    OPEN_BOX = "["
    CLOSE_BOX = "]"

    ##
    # Initialize bridges (Constructor)
    # @param assignment this is the assignmen id (integer)
    # @param appl_id    this is the appl authentication key(from the bridges account)
    # @param username   this is the username (from the bridges account)
    #
    def __init__(self, assignment, username, appl_id):
        self.assignment_part = 0
        self.title = str()
        self.description = str()
        self.set_assignment(assignment)
        self.key = appl_id
        self.connector = Connector(appl_id, username, assignment)
        self.username = username
        self.coord_system_type = "cartesian"

    ##
    #
    #  	This method sets  the handle to the current data structure; this can
    # 	be an array, the head of a linked list, root of a tree structure, a graph
    # 	Arrays of upto 3 dimensions are suppported. It can be any of the data
    # 	structures supported by BRIDGES. Polymorphism and type casting is used
    # 	to determine the actual data structure and extract its representtion.
    #
    #  @param ds   The data structure to set (any of the subclasses of DataStruct)
    #
    #
    def set_data_structure(self, ds):
        try:
            self.ds_handle = ds
            self.vis_type = ds.get_data_structure_type()
        except ValueError:
            print("Exception Thrown: Data structure passed to BRIDGES is null!\n")

    def set_visualize_JSON(self, flag):
        self.json_flag = flag

    ##
    #
    #  This method generates the representation of the current data structure (JSON)
    #  and sends that to the bridges server for generating a visualization.
    #
    def visualize(self):
        nodes_links_str = ""

        if (self.vis_type == "Tree" or self.vis_type == "BinaryTree" or self.vis_type == "SinglyLinkedList", self.vis_type == "DoublyLinkedList", self.vis_type == "MultiList", self.vis_type == "CircularSinglyLinkedList", self.vis_type == "CircularDoublyLinkedList", self.vis_type == "Array", self.vis_type == "GraphAdjacencyList", self.vis_type == "ColorGrid", self.vis_type == "KDTree", self.vis_type == "SymbolCollection"):
            nodes_links_str = self.ds_handle.get_data_structure_representation()

        ds = {
            "visual": self.vis_type,
            "title": self.title,
            "description": self.description,
            "coord_system_type": self.coord_system_type,
            "map_overlay": self.map_overlay,
        }
        ds_json = json.dumps(ds)[:-1] + ", "

        if self.vis_type == "Array":
            dims = [1,1,1]
            ds_array = self.ds_handle
            num_dims = ds_array.get_num_dimensions()
            ds_array.get_dimensions(dims)
            ds_json += self.QUOTE + "dims" + self.QUOTE + self.COLON + self.OPEN_BOX + str(dims[0]) + self.COMMA + str(dims[1]) + self.COMMA + str(dims[2]) + self.CLOSE_BOX + self.COMMA

            ds_json += nodes_links_str
        else:
            ds_json += nodes_links_str

        if self.json_flag:
            print(ds_json)

        response = self.connector.post("/assignments/" + self.get_assignment(), ds_json)

        if response == 200:
            print(
                "\nCheck Your Visualization at the following link:\n\n" + self.connector.get_server_url() + "/assignments/" + str(self.assignment) + "/" + self.username + "\n\n")

            self.assignment_part = self.assignment_part + 1

    ##
    # 	set the assignment id
    #
    #  @param assignment number
    #
    #
    def set_assignment(self, assignment):
        if assignment < 0:
            ValueError("Assignment value must be >= 0")
        elif self.assignment >= 0:
            self.assignment_part = 0
        self.assignment = assignment

    ##
    # 	Get the assignment id
    #
    #   @return assignment as a string
    #
    #
    def get_assignment(self):
        if self.assignment_part < 10:
            return str(self.assignment) + ".0" + str(self.assignment_part)
        else:
            return str(self.assignment) + "." + str(self.assignment_part)

    ##
    #
    #  @param title title used in the visualization;
    #
    #
    def set_title(self, title):
        if len(title) > self._MaxTitleSize:
            print(
                "Visualization Title restricted to" + str(self._MaxTitleSize) + " characters." + " truncated title...")
            self.title = title[:self._MaxTitleSize]
        else:
            self.title = title

    ##
    #
    #  @param description description to annotate the visualization;
    #
    #
    def set_description(self, description):
        if len(description) > self._MaxDescSize:
            print("Visualization Description restricted to " + str(self._MaxDescSize) + " Truncating description..")
            self.description = description[0:self._MaxDescSize]
        else:
            self.description = description

    def set_map_overlay(self, flag):
        self.map_overlay = flag

    def set_coord_system_type(self, coord):
        if coord in self.projection_options:
            self.coord_system_type = coord
        else:
            print("Unrecognized coordinate system \'" + coord + "\', defaulting to cartesian. Options:")
            self.coord_system_type = "cartesian"

    def get_color_grid_from_assignment(self, user: str, assignment: int, subassignment: int = 0) -> ColorGrid:
        """
        Reconstruct a ColorGrid from an existing ColorGrid on the bridges server

        :param str user: the name of the user who uploaded the assignment
        :param int assignment: the ID of the assignment to get
        :param int subassignment: the ID of the subassignment to get (default 0)
        :return: ColorGrid: the ColorGrid stored in the bridges server
        """
        from bridges.data_src_dependent.data_source import get_color_grid_from_assignment
        return get_color_grid_from_assignment(self.connector.server_url, user, assignment, subassignment)

    def get_username(self):
        return self.username.replace(" ", "+")

    def get_assignment_id(self):
        return self.assignment


