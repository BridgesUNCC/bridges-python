class ElevationData:
    """
    @brief  Class that holds elevation data

    The data is stored as a 2d array .data of .cols columns and .rows rows.
    The data at [0][0] are at location xll, yll and the spatial resolution 
    is cellsize.

    This object is generally not created by the user, to see how its created check 
    out bridges::data_src_dependent::data_source::get_elevation_data()

    @sa For an example, check out https://bridgesuncc.github.io/tutorials/Data_Elevation.html

    @author Jay Strahler, Kalpathi Subramanian
    
    @date 3/28/20, 12/29/20, 1/6/20
    """

    
    @property
    def cols(self):
        """ 
        @brief Get data width
        Returns:
            return the width of the data
        """ 
        return self.ncols

    @cols.setter
    def cols(self, ncols):
        """
        @brief Set width of elevation data grid
        Args:
             ncols:  elevation data width to set
        """
        self.ncols = ncols

    @property
    def rows(self):
        """
        Get data height
        Returns:
            return the height of the data
        """
        return self.nrows

    @rows.setter
    def rows(self, nrows):
        """
        Set height of elevation data grid
        Args: 
           nrows:  dlevation data height to set
        """
        self.nrows = nrows 

    @property
    def data(self):
        """ 
        @brief Get elevation data
        Returns:
            return the elevation data
        """ 
        return self._data

    @data.setter
    def data(self, eledata):
        """
        @brief Set elevation data
        Args: 
          eledata:  elevation data to set
        """
        self._data = eledata

    @property
    def xll(self):
        """ 
        @brief Get xcoord of  data origin
        Returns:
            return the elevation data lower left (x coord)
        """ 
        return self._xll

    @xll.setter
    def xll(self, xcoord):
        """
        @brief Set xcoord of elevation data origin
        Args: 
          xcoord:  elevation data xcoord of origin to set
        """
        self._xll = xcoord

    @property
    def yll(self):
        """ 
        @brief Get ycoord of  data origin
        Returns:
            return the elevation data lower left (y coord)
        """ 
        return self._yll

    @yll.setter
    def yll(self, ycoord):
        """
        @brief Set ycoord of elevation data origin
        Args: 
          ycoord:  elevation data ycoord of origin to set
        """
        self._yll = ycoord

    @property
    def cellsize(self):
        """ 
        @brief Get cell size (resolution)  of  elevation data
        Returns:
            return the elevation data cell size
        """ 
        return self._cellsize

    @cellsize.setter
    def cellsize(self, value):
        """
        @brief Set cell size (resolution)  of elevation data
        Args: 
          value:  cell size to set
        """
        self._cellsize = value
    
    @property
    def maxVal(self):
        """ 
        @brief Get max elevation value in the data
        Returns:
            return the max value in data
        """ 
        return self._maxVal

    @maxVal.setter
    def maxVal(self, value):
        """
        @brief Set max elevation value in the data
        Args: 
          value:  max value to set
        """
        self._maxVal = value


    @property
    def minVal(self):
        """ 
        @brief Get min elevation value in the data
        Returns:
            return the min value in data
        """ 
        return self._minVal

    @minVal.setter
    def minVal(self, value):
        """
        @brief Set min elevation value in the data
        Args: 
          value:  min value to set
        """
        self._minVal = value

        

    def __init__(self):
        """
        @brief Constructor - initialize elevation object
        """
        self.ncols = 0
        self.nrows = 0
        self._data = []
        self._xll = 0
        self._yll = 0
        self._cellsize = 0
        self.name = None
        self._maxVal = 0
        self._minVal = 0
