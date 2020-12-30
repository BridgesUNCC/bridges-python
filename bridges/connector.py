
import requests
import traceback

##
#
# @brief This is a class for handling calls to the BRIDGES server to transmit
# JSON to the server and subsequent visualization. It is not
# intended for external use
#

class Connector:
    server_url_live = "http://bridges-cs.herokuapp.com"
    server_type = "application"
    server_url_clone = "http://bridges-clone.herokuapp.com"
    server_url_local = "http://127.0.0.1:3000"
    server_url_game = "http://bridges-games.herokuapp.com"

    key = ""
    username =""

    pattern_found = 0
    debug = False

    ##
    # @brief Connector object constructor
    # @param key is the user_key
    # @param username is students username
    # @param assignment is the assignment number for the assignment
    def __init__(self, key, username, assignment):
        self.key = key
        self.username = username
        self.assignment = assignment
        self.server_url = "http://bridges-cs.herokuapp.com"

    ##
    # @brief Set the server based on a keyword for url
    # @param server is one of the three string keywords('live', 'clone', 'local')
    # that is passed to change the server that the bridges visualization will be sent to
    def set_server(self, server):
        self.set_server_url(server)


    ##
    # @brief Set the server url (string)
    # that is passed to change the server that the bridges visualization 
	# will be sent to
    #
    # @param server is one of the three strings ('live', 'clone', 'local')
    def set_server_url(self, server_url):
        switcher = {
            "live": "http://bridges-cs.herokuapp.com",
            "clone": "http://bridges-clone.herokuapp.com",
            "local": "http://127.0.0.1:3000",
            "games": "http://bridges-games.herokuapp.com"
        }
        self.server_url = switcher.get(server_url, ValueError("Use: live, clone, local to determine url"))


    ##
    # @brief Get the server url (string)
    # @return server url (string)
    def get_server_url(self):
        return self.server_url

   	##
   	# @brief post the data (JSON) to the server
	# @param url  url of server
	# @param data JSON of the data structure representation
	#
    def post(self, url, data):
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

   	##
   	# @brief prepare the  post string for transmission to the server
	# @param url  url of server
	#
    def prepare(self, url):
        out = self.server_url
        out += url
        out += "?apikey=" + self.key + "&username=" + self.username
        return out

