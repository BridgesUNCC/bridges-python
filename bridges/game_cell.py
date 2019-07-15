from bridges.named_color import *
from bridges.named_symbol import *


class GameCell:

    def __init__(self, **kwargs):
        """
        Constructor for the cell of a gamegrid
        Kwargs:
            bg: background color from enum named_colors
            fg: foreground color from enum named_colors
            symbol: the symbol in the cell from named_symbols
        Returns:
              None
        """
        if 'bg' in kwargs:
            self._bg = kwargs['bg']
        else:
            self._bg = NamedColor.black
        if 'fg' in kwargs:
            self._fg = kwargs['fg']
        else:
            self._fg = NamedColor.white
        if 'symbol' in kwargs:
            self._symbol = kwargs['symbol']
        else:
            self._symbol = NamedSymbol.A

    @property
    def bg(self):
        """
        Getter for the background color
        Returns:
            color: background color
        """
        return self._bg.value

    @bg.setter
    def bg(self, color):
        if type(color) == NamedColor:
            self._bg = color
        else:
            self._bg = NamedColor.__getitem__(color)

    @property
    def fg(self):
        """
        Getter for the foreground color
        Returns:
            color: the foreground color
        """
        return self._fg.value

    @fg.setter
    def fg(self, color):
        """
        Setter for the color of the foreground
        Args:
            color: the color to be applied
        Returns:
            None
        """
        if type(color) == NamedColor:
            self._fg = color
        else:
            self._fg = NamedColor.__getitem__(color)

    @property
    def symbol(self):
        """
        Getter for the symbol in the cell
        Returns:
            symbol
        """
        return self._symbol.value

    @symbol.setter
    def symbol(self, s):
        """
        Setter for the symbol in the cell
        Args:
            s: the symbol to be applied
        Returns:
            None
        Raises:
            ValueError: if the int value for the symbol is < 0 or > 255
        """
        if type(s) == NamedSymbol:
            self._symbol = s
        else:
            if s < 0 or s > 255:
                raise ValueError("Symbol " + s + " is invalid; symbols must be specified from the range (0, 255)")
            self._symbol = NamedSymbol.__getitem__(s)

    def get_bg_byte(self):
        return bytes([self._bg.value])

    def get_fg_byte(self):
        return bytes([self._fg.value])

    def get_symbol_byte(self):
        return bytes([self._symbol.value])


