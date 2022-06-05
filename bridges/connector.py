
import requests
import traceback
import os

class Connector:
    """
    @brief This is a class for handling calls to the BRIDGES server to transmit JSON to the server and subsequent visualization. It is not intended for external use
    """

    server_url_live = "http://bridges-cs.herokuapp.com"
    server_type = "application"
    server_url_clone = "http://bridges-clone.herokuapp.com"
    server_url_local = "http://127.0.0.1:3000"
    server_url_game = "http://bridges-games.herokuapp.com"

    key = ""
    username =""

    pattern_found = 0
    debug = False

    def __init__(self, key, username, assignment):
        """
        @brief Connector object constructor
        Args:
            key: is the user_key
            username: is students username
            assignment: is the assignment number for the assignment
        """
        self.key = key
        self.username = username
        self.assignment = assignment
        self.set_server_url ("live")

    def set_server(self, server):
        """
        @brief Set the server based on a keyword for url
        Args:
            server: is one of the three string keywords('live', 'clone', 'local') that is passed to change the server that the bridges visualization will be sent to
        """
        self.set_server_url(server)


    def set_server_url(self, server_url):
        """
        @brief Set the server url (string) that is passed to change the server that the bridges visualization will be sent to
   
        Args: 
            server: is one of the three strings ('live', 'clone', 'local')
        """
        switcher = {
            "live": "http://bridges-cs.herokuapp.com",
            "clone": "http://bridges-clone.herokuapp.com",
            "local": "http://127.0.0.1:3000",
            "games": "http://bridges-games.herokuapp.com"
        }
        force = os.getenv("FORCE_BRIDGES_APISERVER", "")
        if (force != ""):
            server_url = force
        
        self.server_url = switcher.get(server_url, ValueError("Use: live, clone, local to determine url"))


    def get_server_url(self):
        """
        @brief Get the server url (string)
        Returns:
            return server url (string)
        """
        return self.server_url

    def post(self, url, data):
        """
        @brief post the data (JSON) to the server
        Args:
            url:  url of server
            data: JSON of the data structure representation
        """
        try:
            if self.key.isdigit() is not True:
                raise Exception("Key entered is not a valid Key. Please enter a valid Key")
        except Exception as e:
            return traceback.print_tb(e.__traceback__)

        r = requests.post(self.prepare(url), headers={u'content-type': u'application/json'}, data=data.encode('utf-8'))
        if r.status_code != 200:
             print(r.status_code, r.reason)
             print(r.text)
        return r.status_code

    def prepare(self, url):
        """
        @brief prepare the  post string for transmission to the server
        Args:
            url:  url of server
        """
        out = self.server_url
        out += url
        out += "?apikey=" + self.key + "&username=" + self.username
        return out

