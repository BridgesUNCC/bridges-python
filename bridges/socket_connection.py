import socketio


class SocketConnection:
    _sio = socketio.Client()
    _listeners = []

    @_sio.event
    def add_listener(self, to_add):
        print("Subscribing to keypress events..")
        self._listeners.append(to_add)

    @_sio.event
    def setup_connection(self, user, assignment):
        try:
            url = "https://bridges-games.herokuapp.com"
            self._sio.connect(url)

            student_cred = {
                'user': user,
                'assignment': assignment.split('.')[0]
            }

            self._sio.emit('credentials', student_cred)

        except ConnectionError as e:
            print(e)

    @_sio.event
    def connect(self):
        print("Connected")

    @_sio.on('keydown')
    def keydown(self, args):
        obj = args[0]
        for i in range(len(self._listeners)):
            self._listeners[i].keypress(obj)

    @_sio.on('keyup')
    def keyup(self, args):
        obj = args[0]
        for i in range(len(self._listeners)):
            self._listeners[i].keypress(obj)

    @_sio.event
    def disconnect():
        print("disconnected")

    def send_data(self, dataframe):
        if self._sio is None:
            self._sio.emit('gamegrid:recv', dataframe)

    def close(self):
        self._sio.disconnect()
        self._sio.wait()








