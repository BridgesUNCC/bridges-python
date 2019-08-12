import datetime
import time

class EarthquakeUSGS:

    def __set_time_from_unix_timestamp(self, tm):
        epoch_time = int(tm)
        eq_time = epoch_time/1000
        eqt = time.gmtime(eq_time)
        self._time = time.strftime("%Y-%m-%d %H:%M:%S", eqt)

    def __init__(self, magnitude = None, longit = None, latit = None, location = None, title = None, url = None, time = None):
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
        return self._time

    @time.setter
    def time(self, tm):
        self.__set_time_from_unix_timestamp(tm)

    @property
    def latit(self):
        return self._latit

    @latit.setter
    def latit(self, latit):
        self._latit = latit

    @property
    def longit(self):
        return self._longit

    @longit.setter
    def longit(self, longit):
        self._longit = longit

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def magnitude(self):
        return self._magnitude

    @magnitude.setter
    def magnitude(self,magnitude):
        self._magnitude = magnitude




