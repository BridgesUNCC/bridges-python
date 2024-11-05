import json


class BarChart:
    """
    @brief Support for drawing Bar charts.
 
    Bar charts (https://en.wikipedia.org/wiki/Bar_chart) are used to
    represent categorical data as a series of rectangular bars with length
    proportional to the values they represent.
    
    Series in a bar chart provides data for a number of categories
    (sometimes called bins). Categories are defined using
    BarChart.categories and the series are added using BarChart.add_data_series().
    The series are rendered in the order in which they were added. Once
    a series has been added, it can not be modified.
    
    One should always define the categories before adding data. Changing the
    categories after series have been added will throw exceptions;
    adding series with different number of values than the number of
    categories will throw an exception.
    
    The Bar charts can have a title, subtitle. The charts can be
    horizontal or vertically oriented, using BarChart.orientation.
    
    A tooltip indicating the value of a series in a particular bin is
    displayed by hovering on a bar. One can append a string to the
    value using barchart.tooltip_suffix to specify units in the tooltip if desired.
    
      @sa See tutorial on using BarChart at:
       https://bridgesuncc.github.io/tutorials/BarChart.html
    """

    # constructor method

    def __init__(self):
        self._c_label = ""
        self._v_label = ""
        self._title = ""
        self._subtitle = ""
        self._tt_suffix = ""
        self._orientation = "horizontal"
        self._series_data = []
        self._cats = []

    # simple getters and setters to access attributes
    def get_data_structure_type(self):
        return "BarChart"


    @property
    def title(self) -> str:
        """
        Title of the plot
        """
        return self._title

    @title.setter
    def title(self, plot_title: str) -> None:
        """
        Title of the plot
        """
        self._title = plot_title

    @property
    def subtitle(self) -> str:
        """
        Subtitle of the plot
        """
        return self._subtitle

    @subtitle.setter
    def subtitle(self, plot_sub_title: str) -> None:
        """
        Subtitle of the plot
        """
        self._subtitle = plot_sub_title

    @property
    def value_label(self) -> str:
        """
        Label for the value axis
        """
        return self._v_label

    @value_label.setter
    def value_label(self, value_label: str) -> None:
        """
        Label for the value axis
        """
        self._v_label = value_label

    @property
    def categories_label(self) -> str:
        """
        Label for the categories axis
        """
        return self._c_label

    @categories_label.setter
    def categories_label(self, c_label: str) -> None:
        """
        Label for the categories axis
        """
        self._c_label = c_label

    @property
    def orientation(self) -> str:
        """
        Orientation of the bar chart.

        Will always be either "horizontal" or "vertical"
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orient) -> str:
        """
        Sets orientation of the bar chart.

        Must be either "horizontal" or "vertical". Will throw an exception otherwise.
        """
        if orient != "horizontal" and orient != "vertical":
            raise ValueError ("Bar chart orientation must be either \"horizontal\" or \"vertical\"")
        self._orientation = orient

    @property
    def tooltip_suffix(self) -> str:
        """
        the tooltip suffix
        
        This string is appended to the values in the hover tooltip.
        """
        return self._tt_suffix

    @tooltip_suffix.setter
    def tooltip_suffix(self, suffix: str) -> None:
        """
        the tooltip suffix
        
        This string is appended to the values in the hover tooltip.
        """
        self._tt_suffix = suffix

    @property
    def categories(self) -> list[str]:
        """
        Categories for this bar chart
        """
        return self._cats

    @categories.setter
    def categories(self, series_bins: list[str]) -> None:
        """
        Set the categories for the bar chart

        will throw an exception if there are already data series defined.
        """
        if len (self._series_data) >0:
            raise RuntimeError("Can't change categoriess after series have been added.")
        self._cats = series_bins

    def add_data_series(self, name:str, values:list[float]) -> None:
        """ 
        Add a series of data
        
        This will throw an exception if the data vector does not have the same	 
        size as the number of categories.
				 
	This will throw exceptions if two series have the same name.
	
	Args:
           name indicates the name of the data to add
           values values of that serie for each category
        """
        if len(values) != len (self.categories):
            raise ValueError("The data vector should have the same size as the number of categories.")

        for others in self._series_data:
            if name == others[0]:
                raise ValueError("Can't have two series with the same name.")
        
        self._series_data.append ((name, values))

    #Gets the data structure representation as a JSON string
    #Returns: data structure reprsentation (json string)
    def get_data_structure_representation(self):
        bins = {
            "xAxis": {
                "categories": self.categories
            }
        }
        series = []
        for key, value in self._series_data:
            temp_dict = {
                "name": key,
                "data": value
            }
            series.append(temp_dict)
        #print(series)
        json_dict = {
            "plot_title": self.title,
            "subtitle": self.subtitle,
            "x_label": self.categories_label,
            "y_label": self.value_label,
            "tooltip_suffix": self.tooltip_suffix,
            "alignment": self.orientation,
            "xaxis_data": { "xAxis": {"categories": self.categories} },
            "yaxis_data": {"series": series}
        }
        json_output = json.dumps(json_dict)
        return json_dict


