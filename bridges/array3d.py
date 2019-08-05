from bridges.array import *


class Array3D(Array):

    def __init__(self, **kwargs):
        super(Array3D, self).__init__()
        if 'dims' in kwargs:
            self.set_size(3, kwargs['dims'])
            self.num_cols = kwargs['dims'][0]
            self.num_rows = kwargs['dims'][1]
            self.num_slices = kwargs['dims'][2]
        elif 'slices' in kwargs and 'rows' in kwargs and 'cols' in kwargs:
            dims = [kwargs['cols'], kwargs['rows'], kwargs['slices']]
            self.set_size(3, dims)
            self.num_cols = kwargs['cols']
            self.num_rows = kwargs['rows']
            self.num_slices = kwargs['slices']
        else:
            self.num_cols = 0
            self.num_rows = 0
            self.num_slices = 0
            self.size = 0