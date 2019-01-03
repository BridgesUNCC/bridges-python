
import requests
import traceback



class Connector:
    server_url_live = "http://bridges-cs.herokuapp.com"
    server_type = "application"
    server_url_clone = "http://bridges-clone.herokuapp.com"
    server_url_local = "http://127.0.0.1:3000"

    key = ""
    username =""

    pattern_found = 0
    debug = False

    ##
    # Connector object constructor
    # @param key is the user_key
    # @param username is students username
    # @param assignment is the assignment number for the assignment
    def __init__(self, key, username, assignment):
        self.key = key
        self.username = username
        self.assignment = assignment
        self.server_url = "http://bridges-cs.herokuapp.com"

    ##
    # Set the server based on a keyword for url
    # @param server is one of the three string keywords('live', 'clone', 'local')
    # that is passed to change the server that the bridges visualization will be sent to
    def set_server(self, server):
        self.set_server_url(server)


    def set_server_url(self, server_url):
        switcher = {
            "live": "http://bridges-cs.herokuapp.com",
            "clone": "http://bridges-clone.herokuapp.com",
            "local": "http://127.0.0.1:3000"
        }
        self.server_url = switcher.get(server_url, ValueError("Use: live, clone, local to determine url"))


    def get_server_url(self):
        return self.server_url

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

    def prepare(self, url):
        out = self.server_url
        out += url
        out += "?apikey=" + self.key + "&username=" + self.username
        return out

