class EleData:

    @property
    def cols(self):
        return self.ncols

    @cols.setter
    def cols(self, ncols):
        self.ncols = ncols

    @property
    def rows(self):
        return self.nrows

    @rows.setter
    def rows(self, nrows):
        self.nrows = nrows 

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, eledata):
        self._data = eledata

    @property
    def xll(self):
        return self._xll

    @xll.setter
    def xll(self, value):
        self._xll = value

    @property
    def yll(self):
        return self._yll

    @yll.setter
    def yll(self, value):
        self._yll = value

    @property
    def cellsize(self):
        return self._cellsize

    @cellsize.setter
    def cellsize(self, value):
        self._cellsize = value
    
    @property
    def maxVal(self):
        return self._maxVal

    @maxVal.setter
    def maxVal(self, value):
        self._maxVal = value



    def __init__(self):
        self.ncols = 0
        self.nrows = 0
        self._data = []
        self._xll = 0
        self._yll = 0
        self._cellsize = 0
        self.name = None
        self._maxVal = 0