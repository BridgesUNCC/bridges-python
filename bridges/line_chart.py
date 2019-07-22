


class LineChart:

    def __init__(self):
        self._plot_title = ""
        self._plot_subtitle= ""
        self._y_label = ""
        self._x_label = ""
        self.yaxis_data = dict()
        self.xaxis_data = dict()
        self._mouse_track = False
        self._data_label = True
        self._logarithmicx = False
        self._logarithmicy = False

    def get_data_structure_type(self):
        return "LineChart"

    @property
    def mosue_track(self) -> bool:
        return self._mouse_track

    @mosue_track.setter
    def mosue_track(self, val: bool):
        self._mouse_track = val

    @property
    def data_label(self):
        return self._data_label

    @data_label.setter
    def data_label(self, val):
        self._data_label = val

    @property
    def logarithmicx(self):
        return self._logarithmicx

    @logarithmicx.setter
    def logarithmicx(self, val):
        self._logarithmicx = val

    @property
    def logarithmicy(self):
        return self._logarithmicy

    @logarithmicy.setter
    def logarithmicy(self, val):
        self._logarithmicy = val

    @property
    def title(self):
        return self._plot_title

    @title.setter
    def title(self, t):
        self._plot_title = t

    @property
    def sub_title(self):
        return self._plot_subtitle

    @sub_title.setter
    def sub_title(self, s):
        self._plot_subtitle = s

    @property
    def y_label(self):
        return self._y_label

    @y_label.setter
    def y_label(self, label):
        self._y_label = label

    @property
    def x_label(self):
        return self._x_label

    @x_label.setter
    def x_label(self, label):
        self._x_label = label

    def set_data_series(self, series_name, x_data, y_data):
        self.set_x_data(series_name, x_data)
        self.set_y_data(series_name, y_data)

    def set_x_data(self, series, x_data):
        self.xaxis_data[series] = self.convert(x_data)

    def get_x_data(self, series):
        return self.xaxis_data[series]

    def set_y_data(self, series, y_data):
        self.yaxis_data[series] = self.convert(y_data)

    def get_y_data(self, series):
        return self.yaxis_data[series]

    def convert(self, x_data):
        arr = []
        for i in range(len(x_data)):
            arr.append(float(x_data[i]))
        return arr

    def get_data_structure_representation(self):
        