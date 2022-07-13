from bridges.camera import *

class Scene:

    def __init__(self, camera_props:dict):
        self._scene_list = {}
        self._camera = Camera(camera_props['type'], camera_props['fov'], camera_props['position'])

    def get_data_structure_type(self):
        return 'Scene'

    def add(self, scene_object):
        self._scene_list[scene_object._name] = scene_object

    def get(self, scene_object_name: str):
        return self._scene_list[scene_object_name]

    @property
    def camera(self):
        return self._camera

    @camera.setter
    def camera(self, cam:Camera):
        self._camera = cam

    def get_data_structure_representation(self):
        scene_json = {
            'meshes': [],
            'lights': []
        }
        scene_json['camera'] = self._camera.push_representation(scene_json)
        for i in self._scene_list:
            scene_json['meshes'].append(self._scene_list[i]._object_json)

        return scene_json