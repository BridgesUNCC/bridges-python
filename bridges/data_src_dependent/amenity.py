
class Amenity:
    """
    @brief This class is a helper class to be used with amenities data retrieved from OpenStreet Map data

    The dataset contains amenity id, latitude, longitude, name, and a list of 
    various other values.

    This object is generally not created by the user, to see how its created check 
    out bridges::data_src_dependent::data_source::get_amenity_data()
    
    @sa For an example, check out https://bridgesuncc.github.io/tutorials/Data_Amenity.html
    
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

