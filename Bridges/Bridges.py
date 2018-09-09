from Bridges.Connector import *

##
# 	@brief The Bridges class is the main class that provides interfaces to datasets,
#	maintains user and assignment information, and connects to the Bridges server.
#
#  	The Bridges class is responsible  for initializing the Bridges system, specifying
#  	parameters (user id, assignment id, title, description, data structure
# 	type, etc) for the student assignment, generating the data structure representation
# 	and transmission to the Bridges server. In addition, it provides interfaces to
# 	a number of real-world datasets, that makes it easy to access the data for use
#  	algorithms/data structure assignments. <br>
#
#   <b>Datasets.</b> The datasets that are currently supported through the BRIDGES API
# 	include USGS Earthquake Data, IMDB Actor/Movie Data (2 versions), Gutenberg Book
# 	Collection Meta Data, a Video Game Dataset and Shakespeare Dataset. More information
# 	is found in the respective methods (below) and at <p>
# 	http://bridgesuncc.github.io/datasets.html <p>
#
# 	A typical Bridges program includes creating the Bridges object, followed by creation
#   of the data structure by the user, assigning visual attributes to elements of the
# 	data structure, followed by specification of teh data structure type  and the
# 	call to visualize the data structure (Bridges::setDataStructure() and visualize()
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
    # Initialize Bridges (Constructor)
    # @param assignment this is the assignmen id (integer)
    # @param appl_id    this is the appl authentication key(from the Bridges account)
    # @param username   this is the username (from the Bridges account)
    #
    def __init__(self, assignment, username, appl_id):
        self.assignment_part = 0
        self.title = str()
        self.description = str()
        self.set_assignment(assignment)
        self.key = appl_id
        self.connector = Connector(appl_id, username, assignment)
        self.username = username

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
        json_flag = flag


    ##
	#
	#  This method generates the representation of the current data structure (JSON)
	#  and sends that to the Bridges server for generating a visualization.
	#
    def visualize(self):
        nodes_links = []
        nodes_links_str = ""
        response = ""
        ds_array = None
        ds_json = ""

        if (self.vis_type == "Tree" or self.vis_type == "BinaryTree" or self.vis_type == "SinglyLinkedList", self.vis_type == "DoublyLinkedList", self.vis_type == "MultiList", self.vis_type == "CircularSinglyLinkedList", self.vis_type == "CircularDoublyLinkedList", self.vis_type == "Array", self.vis_type == "GraphAdjacencyList", self.vis_type == "ColorGrid"):
            nodes_links_str = self.ds_handle.get_data_structure_representation()

        ds_json = self.OPEN_CURLY +	self.QUOTE + "visual" + self.QUOTE + self.COLON + self.QUOTE + self.vis_type + self.QUOTE + self.COMMA + self.QUOTE + "title" + self.QUOTE + self.COLON + self.QUOTE + self.title + self.QUOTE + self.COMMA + self.QUOTE + "description" + self.QUOTE + self.COLON + self.QUOTE + self.description + self.QUOTE + self.COMMA + self.QUOTE + "coord_system_type" + self.QUOTE + self.COLON + self.QUOTE + self.coord_system_type + self.QUOTE + self.COMMA + self.QUOTE + "map_overlay" + self.QUOTE + self.COLON + str(self.map_overlay).lower() + self.COMMA
        # ds_json += nodes_links_str

        if(self.vis_type == "Array"):
            dims = [1,1,1]
            ds_array = self.ds_handle
            num_dims = ds_array.get_num_dimensions()
            ds_array.get_dimensions(dims)
            ds_json += self.QUOTE + "dims" + self.QUOTE + self.COLON + self.OPEN_BOX + str(dims[0]) + self.COMMA + str(dims[1]) + self.COMMA + str(dims[2]) + self.CLOSE_BOX + self.COMMA

            ds_json += nodes_links_str
        else:
            ds_json += nodes_links_str

        response = self.connector.post("/assignments/" + self.get_assignment(), ds_json)

        if (response == 200):
            print(
                "\nCheck Your Visualization at the following link:\n\n" + self.connector.get_server_url() + "/assignments/" + str(self.assignment) + "/" + self.username + "\n\n")

            self.assignment_part = self.assignment_part + 1



        # self.connector.post("/assignments/" + self.get_assignment(), ds_json)


    ##
	# 	set the assignment id
	#
	#  @param assignment number
	#
	#
    def set_assignment(self, assignment):
        if (assignment < 0):
            ValueError("Assignment value must be >= 0")
        elif (self.assignment >= 0):
            self.assignment_part = 0
        self.assignment = assignment

    ##
	# 	Get the assignment id
	#
	#   @return assignment as a string
	#
	#
    def get_assignment(self):
        if (self.assignment_part < 10):
            return str(self.assignment) + ".0" + str(self.assignment_part)
        else:
            return str(self.assignment) + "." + str(self.assignment_part)

    ##
	#
	#  @param title title used in the visualization;
	#
	#
    def setTitle(self, title):
        if len(title) > self._MaxTitleSize:
            print(
                "Visualization Title restricted to" + str(self._MaxTitleSize) + " characters." + " truncated title...")
            self.title = title[:self._MaxTitleSize]
        else:
            self.title = title

     ##
	 #
	 #  @param descr description to annotate the visualization;
	 #
	 #
    def setDescription(self, description):
        if len(description) > self._MaxTitleSize:
            print("Visualization Description restricted to " + str(self._MaxTitleSize) + " Truncating description..")
            self.description = description[0:self._MaxTitleSize]
        else:
            self.description = description
