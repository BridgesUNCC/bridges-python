from bridges.bst_element import *

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
            n = BSTElement(k, e)
            gb = n.get_value()
            n.set_label(gb.get_text())
            return n
        if rt.get_key() > k:
            rt.set_left(self.insert_help(rt.get_left(), k, e))
        else:
            rt.set_right(self.insert_help(rt.get_right(), k, e))
        return rt

    def remove_help(self, rt, k):
        if rt is None:
            return None
        if rt.get_key() > k:
            rt.set_left(self.remove_help(rt.get_left(), k))
        elif rt.get_key() < k:
            rt.set_right(self.remove_help(rt.get_right(), k))
        else:
            if rt.get_left() is None:
                return rt.get_right()
            elif rt.get_right() is None:
                return rt.get_left()
            else:
                temp = self.get_min(rt.get_right())
                rt.set_value(temp.get_value())
                rt.set_label(temp.get_key())
                rt.set_key(temp.get_key())
                rt.set_right(self.delete_min(rt.get_right()))
        return rt

    def get_min(self, rt):
        if rt.get_left() is None:
            return rt
        else:
            return self.get_min(rt.get_left())

    def delete_min(self, rt):
        if rt.get_left() is None:
            return rt.get_right()
        else:
            rt.set_left(self.delete_min(rt.get_left()))
            return rt




