


class Primitives:

    def __init__(self, type: str, position: list = None):
        self._type = type
        self._position = position
        self._object_json = {
            'type': self._type

        }

    def push_representation(self, scene_json):
        scene_json['meshes'].append(self._object_json)