
import requests
import traceback



class Connector:
    server_url_live = "http://bridges-cs.herokuapp.com"
    server_type = "application"
    server_url_clone = "http://bridges-clone.herokuapp.com"
    server_url_local = "http://bridges-clone.herokuapp.com"

    key = ""
    username =""

    pattern_found = 0
    debug = False

    def __init__(self, key, username, assignment):
        self.key = key
        self.username = username
        self.assignment = assignment
        self.server_url = "http://bridges-cs.herokuapp.com"


    def set_server(self, server):
        self.set_server_url(server)


    def set_server_url(self, server_url):
        switcher = {
            "live": "http://bridges-cs.herokuapp.com",
            "clone": "http://bridges-clone.herokuapp.com",
            "local": "http://bridges-clone.herokuapp.com"
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

