

class State:

    def __init__(self, state: str):
        self._state_name = state
        self._stroke_color = 'blue'
        self._counties = []
        self._view_counties = True
        self._stroke_width = 0.5
        self._fill_color = 'blue'


    @property
    def state_name(self):
        return self._state_name

    @state_name.setter
    def state_name(self, value):
        self._state_name = value

    @property
    def stroke_color(self):
        return self._stroke_color

    @stroke_color.setter
    def stroke_color(self, value):
        self._stroke_color = value

    @property
    def counties(self):
        return self._counties

    @counties.setter
    def counties(self, value):
        self._counties = value

    @property
    def view_counties(self):
        return self._view_counties

    @view_counties.setter
    def view_counties(self, value):
        self._view_counties = value

    @property
    def stroke_width(self):
        return self._stroke_width

    @stroke_width.setter
    def stroke_width(self, value):
        self._stroke_width = value

    @property
    def fill_color(self):
        return self._fill_color

    @fill_color.setter
    def fill_color(self, value):
        self._fill_color = value

