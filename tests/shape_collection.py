from bridges.symbol_collection import *
from bridges.bridges import *
from bridges.circle import *
from bridges.label import *
from bridges.polygon import *
from bridges.label import *
from bridges.color import *

bridges = Bridges(0, "test", "")
sc = SymbolCollection()
s2 = Circle(25.0, 0.0, 25)
s2.set_fill_color(Color("green"))
sc.add_symbol(s2)

l = Label()
l.set_location(0, 25)
l.set_font_size(12)
l.set_stroke_width(1.0)
l.set_label("test label")
l.set_stroke_color(Color("purple"))
sc.add_symbol(l)

bridges.set_data_structure(sc)
bridges.visualize()