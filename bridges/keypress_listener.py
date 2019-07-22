import abc


class KeyPressListener(abc.ABC):
    @abc.abstractmethod
    def key_press(self, keypress): pass