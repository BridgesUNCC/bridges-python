

class EleData:
    """
    Getter for data width
    """
    @property
    def cols(self):
        return self.ncols

    """
    Setter for data width
    """
    @cols.setter
    def cols(self, ncols):
        self.ncols = ncols

    """
    Getter for data height
    """
    @property
    def rows(self):
        return self.nrows

    """
    Setter for data height
    """
    @rows.setter
    def rows(self, nrows):
        self.nrows = nrows 

    """
    Getter for elev. data
    """
    @property
    def data(self):
        return self._data

    """
    Setter for elev. data
    """
    @data.setter
    def data(self, eledata):
        self._data = eledata

    """
    Getter for data origin (X)
    """
    @property
    def xll(self):
        return self._xll

    """
    Setter for data origin (X)
    """
    @xll.setter
    def xll(self, value):
        self._xll = value

    """
    Getter for data origin (Y)
    """
    @property
    def yll(self):
        return self._yll

    """
    Setter for data origin (Y)
    """
    @yll.setter
    def yll(self, value):
        self._yll = value

    """
    Getter for cell size
    """
    @property
    def cellsize(self):
        return self._cellsize

    """
    Setter for cell size
    """
    @cellsize.setter
    def cellsize(self, value):
        self._cellsize = value
    
    """
    Getter for max val
    """
    @property
    def maxVal(self):
        return self._maxVal

    """
    Setter for max val
    """
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
