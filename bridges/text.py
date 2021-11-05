from bridges.symbol import *


class Text(Symbol):


    def __init__(self, label = None):
        super(Text, self).__init__()
        if label is not None:
            self._text = label
        else:
            self._text = ""

        self.stroke_width = 1.0

        self._font_size = None
        self._anchor_alignment_lr = None
        self._anchor_alignment_tb = None
        self._locx = 0.0
        self._locy = 0.0

    def get_shape_type(self):
        return "text"

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, t):
        self._text = t

    @property
    def font_size(self):
        return self._font_size

    @font_size.setter
    def font_size(self, s):
        if(s < 0.0):
            raise ValueError("Font size is too small")
        self._font_size = s

    def set_anchor_alignment(self, typeLR, typeTB):
        '''
        Sets the alignment parameters for the text label
        
        @param typeLR valid parameters are "left", "middle", and "right"
        @param typeTB valid parameters are "top", "bottom",  "embottom", "emtop", "middle"

        @return  symbol
        '''
        self._anchor_alignment_lr = typeLR
        self._anchor_alignment_tb = typeTB

    def set_anchor_location(self, x, y):
        self._locx = x
        self._locy = y

    def get_json_representation(self):

        json_builder = super(Text, self).get_json_representation()

        json_builder['anchor-location'] = [self._locx, self._locy]
        json_builder['text'] = self.text

        if self.font_size is not None:
            json_builder['font-size'] =self.font_size
        if self._anchor_alignment_lr is not None:
            json_builder['anchor-alignmentLR'] = self._anchor_alignment_lr
        if self._anchor_alignment_tb is not None:
            json_builder['anchor-alignmentTB'] = self._anchor_alignment_tb

        return json_builder



