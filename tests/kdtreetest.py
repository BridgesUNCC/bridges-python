from bridges import *
from bridges.kd_tree_element import *

bridges = Bridges(0, "test", "211416381091")
bridges.connector.set_server("local")
bridges.json_flag = True

bridges.set_title("a KD Tree Example")

t0 = KDTreeElement(key = 50, dim = 0)
t1 = KDTreeElement(key = 25, dim = 1)
t2 = KDTreeElement(key = 75, dim = 1)
t3 = KDTreeElement(key = 20, dim = 0)
t4 = KDTreeElement(key = 30, dim = 0)
t5 = KDTreeElement(key = 60, dim = 0)
t6 = KDTreeElement(key = 80, dim = 0)

t0.set_left(t1)
t0.set_right(t2)
t1.set_left(t3)
t1.set_label("X")
t1.set_right(t4)
t2.set_left(t5)
t2.set_left(t6)

t0.set_label("X")
t1.set_label("Y")
t2.set_label("Y")
t3.set_label("X")
t4.set_label("X")
t5.set_label("X")
t6.set_label("X")

t0.get_visualizer().set_color("red")

t1.get_visualizer().set_color("orange")
t4.get_visualizer().set_color("orange")
t5.get_visualizer().set_color("orange")
t6.get_visualizer().set_color("orange")

bridges.set_data_structure(t0)
bridges.visualize()