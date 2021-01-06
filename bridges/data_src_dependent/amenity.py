

class amenityData:
    """
    @brief This class is a helper class to be used with amenities data retrieved from
    OpenStreet Map data
    
    @author Jay Strahler
    
    @date 12/28/20 
    """
    @property
    def id(self): 
        """
        @brief Get id of amenity
        Returns:
            id of amenity
        """
        return self.id_val
    
    @id.setter
    def id(self, id_val):
        """
        @brief Set id of amenity
        Args:
            id_val: id of amenity
        """
        self.id_val = id_val

    @property
    def lat(self): 
        """
        @brief Get latitude of amenity
        Returns:
            latitude of amenity
        """
        return self.lat_val
    
    @lat.setter
    def lat(self, lat_val):
        """
        @brief Set latitude of amenity
        Args:
           lat_val: latitude of amenity to set
        """
        self.lat_val = lat_val

    @property
    def lon(self): 
        """
        @brief Get longitude of amenity
        Returns:
           longitude of amenity
        """
        return self.lon_val
    
    @lon.setter
    def lon(self, lon_val):
        """
        @brief Set longitude of amenity
        Args:
           lon_val: longitude of amenity to set
        """
        self.lon_val = lon_val

    @property
    def name(self): 
        """
        @brief Get name of amenity
        Returns:
            name of amenity
        """
        return self.name_val
    
    @name.setter
    def name(self, name_val):
        """
        @brief Set name of amenity
        Args:
           name_val: name of amenity to set
        """
        self.name_val = name_val

    @property
    def other(self): 
        return self.other_data
    
    @other.setter
    def other(self, other_data):
        """
        @brief Set other of amenity
        Args:
            other_data: other data of amenity
        """
        self.other_data.append(other_data)

    def __init__(self):
        """
        @brief constructor - initialize object
        """
        self.id_val = 0
        self.lat_val = 0
        self.lon_val = 0
        self.name_val = None
        self.other_data = []

class meta:

    @property
    def minLat(self): 
        return self.minLat_val
    
    @minLat.setter
    def minLat(self, minLat_val):
        self.minLat_val = minLat_val

    @property
    def minLon(self): 
        return self.minLon_val
    
    @minLon.setter
    def minLon(self, minLon_val):
        self.minLon_val = minLon_val

    @property
    def maxLat(self): 
        return self.maxLat_val
    
    @maxLat.setter
    def maxLat(self, maxLat_val):
        self.maxLat_val = maxLat_val

    @property
    def maxLon(self): 
        return self.maxLon_val
    
    @minLon.setter
    def maxLon(self, maxLon_val):
        self.maxLon_val = maxLon_val


    @property
    def count(self):
        return self.count_val
    
    @count.setter
    def count(self, count_val):
        self.count_val = count_val

    def __init__(self, minLat_val, minLon_val, maxLat_val, maxLon_val, count_val):
        self.minLat_val = minLat_val
        self.minLon_val = minLon_val
        self.maxLat_val = maxLat_val
        self.maxLon_val = maxLon_val
        self.count_val = count_val

class amenities:

    @property
    def data(self):
        return self.data_val

    @data.setter
    def data(self, data_val):
        self.data_val.append(data_val)

    @property
    def meta(self):
        return self.meta_val

    @meta.setter
    def meta(self, meta_val):
        self.meta_val = meta_val

    def __init__ (self):
        self.data_val = []
        self.meta_val = None
