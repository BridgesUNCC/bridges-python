import socketio
import json


class SocketConnection:
    _sio = socketio.Client()
    _listeners = []

    def __init__(self, b):
        self.bridges = b

    @_sio.event
    def add_listener(self, to_add):
        print("Subscribing to keypress events..")
        self._listeners.append(to_add)

    @_sio.event
    def setup_connection(self, user, assignment):
        try:
            url = "https://bridges-games.herokuapp.com"
            self._sio.connect(url, transports=["websocket"])

            student_cred = {
                'user': user,
                'apikey': self.bridges.get_key(),
                'assignment': self.bridges.get_assignment_id()
            }
            student_cred = json.dumps(student_cred)

            print("passing student creditials to server..")
            self._sio.emit('credentials', student_cred)

        except ConnectionError as e:
            print(e)

    @_sio.on('announcement')
    def announcement(self, *args):
        obj = args
        print("announcement", obj)

    @_sio.on('keydown')
    def keydown(self, *args):
        print(self._listeners)
        obj = args
        for i in range(len(self._listeners)):
            self._listeners[i].key_press(obj)

    @_sio.on('keyup')
    def keyup(self, *args):
        obj = args
        for i in range(len(self._listeners)):
            self._listeners[i].key_press(obj)

    @_sio.on('disconnect')
    def disconnect(self):
        print("disconnected")

    def send_data(self, dataframe):
        if self._sio is not None:
            data = json.dumps(dataframe)
            self._sio.emit('gamegrid:recv', data)

    def close(self):
        self._sio.disconnect()
        self._sio.wait()








