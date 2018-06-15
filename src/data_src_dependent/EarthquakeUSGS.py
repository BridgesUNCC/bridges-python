import time

class EarthquakeUSGS:

    def getDate(self):

        s = self.getTime()
        epoch_time = int(self.getTime())
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

    def getTime(self):
        return self.time

    def setTime(self, tm):
        self.time = tm

    def getYear(self):
        self.getDate()
        return self.year

    def getMonth(self):
        self.getDate()
        return self.month

    def getDay(self):
        self.getDate()
        return self.day

    def getHour(self):
        self.getDate()
        return self.hour

    def getMinutes(self):
        self.getDate()
        return self.min

    def getSeconds(self):
        self.getDate()
        return self.sec

    def getLatit(self):
        return self.latit

    def setLatit(self, latit):
        self.latit = latit

    def getLongit(self):
        return self.longit

    def setLongit(self, longit):
        self.longit = longit

    def getLocation(self):
        return self.location

    def setLocation(self, location):
        self.location = location

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getUrl(self):
        return self.url

    def setUrl(self, url):
        self.url = url

    def getMagnitude(self):
        return self.magnitude

    def setMagnitude(self,magnitude):
        self.magnitude = magnitude




