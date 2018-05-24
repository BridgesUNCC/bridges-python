
import requests
import Bridges
import json



class Connector:
    #server_url = "http://bridges-clone.herokuapp.com"
    server_url = "http://localhost:3000"
    server_type = "application"
    # server_url = "http://bridges-cs.herokuapp.com"
    key = ""

    pattern_found = 0
    debug = False

    def __init__(self, key):
        self.key = key


    def set_server(self, server):
        self.set_server_url(self.server_url)


    def set_server_url(self, server_url):
        while (server_url.endswith("/")):
            server_url = server_url[0:len(server_url) - 1]
        if (len(server_url) > 0):
            self.server_url = server_url

    def get_server_url(self):
        return self.server_url

    def post(self, url, data):
        r = requests.post(self.prepare(url), headers={u'content-type': u'application/json'}, data=data)
        print(r.status_code, r.reason)

    def prepare(self, url):
        out = self.server_url
        out += url
        out += "?apikey=" + self.key
        return out

