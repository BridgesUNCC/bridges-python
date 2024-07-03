from bridges import *
from bridges.symbol_group import *
from bridges.text import *


def anchor_test(alignLR, alignTB):

    group = SymbolGroup()

    xaxis = Polyline()
    xaxis.add_point(-50.0, 0.0)
    xaxis.add_point(50.0, 0.0)
    xaxis.stroke_color = "black"
    xaxis.stroke_width = 1.0
    group.add_symbol(xaxis)

    yaxis = Polyline()
    yaxis.add_point(0.0, -50.0)
    yaxis.add_point(0.0, 50.0)
    yaxis.stroke_color = "black"
    yaxis.stroke_width = 1.0
    group.add_symbol(yaxis)

    t = Text()
    t.font_size = 10.0
    t.stroke_width = 1.0
    t.text = "Something"
    t.stroke_color = "black"
    t.set_anchor_alignment(alignLR, alignTB)
    group.add_symbol(t)

    t2 = Text()
    t2.font_size = 10.0
    t2.stroke_width = 1.0
    t2.text = alignLR + " " + alignTB
    t2.stroke_color = "black"
    t2.set_anchor_location(0.0, -50.0)
    t2.set_anchor_alignment("middle", "top")
    group.add_symbol(t2)

    return group

def main():
    bridges = Bridges(1, "test", "137842425086")

    bridges.set_title("Symbol Collection")

    bridges.set_server_url("clone")

    sc = SymbolCollection()

    sc.setviewport(-100, 400, -100, 700)

    group = anchor_test("left", "bottom")
    group.translate(0,0)
    sc.add_symbol(group)

    group = anchor_test("middle", "bottom")
    group.translate(120, 0)
    sc.add_symbol(group)

    group = anchor_test("right", "bottom")
    group.translate(240, 0)
    sc.add_symbol(group)

    group = anchor_test("left", "embottom")
    group.translate(0, 150)
    sc.add_symbol(group)

    group = anchor_test("middle", "embottom")
    group.translate(120, 150)
    sc.add_symbol(group)

    group = anchor_test("right", "embottom")
    group.translate(240, 150)
    sc.add_symbol(group)

    group = anchor_test("left", "emtop")
    group.translate(0, 450)
    sc.add_symbol(group)

    group = anchor_test("middle", "emtop")
    group.translate(120, 450)
    sc.add_symbol(group)

    group = anchor_test("right", "emtop")
    group.translate(240, 450)
    sc.add_symbol(group)

    group = anchor_test("left", "top")
    group.translate(0, 600)
    sc.add_symbol(group)

    group = anchor_test("middle", "top")
    group.translate(120, 600)
    sc.add_symbol(group)

    group = anchor_test("right", "top")
    group.translate(240, 600)
    sc.add_symbol(group)

    bridges.set_data_structure(sc)

    bridges.set_visualize_JSON(True)
    bridges.visualize()

if __name__ == "__main__":
    main()