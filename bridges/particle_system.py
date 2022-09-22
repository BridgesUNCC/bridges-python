
class Particle_System:

    def __init__(self, name, position, num_of_particles):
        self._name = name
        self._position = position
        self._num_of_particles = num_of_particles
        self._velocity = 0
        self._object_json = {
            'name': self._name,
            'position': self._position,
            'particle count': self._num_of_particles,
            'valocity': self._velocity
        }


    def push_representation(self, scene_json):
        scene_json['meshes'].append(self._object_json)