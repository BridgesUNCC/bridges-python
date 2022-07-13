import socketio
import json

class SocketConnection:
    """
    This class is used internally as part of the BRIDGES Game API to set up 
    connections to the BRIDGES Game server. Not to be used directly by BRIDGES 
    users directly
    """

    _sio = socketio.Client()
    _listeners = []
    _verbose = False
    
    def __init__(self, b):
        self.bridges = b

    @staticmethod
    def add_listener(to_add):
        print("Subscribing to keypress events..", to_add)
        SocketConnection._listeners.append(to_add)

    def setup_connection(self, user, assignment):
        try:
            #url = "https://bridges-games.herokuapp.com"
            url = self.bridges.connector.get_server_url()
            if self._verbose:
                print ("attempting to connect to socket.io at "+url)
            SocketConnection._sio.connect(url, transports=["websocket"])

            student_cred = {
                'user': self.bridges.get_username(),
                'apikey': self.bridges.get_key(),
                'assignment': self.bridges.get_assignment_id()
            }
            student_cred = json.dumps(student_cred)

            if self._verbose:
                print("passing student credentials to server..")
            SocketConnection._sio.emit('credentials', student_cred)

        except ConnectionError as e:
            print(e)

#    @_sio.on('announcement')
#    def announcement(*args):
#        print("announcement", *args)

    @_sio.on('keydown')
    def keydown(*args):
        #print(*args)
        for i in range(0, len(SocketConnection._listeners)):
            SocketConnection._listeners[i].key_press(*args)

    @_sio.on('keyup')
    def keyup(*args):
        for i in range(0, len(SocketConnection._listeners)):
            SocketConnection._listeners[i].key_press(*args)

    @_sio.on('disconnect')
    def disconnect(*args):
        print(*args, "disconnected")

    def send_data(self, dataframe, vistype):
        if SocketConnection._sio is not None:
            data = json.dumps(dataframe)
            SocketConnection._sio.emit(vistype.lower() + ':recv', data)

    def close(self):
        SocketConnection._sio.disconnect()
        SocketConnection._sio.wait()








