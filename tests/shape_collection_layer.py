from bridges import *
from bridges.symbol_group import *
from bridges.text import *


def main():

    bridges = Bridges(1, "test", "988181220044")

    bridges.set_title("Symbol Collection")
    bridges.set_description("Red Square, green circle, magenta horizontal and vertical lines, "
                            "and a test label with a purple outline")

    bridges.set_server_url("local")
    bridges.set_coord_system_type('equirectangular')
    bridges.set_map_overlay(True)

    sc = SymbolCollection()

    sg = SymbolGroup()

    s1 = Rectangle(locx=-25.0, locy=0.0, w=50.0, h=50.0)
    s1.fill_color = "red"
    s1.layer = 1
    sg.add_symbol(s1)

    s2 = Circle(locx=25.0, locy=0.0, r=25.0)
    s2.fill_color = "green"
    s2.layer = 2
    sg.add_symbol(s2)

    t = Text()
    t.text = "group above with rectangle over circle"
    t.font_size = 10
    t.stroke_width = 1
    t.stroke_color = "black"
    sg.add_symbol(t)

    sg.layer = 1
    sc.add_symbol(sg)

    sg = SymbolGroup()

    s1 = Rectangle(locx=-25.0, locy=0.0, w=50.0, h=50.0)
    s1.fill_color = "yellow"
    s1.layer = 4
    sg.add_symbol(s1)

    s2 = Circle(locx=25.0, locy=0.0, r=25.0)
    s2.fill_color = "blue"
    s2.layer = 3
    sg.add_symbol(s2)

    t = Text()
    t.text = "group below with circle over rectangle"
    t.font_size = 10
    t.stroke_width = 1
    t.stroke_color = "black"
    sg.add_symbol(t)

    sg.layer = 2
    sg.translate(30.0,30.0)
    sc.add_symbol(sg)

    bridges.set_data_structure(sc)

    bridges.set_visualize_JSON(True)
    bridges.visualize()

if __name__ == "__main__":
    main()

