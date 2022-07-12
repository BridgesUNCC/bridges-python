
class Mesh:

    def __init__(self, vertices: list):
        self._vertices = vertices
        self._color = [1.0, 1.0, 0.5, 1.0]
        self._transform = []
        self._object_json = {
            'type': "custom mesh",
            'vertices': vertices
        }

    def push_representation(self, scene_json):
        scene_json['meshes'].append(self._object_json)