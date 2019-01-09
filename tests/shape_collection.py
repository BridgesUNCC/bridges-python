from bridges.symbol_collection import *
from bridges.bridges import *
from bridges.circle import *
from bridges.polygon import *
from bridges.rectangle import *
from bridges.label import *
from bridges.color import *

def main():
    bridges = Bridges(0, "test", "211416381091")
    bridges.connector.set_server("local")
    bridges.set_title("Symbol Collection")
    bridges.set_description("Some Shapes and Symbols")
    bridges.json_flag = True

    sc = SymbolCollection()
    s1 = Rectangle(50, 50, -25.0, 0.0)
    s1.set_fill_color(Color("green"))
    sc.add_symbol(s1)

    s2 = Circle(25.0, 0.0, 25)
    s2.set_fill_color(Color("green"))
    sc.add_symbol(s2)

    s3 = Polygon()
    s3.add_point(-100,0)
    s3.add_point(100, 0)
    s3.add_point(0, 0)
    s3.add_point(0, -100)
    s3.add_point(0, 100)
    s3.add_point(0, 0)
    s3.set_stroke_color(Color("magenta"))
    sc.add_symbol(s3)

    l = Label()
    l.set_location(0, 25)
    l.set_font_size(12)
    l.set_stroke_width(1.0)
    l.set_label("test label")
    l.set_stroke_color(Color("purple"))
    sc.add_symbol(l)

    bridges.set_data_structure(sc)
    bridges.visualize()

if __name__ == '__main__':
    main()