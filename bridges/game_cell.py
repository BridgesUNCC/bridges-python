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
            self._fg  = NamedColor.white
        if 'symbol' in kwargs:
            self._symbol = kwargs['symbol']
        else:
            self._symbol = NamedSymbol.non

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
        self._bg = color

    @property
    def fg(self):
        """
        Getter for the foreground color
        Returns:
            color: the foreground color
        """
    @fg.setter
    def fg(self, color):
        """
        Setter for the color of the foreground
        Args:
            color: the color to be applied
        Returns:
            None
        """
        self._fg = color

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
        """
        self._symbol = s

    def byte(self):
        bytes([self._symbol])

