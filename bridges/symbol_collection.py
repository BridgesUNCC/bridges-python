import json

class SymbolCollection:
    """
    @brief the SymbolCollection object is a container object to hold a collection of symbols
    (rectangles, polygons, circles, labels).
    
    @author Matthew Mcquaigue
    
    @date 2018, 7/23/19
    
    \sa Symbol Collection tutorial, 
    https://bridgesuncc.github.io/tutorials/Symbol_Collection.html
    """
    def __init__(self):
        """
        Constructor for collection of symbols
        """
        self._symbols = []
        self._domainxmin = -100
        self._domainxmax = 100
        self._domainymin = -100
        self._domainymax = 100
        self._autoupdateviewport = True

    def setviewport(self, xmin, xmax, ymin, ymax):
        """
        Set the display size.
        Args:
            xmin: min x coordinate
            xmax: max x coordinate
            ymin: min y coordinate
            ymax: max y coordinate
        """
        self._autoupdateviewport = False
        self._domainxmin = xmin
        self._domainxmax = xmax
        self._domainymin = ymin
        self._domainymax = ymax    
        
    def get_data_structure_type(self):
        """
        Getter for the data structure type as a JSON string
        Returns
            str: the data structure type
        """
        return "SymbolCollectionV2"

    def add_symbol(self, s):
        """
        Add a symbol to the collection
        Args:
             s : symbol to be added
        Returns:
             none 
        """
        self._symbols.append(s)

    def update_axis_domains(self, s):
        """
        Update the bounding box of the symbol collection
        Args:
             s: input symbol to update dimensions
        Returns:
             none
        """
        # dims = s.get_dimensions()
        #
        # if dims[0] < self._domainxmin:
        #     self._domainxmin = dims[0]
        # if dims[1] > self._domainxmax:
        #     self._domainxmax = dims[1]
        #
        # if dims[2] < self._domainymin:
        #     self._domainymin = dims[2]
        # if dims[3] > self._domainymax:
        #     self._domainymax = dims[3]
        return

    def get_data_structure_representation(self):
        """
        Getter for the data structure's JSON representatoin
        Returns:
            str: the data structure representation
        """
        symbol_json = []
        for i in range(len(self._symbols)):
            if (self._autoupdateviewport):
                self.update_axis_domains(self._symbols[i])
            self._symbols[i].add_all_json(symbol_json, None)

        final_json = {
            "domainX": [self._domainxmin, self._domainxmax],
            "domainY": [self._domainymin, self._domainymax],
            "symbols": symbol_json
        }
        return final_json
