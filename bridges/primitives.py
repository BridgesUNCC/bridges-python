import webcolors


class Primitives:

    def __init__(self, type: str, name: str, position: list = None):
        self._type = type
        self._name = name
        self._position = position
        self._transform = []
        self._color = "red"
        self._object_json = {
            'name': self._name,
            'position': self._position,
            'transform': self._transform,
            'color': self._color
        }

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, pos:list):
        self._position = pos
        self._object_json['position'] = self._position

    @property
    def transform(self):
        return self._transform

    def set_transform(self, transform:list):
        self._transform = transform
        self._object_json['transform'] = self._transform

    def append_transform(self, transform:list):
        self._transform.append(transform)
        self._object_json['transform'] = self._transform

    def set_color(self, *args, **kwargs) -> None:
        """
        Sets color for a an element or link. Requires either 3 ints 0-255 for RGB and an optional float 0.0-1.0 for alpha or a str of a web color can also key the RGBA values with r, g, b, a or red, green, blue, alpha respectively and col_name for the str
        Args:
            args: int, int, int optional float or str
            kwargs: r/red: int, b/blue: int, g/green: int optional a/alpha: float or col_name: str
        """
        col_name = None
        if args:
            errorcondition = True
            if len(args) == 1 and type(args[0]) == list:
                self._color = [args[0][0]/255, args[0][1]/255, args[0][2]/255, args[0][3]]
                self._object_json['color'] = self._color
                errorcondition=False
            if len(args) == 4 or len(args) == 3:
                self._color = [args[0]/255, args[1]/255, args[2]/255, 1.0]
                if len(args) == 4:
                    self._color = args[3]
                self._object_json['color'] = self._color
                errorcondition = False
            elif len(args) == 1:
                if type(args[0]) is str:
                    col_name = args[0]
                    errorcondition = False
            if errorcondition:
                raise ValueError("To use Color constructor pass 3 RGB values and a float alpha value or a color name or a Color object")
        elif kwargs:
            if 'col_name' in kwargs:
                col_name = kwargs['col_name']

        if col_name is not None:
            try:
                web_color = webcolors.name_to_rgb(col_name)
                self.set_color(web_color.red, web_color.green, web_color.blue)
            except ValueError:
                raise ValueError(col_name + " is not a valid color name")


    def push_representation(self, scene_json):
        scene_json['meshes'].append(self._object_json)