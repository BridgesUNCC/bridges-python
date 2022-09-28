
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

class Terrain_Mesh:

    def __init__(self, name, rows, cols, elevation_data):
        self._name = name
        self._rows = rows
        self._cols = cols
        self._vertices = elevation_data
        self._colors = [[[0 for k in range(3)] for j in range(cols)] for i in range(rows)]
        self._color = [1.0, 1.0, 1.0, 1.0]
        self._transform = []
        self._object_json = {
            'name': self._name,
            'type': "terrain",
            'vertices': self._vertices,
            'colors': self._colors,
            'rows': self._rows,
            'cols': self._cols
        }

    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, rows):
        self._rows = rows
        self._object_json['rows'] = self._rows

    @property
    def cols(self):
        return self._cols

    @cols.setter
    def cols(self, cols):
        self._cols = cols
        self._object_json['cols'] = self._cols

    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, vertices):
        self._vertices = vertices
        self._object_json['vertices'] = self._vertices

    @property
    def colors(self):
        return self._colors

    @colors.setter
    def colors(self, colors):
        self._colors = colors
        self._object_json['colors'] = self._colors

    def push_representation(self, scene_json):
        self._object_json['vertices'] = self._vertices
        self._object_json['colors'] = self._colors
        scene_json['meshes'].append(self._object_json)