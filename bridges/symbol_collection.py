import json


class SymbolCollection:

    def __init__(self):
        self.symbols = dict()
        self.domain = 100.0

    def get_data_structure_type(self):
        return "SymbolCollection"

    def add_symbol(self, s):
        self.symbols[s.get_identifier()] = s

    def update_axis_domains(self, s):
        dims = s.get_dimensions()

        if abs(dims[0]) > self.domain:
            self.domain = abs(dims[0])
        if abs(dims[1]) > self.domain:
            self.domain = abs(dims[1])

        if abs(dims[2]) > self.domain:
            self.domain = abs(dims[2])
        if abs(dims[3]) > self.domain:
            self.domain = abs(dims[3])

    def get_data_structure_representation(self):
        symbol_json = []

        for key in self.symbols.keys():
            self.update_axis_domains(self.symbols[key])
            symbol_json.append(self.symbols[key].get_json_representation())

        symbol_json = json.dumps(symbol_json)
        return "\"""domainX\""":[" + str(-self.domain) + "," + str(self.domain) + "],\"""domainY\""":[" + str(-self.domain) + "," + str(self.domain) + "], " + "\"""symbols\""":" + symbol_json + "}"
