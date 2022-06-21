


class Primitives:

    def __init__(self, type: str, position: list = None):
        self._type = type
        self._position = position
        self.transform = []
        self._color = "red"
        self._object_json = {
            'type': self._type,
            'position': self._position,
            'transform': self.transform,
            'color': self._color
        }

    def push_representation(self, scene_json):
        scene_json['meshes'].append(self._object_json)