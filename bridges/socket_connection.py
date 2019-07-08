import socketio

class SocketConnection:
    _sio = socketio.Client()
    _listeners = []

    def add_listener(self, to_add):
        print("Subscribing to keypress events..")
        self._listeners.append(to_add)

    def setup_connection(self, user, assignment):
        try:
            url = "https://bridges-games.herokuapp.com"
            self._sio.connect(url)

            @self._sio.on('on')
            def
        except ConnectionError as e:
            print(e)




