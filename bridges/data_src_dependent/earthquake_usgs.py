import datetime
import time

##
#
#    Class that hold earthquake data, for use with USGIS retrieved quake data.
#    Class that holds earthquake USGIS data. BRIDGES uses scripts to 
#    continually monitor USGIS site (tweets) and retrieve the latest 
#    quake data for use in student projects.
#
#    @author Matthew Mcquaigue, Kalpathi Subramanian,
#    @date  2/18/18, 12/29/20
#

class EarthquakeUSGS:
    def __set_time_from_unix_timestamp(self, tm):
        epoch_time = int(tm)
        eq_time = epoch_time / 1000
        eqt = time.gmtime(eq_time)
        self._time = time.strftime("%Y-%m-%d %H:%M:%S", eqt)

    ##
    # constructor
    # @param magnitude magnitude of quake 
    # @param latitude  latitude position
    # @param longitude longitude position
    # @param location  location of quake
    # @param title     title (has some of eq info in a string)
    # @param url       url for more information
    # @param time       occurrence time of quake
    #
    def __init__(self, magnitude=None, longit=None, latit=None, location=None, 
                     title=None, url=None, time=None):
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
            self._time =  time

    ##
    #  Get occurrence time (epoch)  of quake
    #
    @property
    def time(self):
        return self._time

    ##
    #      Set occurrence time (epoch)  of quake
    #    @param tm  occurrence time (epoch)    
    #
    @property
    @time.setter
    def time(self, tm) -> None:
        self.__set_time_from_unix_timestamp(tm)

    ##
    #  Get latitude of quake
    #
    @property
    def latit(self) -> float:
        return self._latit

    ##
    #      Set latitude of quake
    #    @param  latit latitude to set
    #
    @latit.setter
    def latit(self, latit: float) -> None:
        self._latit = latit

    ##
    #  Get longitude of quake
    #
    @property
    def longit(self) -> float:
        return self._longit

    ##
    #      Set longitude of quake
    #    @param  longit longitude to set
    #
    @longit.setter
    def longit(self, longit: float) -> None:
        self._longit = longit

    ##
    # Get the location of quake (typically a city or something of the sort)
    #
    @property
    def location(self) -> str:
        return self._location

    ##
    #      Set location of quake
    #    @param  location location to set
    #
    @location.setter
    def location(self, location: str):
        self._location = location

    ##
    #  
    #   Get the title of quake (typically a one line description)
    #   @return title of quake
    @property
    def title(self) -> str:
        return self._title

    ##
    #    Set title of quake
    #    @param  title of quake to set
    #
    @title.setter
    def title(self, title: str):
        self._title = title

    ##
    #  Get url of quake
    #
    @property
    def url(self) -> str:
        return self._url

    ##
    #      Set url of quake
    #    @param  url of quake to set
    #
    @url.setter
    def url(self, url: str):
        self._url = url

    ##
    #  @brief Get magnitude of quake on the Richter scale 
    #
    @property
    def magnitude(self) -> float:
        return self._magnitude

    ##
    #      Set magnitude of quake
    #    @param  magn magnitude of quake to set
    #
    @magnitude.setter
    def magnitude(self, magn: float):
        """
        Setter for the magnitude of the quake
        Args:
            magnitude: magnitude to set
        """
        self._magnitude = magnitude
