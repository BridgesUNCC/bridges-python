from bridges.named_color import *
from bridges.named_symbol import *

class GameCell:
    """
    This class is used to represent cells in GameGrids in BRIDGES.
    Each cell has a foreground color, background color, and symbol.
    @sa  Refer to the Game tutorial at 
    
    https://bridgesuncc.github.io/tutorials/NonBlockingGame.html
    
    @author David Burlinson, Matthew McQuaigue
    @date 9/06/18
    """

    def __init__(self, **kwargs):
        """
        Constructor for the cell of a gamegrid
        Kwargs:
            0: background color from enum named_colors
            1: foreground color from enum named_colors
            2: the symbol in the cell from named_symbols
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
            self._fg = NamedColor.cyan
        if 'symbol' in kwargs:
            self._symbol = kwargs['symbol']
        else:
            self._symbol = NamedSymbol.none

    @property
    def bg(self):
        """
        Getter for the background color
        Returns:
            color: background color
        """
        return self._bg

    @bg.setter
    def bg(self, color):
        """
        Setter for the background color
        Args:
            color: color to be set
        Returns:
            None
        """
        if type(color) == NamedColor:
            self._bg = color
        else:
            self._bg = NamedColor[color]

    @property
    def fg(self):
        """
        Getter for the foreground color
        Returns:
            color: the foreground color
        """
        return self._fg

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
            self._fg = NamedColor[color]

    @property
    def symbol(self):
        """
        Getter for the symbol in the cell
        Returns:
            symbol
        """
        return self._symbol

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
            self._symbol = NamedSymbol[s]

    def get_bg_byte(self):
        """
        Gets the background color as a byte.
        Returns:
            background color as byte (index of value in NamedColor)
        """
        return bytes([self._bg.value])

    def get_fg_byte(self):
        """
        Gets the foreground color as a byte.
        Returns:
            foreground color as byte (index of value in NamedColor)
        """
        return bytes([self._fg.value])

    def get_symbol_byte(self):
        """
        Gets the symbol as a byte.
        Returns:
             symbol as byte
        """
        return bytes([self._symbol.value])


