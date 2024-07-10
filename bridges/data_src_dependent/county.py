

class County:

    def __init__(self, id: str, code: str, county: str, state: str):
        self._geoid = id
        self._fips_code = code
        self._county_name = county
        self._state_name = state
        self._stroke_color = 'green'
        self._stroke_width = 0.5
        self._fill_color = 'blue'
        self._hide = False

    @property
    def geoid(self):
        return self._geoid

    @geoid.setter
    def geoid(self, value):
        self._geoid = value

    @property
    def fips_code(self):
        return self._fips_code

    @fips_code.setter
    def fips_code(self, value):
        self._fips_code = value

    @property
    def county_name(self):
        return self._county_name

    @county_name.setter
    def county_name(self, value):
        self._county_name = value

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

    @property
    def hide(self):
        return self._hide

    @hide.setter
    def hide(self, value):
        self._hide = value
