from bridges.symbol import *
from bridges.color import *

class SymbolGroup(Symbol):

    def __init__(self):
        super(SymbolGroup, self).__init__()
        self.al = []

    def add_symbol(self, s):
        self.al.append(s)

    def get_shape_type(self):
        return "group"

    def add_all_json(self, symbol_json, parent):
        id = len(symbol_json)

        obj = self.get_json_representation()

        obj['ID'] = id

        if parent is not None:
            obj['parentID'] = parent

        symbol_json.append(obj)

        for i in range(len(self.al)):
            self.al[i].add_all_json(symbol_json, id)