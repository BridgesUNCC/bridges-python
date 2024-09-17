import json


class BarChart:
    # constructor method

    def __init__(self):
        self.x_label = ""
        self.y_label = ""
        self.plot_title = ""
        self.plot_sub_title = ""
        self.tooltip_suffix = ""
        self.alignment = "horizontal"
        self.series_data = {}
        self.series_bins = []

    # simple getters and setters to access attributes
    def get_data_structure_type(self):
        return "BarChart"


    @property
    def title(self) -> str:
        return self.plot_title

    @title.setter
    def title(self, plot_title: str) -> None:
        self.plot_title = plot_title

    @property
    def sub_title(self) -> str:
        return self.plot_sub_title

    @sub_title.setter
    def sub_title(self, plot_sub_title: str) -> None:
        self.plot_sub_title = plot_sub_title

    @property
    def series_label(self) -> str:
        return self.y_label

    @series_label.setter
    def series_label(self, y_label: str) -> None:
        self._y_label = y_label

    @property
    def bins_label(self) -> str:
        return self.x_label

    @bins_label.setter
    def bins_label(self, x_label: str) -> None:
        self.x_label = x_label

    @property
    def alignment(self, new_alignment) -> str:
        self.alignment = new_alignment

    @alignment.setter
    def alignment(self) -> str:
        return self.alignment

    @property
    def tooltip_suffix(self) -> str:
        return self.tooltip_suffix

    @tooltip_suffix.setter
    def set_tooltip_suffix(self, tooltip_suffix: str) -> None:
        self.tooltip_suffix = tooltip_suffix

    @property
    def series_data(self):
        return self.series_data

    @series_data.setter
    def series_data(self, series_name: str, data: float) -> None:
        self.series_data[series_name] = data

    @property
    def series_bins(self):
        return self.series_bins

    @series_bins.setter
    def series_bins(self, series_bins) -> None:
        self.series_bins = series_bins

    #Gets the data structure representation as a JSON string
    #Returns: data structure reprsentation (json string)
    def get_data_structure_representation(self):
        bins = {
            "xAxis": {
                "categories": self.get_series_bins()
            }
        }
        series = []
        for key, value in self.get_series_data().items():
            temp_dict = {
                "name": key,
                "data": value
            }
            series.append(temp_dict)
        print(series)
        json_dict = {
            "plot_title": self.get_title(),
            "subtitle": self.get_sub_title(),
            "x_label": self.get_bins_label(),
            "y_label": self.get_series_label(),
            "tooltip_suffix": self.get_tooltip_suffix(),
            "alignment": self.get_bar_alignment(),
            "xaxis_data": bins,
            "yaxis_data": {"series": series}
        }
        json_output = json.dumps(json_dict)
        return json_dict


