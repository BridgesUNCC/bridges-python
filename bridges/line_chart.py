
##
# @brief Show series of data or functions using a line chart.
#
# Line charts (https://en.wikipedia.org/wiki/Line_chart) are used to
# represent graphically functions such as f(x) = 3*x+1, or data such
# as temperature of a liquid on a stove as time passes. A individual
# function or a set of data is called "series".
#
# A series is represented by two arrays xdata and ydata such that
# there is a point at (xdata[0], ydata[0]), an other at (xdata[1],
# ydata[1]), ... One can add a series by passing the two arrays using
# setDataSeries() or add the arrays individually using setXData() and
# setYData().
#
# The different series have a label associated with them by default
# which can be disabled (see toggleSeriesLabel()).
#
# The data is typically shown with axes that use a linear
# scale. However, the scale can be changed to logarithmic for each
# axis individually (see toggleLogarithmicX() and
# toggleLogarithmic()).
#
# The LineChart can have a title (see getTitle() and setTitle()) and
# a subtitle (see setSubTitle() and getSubTitle()).
#
# @author Erik Saule, Matthew Mcquaigue
#
# @date 7/23/19
#
# \sa Line chart tutorial at 
#
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
        """
        Get the data type
        Returns: 
             name of the data type (used internally)
        """
        return "LineChart"

    @property
    def mosue_track(self) -> bool:
        """
        Is mounse tracking on? 
        Returns:
            bool: mouse tracking flag
        """
        return self._mouse_track

    @mosue_track.setter
    def mosue_track(self, val: bool):
        """
        Set mouse tracking flag
        Args:
           val(bool): mouse tracking flag
        """
        self._mouse_track = val

    @property
    def data_label(self):
        """
        Getter for data label
        Returns:
            bool: data label flag
        """
        return self._data_label

    @data_label.setter
    def data_label(self, val):
        """
        Setter for data label flag
        Args:
            val (bool) : data label flag 
        """
        self._data_label = val

    @property
    def logarithmicx(self):
        """
        use logarithmic scale on X axis?
        Returns:
            bool : logarthmic scale flag 
        """
        return self._logarithmicx

    @logarithmicx.setter
    def logarithmicx(self, val):
        """
        Setter for logarithmic scale on X axis
        Args:
            val (bool) : logarithmic scale flag
        Returns:
            None
        """
        self._logarithmicx = val

    @property
    def logarithmicy(self):
        """
        use logarithmic scale on Y axis?
        Returns:
            bool : logarthmic scale flag 
        """
        return self._logarithmicy

    @logarithmicy.setter
    def logarithmicy(self, val):
        """
        Setter for logarithmic scale on Y axis
        Args:
            val (bool) : logarithmic scale flag
        Returns:
            None
        """
        self._logarithmicy = val

    @property
    def title(self):
        """
        Getter for plot title
        Returns:
            str : plot title
        """
        return self._plot_title

    @title.setter
    def title(self, t):
        """
        Setter for plot title
        Args:
            t (str): plot title
        Returns:
            None
        """
        self._plot_title = t

    @property
    def sub_title(self):
        """
        Getter for plot sub title
        Returns:
            str : plot sub title
        """
        return self._plot_subtitle

    @sub_title.setter
    def sub_title(self, s):
        """
        Setter for plot sub title
        Args:
            s (str): plot sub title
        Returns:
            None
        """
        self._plot_subtitle = s

    @property
    def y_label(self):
        """
        Getter for plot Y label
        Returns:
            str : plot label
        """
        return self._y_label

    @y_label.setter
    def y_label(self, label):
        """
        Setter for plot Y label
        Args:
            label (str): plot label
        Returns:
            None
        """
        self._y_label = label

    @property
    def x_label(self):
        """
        Getter for plot X label
        Returns:
            str : plot label
        """
        return self._x_label

    @x_label.setter
    def x_label(self, label):
        """
        Setter for plot X label
        Args:
            label (str): plot label
        Returns:
            None
        """
        self._x_label = label

    def set_data_series(self, series_name, x_data, y_data):
        """
        Setter for plot data on X and Y axes
        Args:
            x_data (dict):  plot data for x axis
            y_data (dict):  plot data for y axis
        Returns:
            None
        """
        self.set_x_data(series_name, x_data)
        self.set_y_data(series_name, y_data)

    def set_x_data(self, series, x_data):
        """
        Setter for plot data on X axis
        Args:
            x_data (dict):  plot data
        Returns:
            None
        """
        self.xaxis_data[series] = self.convert(x_data)

    def get_x_data(self, series):
        """
        Getter for plot data on X
        Returns:
            dict : plot data
        """
        return self.xaxis_data[series]

    def set_y_data(self, series, y_data):
        """
        Setter for plot data on Y axis
        Args:
            y_data (dict):  plot data
        Returns:
            None
        """
        self.yaxis_data[series] = self.convert(y_data)

    def get_y_data(self, series):
        """
        Getter for plot data on Y
        Returns:
            dict : plot data
        """
        return self.yaxis_data[series]

    def convert(self, x_data):
        """
        """
        arr = []
        for i in range(len(x_data)):
            arr.append(float(x_data[i]))
        return arr

    def get_data_structure_representation(self):
        """
        """
        