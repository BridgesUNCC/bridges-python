from bridges.symbol_collection import *
from bridges.bridges import *
from bridges.circle import *
from bridges.polyline import *
from bridges.polygon import *
from bridges.rectangle import *
from bridges.label import *
from bridges.color import *

def main():
    bridges = Bridges(0, "test", "988181220044")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")
    bridges.set_title("Symbol Collection")
    bridges.set_description("Some Shapes and Symbols")

    sc = SymbolCollection()
    s1 = Rectangle(w=50, h=50, locx=-25.0, locy=0.0)
    s1.fill_color = "green"
    sc.add_symbol(s1)

    s2 = Circle(x=25.0, y=0.0, r=25)
    s2.fill_color = "green"
    sc.add_symbol(s2)

    s3 = Polygon()
    s3.add_point(-25,-10)
    s3.add_point(25, 0)
    s3.stroke_color = "magenta"
    s3.stroke_width = 2.0
    sc.add_symbol(s3)

    s4 = Polyline()
    s4.add_point(-100, 0)
    s4.add_point(100, 0)
    s4.stroke_color = "magenta"
    s4.stroke_width = 2.0
    sc.add_symbol(s4)

    s5 = Polyline()
    s5.add_point(0.0, -100.0)
    s5.add_point(0.0, 100.0)
    s5.stroke_width = 2.0
    sc.add_symbol(s5)

    s6 = Polygon()
    s6.add_point(-30.0, 40.0)
    s6.add_point(30.0, 40.0)
    s6.add_point(0.0, 80.0)
    s6.stroke_color = "cyan"
    s6.fill_color = "yellow"
    s6.stroke_width = 3.0
    sc.add_symbol(s6)

    l = Label()
    l.set_location(0, 25)
    l.font_size = 12
    l.stroke_width = 1.0
    l.label = "test label"
    l.stroke_color = "purple"
    sc.add_symbol(l)

    bridges.set_data_structure(sc)
    bridges.visualize()

if __name__ == '__main__':
    main()