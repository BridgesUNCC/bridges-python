import datetime
import time

class EarthquakeUSGS:
    """
    @brief Class that holds earthquake data records.

    Class that hold earthquake data, for use with USGIS retrieved quake data.
    BRIDGES uses scripts to 
    continually monitor USGIS site (tweets) and retrieve the latest 
    quake data for use in student projects.

    This object is generally not created by the user, to see how its created check 
    out bridges::data_src_dependent::data_source::get_earthquake_usgs_data()

    @sa For an example, check out https://bridgesuncc.github.io/tutorials/Data_EQ_USGS.html

    @author Matthew Mcquaigue, Kalpathi Subramanian,
    @date  2/18/18, 12/29/20, 1/6/21
    """
    def __set_time_from_unix_timestamp(self, tm):
        epoch_time = int(tm)
        eq_time = epoch_time / 1000
        eqt = time.gmtime(eq_time)
        self._time = time.strftime("%Y-%m-%d %H:%M:%S", eqt)

    def __init__(self, magnitude=None, longit=None, latit=None, location=None, 
                     title=None, url=None, time=None):
        """
        @brief constructor
        Args: 
            magnitude: magnitude of quake 
            latit: latitude position
            longit: longitude position
            location:  location of quake
            title:     title (has some of eq info in a string)
            url:       url for more information
            time:       occurrence time of quake
        """
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
            self.time =  time

    @property
    def time(self):
        """   
        @brief Get occurrence time (epoch)  of quake
        Returns:
            Quake occurrence time
        """
        return self._time

    @time.setter
    def time(self, tm) -> None:
        """   
        @brief Set occurrence time (epoch)  of quake
        Args:
            tm: Quake occurrence time to set
        """
        self.__set_time_from_unix_timestamp(tm)

    @property
    def latit(self) -> float:
        """   
        @brief Get latitude of quake
        Returns:
            Quake latitude
        """
        return self._latit

    @latit.setter
    def latit(self, latit: float) -> None:
        """   
        @brief Set latitude of quake
        Args:
            latit: quake latitude to set
        """
        self._latit = latit

    @property
    def longit(self) -> float:
        """   
        @brief Get longitude of quake
        Returns:
            Quake longitude
        """
        return self._longit

    @longit.setter
    def longit(self, longit: float) -> None:
        """   
        @brief Set longitude of quake
        Args:
            longit: quake longitude to set
        """
        self._longit = longit

    @property
    def location(self) -> str:
        """   
        @brief Get location of quake (typically a city or something of the sort)
        Returns:
            Quake location 
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """   
        @brief Set location of quake
        Args:
            location: quake location to set
        """
        self._location = location

    @property
    def title(self) -> str:
        """   
        @brief Get quake title 
        Returns:
            Quake title 
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """   
        @brief Set title of quake
        Args:
            title: quake title to set
        """
        self._title = title

    @property
    def url(self) -> str:
        """   
        @brief Get quake url 
        Returns:
            Quake url 
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """   
        @brief Set url of quake
        Args:
            url: quake url to set
        """
        self._url = url

    @property
    def magnitude(self) -> float:
        """   
        @brief Get quake magnitude (Richter scale) 
        Returns:
            Quake magnitude 
        """
        return self._magnitude

    @magnitude.setter
    def magnitude(self, magn: float):
        """
        Setter for the magnitude of the quake
        Args:
            magn: magnitude to set
        """
        self._magnitude = magnitude
