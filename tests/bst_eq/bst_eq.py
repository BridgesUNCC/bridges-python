from bridges.bridges import *
from bridges.bst_element import *
from bridges.data_src_dependent.data_source import *

class BST:
    def __init__(self):
        self.root = None
        self.node_count = 0

    def get_tree_root(self):
        return self.root

    def clear(self):
        self.root = None
        self.node_count = 0

    def insert(self, k, e):
        self.root = self.insert_help(self.root, k, e)
        self.node_count += 1

    def remove(self, k):
        temp = self.find_help(self.root, k)
        if temp is not None:
            self.root = self.remove_help(self.root, k)
            self.node_count -= 1
        return temp

    def find_help(self, rt, k):
        if rt is None:
            return None
        if rt.get_key() > 0:
            return self.find_help(rt.get_left(), k)
        elif rt.get_key() == 0:
            return rt.get_value()
        else:
            return self.find_help(rt.get_right(), k)

    def insert_help(self, rt, k, e):
        if rt is None:
            n = BSTElement(key=k, e=e)
            eq = n.value
            n.label = eq.get_title() + eq.get_time()
            return n
        if rt.key > k:
            rt.left = self.insert_help(rt.left, k, e)
        else:
            rt.right = self.insert_help(rt.right, k, e)
        return rt

    def remove_help(self, rt, k):
        if rt is None:
            return None
        if rt.key > k:
            rt.left = self.remove_help(rt.get_left(), k)
        elif rt.key < k:
            rt.right = self.remove_help(rt.get_right(), k)
        else:
            if rt.left is None:
                return rt.right
            elif rt.right is None:
                return rt.left
            else:
                temp = self.get_min(rt.right)
                rt.value = temp.value
                rt.label = temp.key
                rt.key = temp.key
                rt.right = self.delete_min(rt.right)
        return rt

    def get_min(self, rt):
        if rt.left is None:
            return rt
        else:
            return self.get_min(rt.left)

    def delete_min(self, rt):
        if rt.left is None:
            return rt.right
        else:
            rt.left = self.delete_min(rt.left)
            return rt

def main():
    # create the Bridges object, set credentials
    bridges = Bridges(0, "test", "988181220044")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")
    bridges.set_title("Recent Earthquakes(USGIS Data)")
    bridges.json_flag = True

    eqlist = get_earthquake_usgs_data(100)
    bst = BST()
    for i in range(len(eqlist)):
        if eqlist[i].get_magnitude() > 2:
            bst.insert(eqlist[i].get_magnitude(), eqlist[i])
            print(bst.node_count)

    bridges.set_data_structure(bst.get_tree_root())
    bridges.visualize()

if __name__ == '__main__':
    main()