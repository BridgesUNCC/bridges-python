import TreeElement
import Connector



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
        self.connector = Connector.Connector(appl_id, username, assignment)
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
        ds_json += nodes_links_str

        self.connector.post("/assignments/" + self.get_assignment(), ds_json)

    def set_assignment(self, assignment):
        if (assignment < 0):
            ValueError("Assignment value must be >= 0")
        elif (self.assignment >= 0):
            self.assignment_part = 0
        self.assignment = assignment

    def get_assignment(self):
        return str(self.assignment) + "." + str(self.assignment_part)

    def setTitle(self, titl):
        self.title = titl; 

    def setDescription(self, descr):
        self.title = descr; 

