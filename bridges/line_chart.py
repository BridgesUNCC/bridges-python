

class LineChart:
    """
    @brief Show series of data or functions using a line chart.
    
    Line charts (https://en.wikipedia.org/wiki/Line_chart) are used to
    represent graphically functions such as f(x) = 3*x+1, or data such
    as temperature of a liquid on a stove as time passes. A individual
    function or a set of data is called "series".
    
    A series is represented by two arrays xdata and ydata such that
    there is a point at (xdata[0], ydata[0]), an other at (xdata[1],
    ydata[1]), ... One can add a series by passing the two arrays using
    setDataSeries() or add the arrays individually using setXData() and
    setYData().
    
    The different series have a label associated with them by default
    which can be disabled (see toggleSeriesLabel()).
    
    The data is typically shown with axes that use a linear
    scale. However, the scale can be changed to logarithmic for each
    axis individually (see toggleLogarithmicX() and
    toggleLogarithmic()).
    
    The LineChart can have a title (see getTitle() and setTitle()) and
    a subtitle (see setSubTitle() and getSubTitle()).
    
    @author Erik Saule, Matthew Mcquaigue
    
    @date 7/23/19
    """

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
    def mouse_track(self) -> bool:
        """
        Is mounse tracking on? 
        Returns:
            bool: mouse tracking flag
        """
        return self._mouse_track

    @mouse_track.setter
    def mouse_track(self, val: bool):
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
            series_name: title for the series
            x_data:  plot data for x axis
            y_data:  plot data for y axis
        Returns:
            None
        """
        self.set_x_data(series_name, x_data)
        self.set_y_data(series_name, y_data)

    def set_x_data(self, series, x_data):
        """
        Setter for plot data on X axis
        Args:
            series: the name of the series
            x_data:  plot data
        Returns:
            None
        """
        self.xaxis_data[series] = x_data

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
            series:  series name
            y_data:  plot data
        """
        self.yaxis_data[series] = y_data

    def get_y_data(self, series):
        """
        Getter for plot data on Y
        Returns:
            dict : plot data
        """
        return self.yaxis_data[series]

    def convert(self, x_data):
        """
        Convert input data into an array of floats.
        Args:
            x_data : input data in a list of values
        Returns:
            A list of floats of the same data
        """
        arr = []
        for i in range(len(x_data)):
            arr.append(float(x_data[i]))
        return arr

    def check(self) -> bool:
        correct = True
        for key, value in self.xaxis_data.items():
            series = key
            xdata = value
            ydata = self.yaxis_data.get(series)
            if ydata is None:
                print("Series \"" + series + "\" has xdata but no ydata")
                correct = False
            if len(xdata) != len(ydata):
                print("Series \"" + series + "\" has xdata and ydata of different sizes")
                correct = False
            if self.logarithmicx:
                for i in range(0, len(xdata)):
                    if xdata[i] <= 0:
                        print("Xaxis scale is logarithmic but series " + series +
                              " has xdata[" + str(i) + "] = " + str(xdata[i]) + " (should be stricly positive)")
            if self.logarithmicy:
                for i in range(0, len(ydata)):
                    if ydata[i] <= 0:
                        print("Yaxis scale is logarithmic but series " + series +
                              " has ydata[" + str(i) + "] = " + str(ydata[i]) + " (should be stricly positive)")
        for key, value in self.yaxis_data.items():
            series = key
            ydata = value
            xdata = self.xaxis_data.get(series)
            if xdata is None:
                print("Series: " + series + " has ydata but no xdata")
                correct = False

        return correct

    def get_data_structure_representation(self):
        """
        Get a JSON of the data structure representation
        Returns:
            JSON string of the data structure
        """
        self.check()

        xaxis_json = []
        yaxis_json = []
        for key, value in self.xaxis_data.items():
            x_temp = []
            data_key = key
            data_value = value
            for i in range(0, len(data_value)):
                x_temp.append(data_value[i])
            temp_xaxis_json = {
                "Plot_Name": str(data_key),
                "xaxis_data": x_temp
            }
            xaxis_json.append(temp_xaxis_json)


        for key, value in self.yaxis_data.items():
            y_temp = []
            data_key = key
            data_value = value
            for i in range(0, len(data_value)):
                y_temp.append(data_value[i])
            temp_yaxis_json = {
                "Plot_Name": str(data_key),
                "yaxis_data": y_temp
            }
            yaxis_json.append(temp_yaxis_json)


        json_dict = {
            "plot_title": str(self.title),
            "subtitle": str(self.sub_title),
            "xLabel": str(self.x_label),
            "yLabel": str(self.y_label),
            "xaxisType": self.logarithmicx,
            "yaxisType": self.logarithmicy,
            "options": {
                "mouseTracking": self._mouse_track,
                "dataLabels": str(self.data_label)
            },
            "xaxis_data": xaxis_json,
            "yaxis_data": yaxis_json
        }

        return json_dict
