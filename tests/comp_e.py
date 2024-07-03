

class CompE:

    def get_x(self, v):
        pass

    def get_y(self, v):
        pass

class CompEOSM(CompE):

    def get_x(self, v):
        return v.longitude

    def get_y(self, v):
        return v.latitude
