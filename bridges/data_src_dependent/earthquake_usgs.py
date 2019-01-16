import time


class EarthquakeUSGS:

    def getDate(self):

        s = self.get_time()
        epoch_time = int(self.get_time())
        eq_time = epoch_time/1000

        eqt = time.gmtime(eq_time)

        year = eqt.tm_year + 1900
        month = eqt.tm_mon
        day = eqt.tm_mday
        hour = eqt.tm_hour
        sec = eqt.tm_sec
        min = eqt.tm_min

    def __init__(self, magnitude = None, longit = None, latit = None, location = None, title = None, url = None, time = None):
        if magnitude is not None:
            self.magnitude = magnitude
        else:
            self.magnitude = 0.0

        if longit is not None:
            self.longit = longit
        else:
            self.longit = 0.0

        if latit is not None:
            self.latit = latit
        else:
            self.latit = 0.0

        if location is not None:
            self.location = location
        else:
            self.location = ""

        if title is not None:
            self.title = title
        else:
            self.title = ""

        if url is not None:
            self.url = url
        else:
            self.url = ""

        if time is not None:
            self.time = time
        else:
            self.time = ""
            self.year = self.month = self.day = self.hour = self.min = self.sec =0

    def get_time(self):
        return self.time

    def set_time(self, tm):
        self.time = tm

    def get_year(self):
        self.getDate()
        return self.year

    def get_month(self):
        self.getDate()
        return self.month

    def get_day(self):
        self.getDate()
        return self.day

    def get_hour(self):
        self.getDate()
        return self.hour

    def get_minutes(self):
        self.getDate()
        return self.min

    def get_seconds(self):
        self.getDate()
        return self.sec

    def get_latit(self):
        return self.latit

    def set_latit(self, latit):
        self.latit = latit

    def get_longit(self):
        return self.longit

    def set_longit(self, longit):
        self.longit = longit

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url

    def get_magnitude(self):
        return self.magnitude

    def set_magnitude(self,magnitude):
        self.magnitude = magnitude




