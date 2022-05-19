

class Scene:

    def __init__(self):
        self._scene_list = []

    def get_data_structure_type(self):
        return 'Scene'

    def add(self, scene_object):
        self._scene_list.append(scene_object)

    def get_data_structure_representation(self):
        scene_json = {
            'meshes': [],
            'camera': None,
            'lights': []
        }
        for i in range(len(self._scene_list)):
            self._scene_list[i].push_representation(scene_json)

        return scene_json