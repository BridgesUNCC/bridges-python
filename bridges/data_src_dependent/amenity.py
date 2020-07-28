

class amenityData:

    @property
    def id(self): 
        return self.id_val
    
    @id.setter
    def id(self, id_val):
        self.id_val = id_val

    @property
    def lat(self): 
        return self.lat_val
    
    @lat.setter
    def lat(self, lat_val):
        self.lat_val = lat_val

    @property
    def lon(self): 
        return self.lon_val
    
    @lon.setter
    def lon(self, lon_val):
        self.lon_val = lon_val

    @property
    def name(self): 
        return self.name_val
    
    @name.setter
    def name(self, name_val):
        self.name_val = name_val

    @property
    def other(self): 
        return self.other_data
    
    @other.setter
    def other(self, other_data):
        self.other_data.append(other_data)

    def __init__(self):
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