import datetime
import time


class EarthquakeUSGS:
    """
	Class that hold earthquake data, for use with USGIS retrieved quake data.
    Class that holds earthquake USGIS data. BRIDGES uses scripts to continually monitor
	USGIS site (tweets) and retrieve the latest quake data for use in student projects.
	Kalpathi Subramanian, 2/18/18
    """

    def __set_time_from_unix_timestamp(self, tm):
        epoch_time = int(tm)
        eq_time = epoch_time / 1000
        eqt = time.gmtime(eq_time)
        self._time = time.strftime("%Y-%m-%d %H:%M:%S", eqt)

    def __init__(self, magnitude=None, longit=None, latit=None, location=None, title=None, url=None, time=None):
        self._time = int()
        if magnitude is not None:
            self._magnitude = magnitude
        else:
            self._magnitude = 0.0
        if longit is not None:
            self._longit = longit
        else:
            self._longit = 0.0
        if latit is not None:
            self._latit = latit
        else:
            self._latit = 0.0
        if location is not None:
            self._location = location
        else:
            self._location = ""
        if title is not None:
            self._title = title
        else:
            self._title = ""
        if url is not None:
            self._url = url
        else:
            self._url = ""
        if time is not None:
            self.time = time

    @property
    def time(self):
        """
        Getter for the time of the earthquakle
        Returns:
            time of earthquake
        """
        return self._time

    @time.setter
    def time(self, tm) -> None:
        """
        Set epoch time
        Args:
            tm: time as epoch
        """
        self.__set_time_from_unix_timestamp(tm)

    @property
    def latit(self) -> float:
        """
        Get latitude of quake
        Returns:
            latitude of the quake
        """
        return self._latit

    @latit.setter
    def latit(self, latit: float) -> None:
        """
        Setter for the latitude
        Args:
            latit: latitiude to set
        """
        self._latit = latit

    @property
    def longit(self) -> float:
        """
        Getter for the longitude of quake
        Returns:
            logitude
        """
        return self._longit

    @longit.setter
    def longit(self, longit: float) -> None:
        """
        Setter for the longitutde of the quake
        Args:
            longit: logitude to set
        """
        self._longit = longit

    @property
    def location(self) -> str:
        """
        Getter for the location of quake (typically a city or something of the sort)
        Returns:
            location
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """
        Setter for the location of the quake
        Args:
            location: location to set
        """
        self._location = location

    @property
    def title(self) -> str:
        """
        Getter for the title of quake (typically a one line description)
        Returns:
            title
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """
        Setter for the title of the quake
        Args:
            title: title to set
        """
        self._title = title

    @property
    def url(self) -> str:
        """
        Getter for the url of quake
        Returns:
            url
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """
        Setter for the url of the quake
        Args:
            url: url to set
        """
        self._url = url

    @property
    def magnitude(self) -> float:
        """
        Getter for the magnitude of quake on the scale on Richter scale
        Returns:
            magnitude
        """
        return self._magnitude

    @magnitude.setter
    def magnitude(self, magnitude: float):
        """
        Setter for the magnitude of the quake
        Args:
            magnitude: magnitude to set
        """
        self._magnitude = magnitude
