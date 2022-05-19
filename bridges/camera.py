

class Camera:

    def __init__(self, type):
        self._type = type
        self._object_json = {
            'type': type
        }

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    def push_representation(self, scene_json):
        scene_json['camera'] = self._object_json


