import json
import os
import pickle

##
# This class is used to cache very large datasets, such as the OpenStreet Map data.
# This is for internal use only for efficiency.
#
# @author Jay Strahler, Erik Saule
# @date  2019, 2020
#

class lru_cache():

    def __init__(self, max_cache_size: int = 0):
        self.max_cache_size = max_cache_size + 1
        self.lru = []
        if not os.path.isdir("./bridges_data_cache"):
            os.mkdir("./bridges_data_cache")


    def put(self, hash, content):
        try:
            with open("./bridges_data_cache/lru.txt", "rb") as fp:
                self.lru = pickle.load(fp)
        except:
            pass


        try: # Removes the location requested by the user from the LRU list
            self.lru.remove(hash)
        except:
            pass
        self.lru.insert(0, hash)

        # Removes least used map if there are more than 30 maps already saved
        if (len(self.lru) >= self.max_cache_size):
            re = self.lru[len(self.lru)-1]
            if (os.path.isfile(f"./bridges_data_cache/{re}")):
                os.remove(f"./bridges_data_cache/{re}")
            self.lru.remove(re)

        with open("./bridges_data_cache/lru.txt", "wb") as fp:   #Pickling
            pickle.dump(self.lru, fp)

        with open(f"./bridges_data_cache/{hash}", "wb") as f:   # write to file in cache
            pickle.dump(content, f)
        return



    def get(self, hash):
        with open("./bridges_data_cache/" + hash, "rb") as j:
            try:
                data = pickle.load(j)
            except:
                print("Error: Issue reading locally cached file")
        return data



    def inCache(self, file_name):
        if (os.path.isfile(f"./bridges_data_cache/{file_name}")):
            return True
        return False
