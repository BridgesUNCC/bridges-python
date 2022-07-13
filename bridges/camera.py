

class Camera:

    def __init__(self, type, fov, position):
        self._type = type
        self._position = position
        self._fov = fov
        self._object_json = {
            'type': type,
            'fov': self._fov,
            'position': self._position
        }

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def fov(self):
        return self._fov

    @fov.setter
    def fov(self, fov:int):
        self._fov = fov

    def push_representation(self, scene_json):
        scene_json['camera'] = self._object_json


