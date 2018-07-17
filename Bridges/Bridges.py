from Bridges.TreeElement import *
from Bridges.Connector import *



class Bridges:
    vis_type = ""
    ds_handle = object()
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

    def __init__(self, assignment, username, appl_id):


        self.assignment_part = 0
        self.title = str()
        self.description = str()
        self.set_assignment(assignment)
        self.key = appl_id
        self.connector = Connector(appl_id, username, assignment)
        self.username = username

    def set_data_structure(self, ds):
        try:
            self.ds_handle = ds
            self.vis_type = ds.get_data_structure_type()
        except ValueError:
            print("Exception Thrown: Data structure passed to BRIDGES is null!\n")

    def set_visualize_JSON(self, flag):
        json_flag = flag


    def visualize(self):
        nodes_links = []
        nodes_links_str = ""

        if (self.vis_type == "Tree" or self.vis_type == "BinaryTree" or self.vis_type == "SinglyLinkedList", self.vis_type == "DoublyLinkedList", self.vis_type == "MultiList", self.vis_type == "CircularSinglyLinkedList", self.vis_type == "CircularDoublyLinkedList", self.vis_type == "Array", self.vis_type == "GraphAdjacencyList"):
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

        print(ds_json)

        self.connector.post("/assignments/" + self.get_assignment(), ds_json)

    def set_assignment(self, assignment):
        if (assignment < 0):
            ValueError("Assignment value must be >= 0")
        elif (self.assignment >= 0):
            self.assignment_part = 0
        self.assignment = assignment

    def get_assignment(self):
        return str(self.assignment) + "." + str(self.assignment_part)

<<<<<<< HEAD:Bridges/Bridges.py
    def setTitle(self, title):
        if len(title) > self._MaxTitleSize:
            print(
                "Visualization Title restricted to" + str(self._MaxTitleSize) + " characters." + " truncated title...")
            self.title = title[:self._MaxTitleSize]
        else:
            self.title = title
=======
    def setTitle(self, titl):
        self.title = titl; 

    def setDescription(self, descr):
        self.title = descr; 

>>>>>>> a2021e69f8d3c710f3a94e4d636af03a7216add6:src/Bridges.py
