

class EleData:
    """
    @brief class storing elevation data.

    The data is stored as a 2d array .data of .cols columns and .rows rows.
    The data at [0][0] are at location .xll, .yll and the spatial resolution is .cellsize.
    """

    @property
    def cols(self):
        """
        Getter for data width
        """
        return self.ncols

    @cols.setter
    def cols(self, ncols):
        """
        Setter for data width
        """
        self.ncols = ncols

    @property
    def rows(self):
        """
        Getter for data height
        """
        return self.nrows

    @rows.setter
    def rows(self, nrows):
        """
        Setter for data height
        """
        self.nrows = nrows 

    @property
    def data(self):
        """
        Getter for elev. data
        """
        return self._data

    @data.setter
    def data(self, eledata):
        """
        Setter for elev. data
        """
        self._data = eledata

    @property
    def xll(self):
        """
        Getter for data origin (X)
        """
        return self._xll

    @xll.setter
    def xll(self, value):
        """
        Setter for data origin (X)
        """
        self._xll = value

    @property
    def yll(self):
        """
        Getter for data origin (Y)
        """
        return self._yll

    @yll.setter
    def yll(self, value):
        """
        Setter for data origin (Y)
        """
        self._yll = value

    @property
    def cellsize(self):
        """
        Getter for cell size
        """
        return self._cellsize

    @cellsize.setter
    def cellsize(self, value):
        """
        Setter for cell size
        """
        self._cellsize = value
    
    @property
    def maxVal(self):
        """
        Getter for max val
        """
        return self._maxVal

    @maxVal.setter
    def maxVal(self, value):
        """
        Setter for max val
        """
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
