import json

##
# @brief the SymbolCollection object is a container object to hold a collection of symbols
#  (rectangles, polygons, circles, labels).
#
# @author Matthew Mcquaigue
#
# @date 2018, 7/23/19
#
# \sa Symbol Collection tutorial, 
#     http://bridgesuncc.github.io/tutorials/Symbol_Collection.html
#
#
class SymbolCollection:

    def __init__(self):
        """
        Constructor for collection of symbols
        """
        self._symbols = dict()
        self._domain = 100.0

    def get_data_structure_type(self):
        """
        Getter for the data structure type
        Returns
            str: the data structure type
        """
        return "SymbolCollection"

    def add_symbol(self, s):
        """
        Add a symbol to the collection
        Args:
             s : symbol to be added
        Returns:
             none 
        """
        self._symbols[s.identifier] = s

    def update_axis_domains(self, s):
        """
        Update the bounding box of the symbol collection
        Args:
             s: input symbol to update dimensions
        Returns:
             none
        """
        dims = s.get_dimensions()

        if abs(dims[0]) > self._domain:
            self._domain = abs(dims[0])
        if abs(dims[1]) > self._domain:
            self._domain = abs(dims[1])

        if abs(dims[2]) > self._domain:
            self._domain = abs(dims[2])
        if abs(dims[3]) > self._domain:
            self._domain = abs(dims[3])

    def get_data_structure_representation(self):
        """
        Getter for the data structure's JSON representatoin
        Returns:
            str: the data structure representation
        """
        symbol_json = []
        for key in self._symbols.keys():
            self.update_axis_domains(self._symbols[key])
            symbol_json.append(self._symbols[key].get_json_representation())

        final_json = {
            "domainX": [str(-self._domain), str(self._domain)],
            "domainY": [str(-self._domain), str(self._domain)],
            "symbols": symbol_json
        }
        return final_json
