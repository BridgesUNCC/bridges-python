from bridges import *
from abc import ABC
from bridges.symbol_collection import *
from bridges.rectangle import *
from bridges.label import *
from bridges.polyline import *


class Dictionary(ABC):
    @abstractmethod
    def get(self, key):
        """
        returns the value of node at key
        :param key: key of node
        :return: value of node
        """
        pass

    @abstractmethod
    def set(self, key, value) -> None:
        """
        set node at key with value
        :param key: key of node
        :param value: new value of node
        :return: None
        """
        pass

    @abstractmethod
    def delete(self, key) -> None:
        """
        Deletes the node at the given key
        :param key: key of node
        :return: None
        """
        pass


class HashTableNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable(Dictionary, ABC):

    def __init__(self, capacity=30, load_factor=10):
        self._table = [None] * capacity
        self.capacity = capacity
        self.count = 0
        self.load_factor = load_factor

    def get(self, key):
        """
        returns the value of node at key
        :param key: key of node
        :return: node or None
        """
        index = hash(key) % self.capacity

        node = self._table[index]
        while node is not None:
            if node.key == key:
                break
            node = node.next

        return node

    def set(self, key, value) -> None:
        """
        set node at key with value
        :param key: key of node
        :param value: new value of node
        :return: None
        """

        index = hash(key) % self.capacity
        node = self._table[index]

        new = True
        if node is None:
            self._table[index] = HashTableNode(key, value)
        else:
            if node.key == key:
                node.value = value
                new = False
            else:
                while node.next is not None:
                    if node.next.key == key:
                        node.next.value = value
                        new = False
                        break
                    node = node.next
                if new:
                    node.next = HashTableNode(key, value)

        if new:
            self.count += 1
            if self.count / self.capacity > self.load_factor:
                self._resize(self.capacity * 2)

    def delete(self, key) -> None:
        """
        Deletes the node at the given key
        :param key: key of node
        :return: None
        """
        index = hash(key) % self.capacity

        node = self._table[index]
        if node is not None:
            while node.next is not None:
                if node.next.key == key:
                    if node.next.next is None:
                        node.next = None
                        self.count -= 1
                        break
                    else:
                        node.next = node.next.next
                        self.count -= 1
                        break
                node = node.next

    def _resize(self, capacity):
        new_table = HashTable(capacity)

        for node in self._table:
            while node is not None:
                new_table.set(node.key, node.value)
                node = node.next

        self.capacity = capacity
        self._table = new_table._table

    def visualize(self, bridges_inst):
        vis = SymbolCollection()

        for index, bucket in enumerate(self._table):
            x = 0
            y = 100 + (self.capacity - index) * 30
            bucket_rect = Rectangle(w=25, h=25, locx=x, locy=y)
            bucket_rect.fill_color = "white"
            vis.add_symbol(bucket_rect)
            bucket_label = Label()
            bucket_label.set_location(x, y)
            bucket_label.font_size = 12
            bucket_label.label = f'{index}'
            vis.add_symbol(bucket_label)
            x += 62.5
            while bucket is not None:
                bucket_rect = Rectangle(w=100, h= 25, locx=x, locy=y)
                bucket_rect.fill_color = "white"
                vis.add_symbol(bucket_rect)
                bucket_label = Label()
                bucket_label.set_location(x, y)
                bucket_label.font_size = 12
                bucket_label.label = f'{bucket.key}: {bucket.value}'
                vis.add_symbol(bucket_label)
                line = Polyline()
                line.add_point(x + 50, y)
                line.add_point(x + 150, y)
                line.add_point(x + 125, y - 12.5)
                line.add_point(x + 150, y)
                line.add_point(x + 125, y + 12.5)
                line.stroke_width = 1
                line.stroke_color = "red"
                vis.add_symbol(line)
                x += 200
                bucket = bucket.next

            bucket_rect = Rectangle(w=100, h=20, locx=x, locy=y)
            bucket_rect.fill_color = "white"
            vis.add_symbol(bucket_rect)
            bucket_label = Label()
            bucket_label.set_location(x, y)
            bucket_label.font_size = 12
            bucket_label.label = "∅"
            vis.add_symbol(bucket_label)

        bridges_inst.set_data_structure(vis)
        bridges_inst.visualize()


class BSTDictionary(Dictionary, ABC):

    def __init__(self):
        self.root = None

    def get(self, key):
        """
        returns the value of node at key
        :param key: key of node
        :return: BSTNode at key
        """
        found_node = self._find(self.root, key)
        return found_node

    def _find(self, root, key):
        if(root is not None):
            if(root.key == key):
                return root
            elif(key < root.key):
                return self._find(root.left, key)
            elif(key > root.key):
                return self._find(root.right, key)
        else:
            return None

    def set(self, key, value):
        """
        set node at key with value
        :param key: key of node
        :param value: new value of node
        :return: None
        """
        self.root = self._insert(self.root, key, value)

    def _insert(self, root, key, value):
        """
        private def to insert dict key and value into the BST
        :param root: the root of the bst
        :param key: the key in the dict for the bst node
        :param value: the value in the dict for the bst node
        :return: the root
        """
        if(root is None):
            el = BSTElement(key = key, e = value)
            el.label = value
            return el
        elif(key == root.key):
            root.value = value
            root.label = value
        elif(key < root.key):
            root.left = self._insert(root.left, key, value)
        else:
            root.right = self._insert(root.right, key, value)

        return root



    def delete(self, key) -> None:
        """
        Deletes the node at the given key
        :param key: key of node
        :return: None
        """
        pass


class MyHeapElement(BinTreeElement):
    k = None
    count_left = 0
    count_right = 0


class MyHeap(object):
    def __init__(self):
        self.root = None

    def _insert_helper(self, lroot, k, v):
        if lroot == None:
            lroot = MyHeapElement()
            lroot.k = k
            lroot.value = v
            return lroot

        if k < lroot.k:
            tempk = k
            k = lroot.k
            lroot.k = tempk

            tempv = v
            v = lroot.value
            lroot.value = tempv

        if lroot.count_left < lroot.count_right:
            lroot.count_left += 1
            lroot.left = self._insert_helper(lroot.left, k, v)
        else:
            lroot.count_right += 1
            lroot.right = self._insert_helper(lroot.right, k, v)

        return lroot

    def insert(self, k, v):
        self.root = self._insert_helper(self.root, k, v)

    def _pop_helper(self, lroot):
        lc = lroot.left
        rc = lroot.right

        if lroot.count_right == 0:
            lroot.k = lc.k
            lroot.value = lc.value
            lroot.count_left -= 1

            if lroot.count_left == 0:
                lroot.left = None
            else:
                self._pop_helper(lc)

            return

        if lroot.count_left == 0:
            lroot.k = rc.k
            lroot.value = rc.value
            lroot.count_right -= 1

            if lroot.count_right == 0:
                lroot.right = None
            else:
                self._pop_helper(rc)

            return

        if lc.k < rc.k:
            lroot.k = lc.k
            lroot.value = lc.value
            lroot.count_left -= 1

            if lroot.count_left == 0:
                lroot.left = None
            else:
                self._pop_helper(lc)
        else:
            lroot.k = rc.k
            lroot.value = rc.value
            lroot.count_right -= 1

            if lroot.count_right == 0:
                lroot.right = None
            else:
                self._pop_helper(rc)

    def pop(self):
        if self.root.count_left == 0 and self.root.count_right == 0:
            self.root = None

        self._pop_helper(self.root)

    def size(self):
        if self.root == None:
            return 0
        else:
            return 1 + self.root.count_left + self.root.count_right

    def update_labels(self):
        if self.root != None:
            self._update_labels_helper(self.root)

    def _update_labels_helper(self, lroot):
        lroot.label = str(lroot.k) + ", " + str(lroot.value)

        if lroot.left:
            self._update_labels_helper(lroot.left)

        if lroot.right:
            self._update_labels_helper(lroot.right)


def split_lyrics(lyrics):
    return lyrics.split(" ")


def main():
    import os
    bridges = Bridges(300, "test", "137842425086")
    # Initialize bridges with your credentials
    # bridges = Bridges(208, "BRIDGES_USER_ID", "BRIDGES_API_KEY")
    bridges.connector.set_server("clone")

    # Set assignment details
    bridges.set_title("Priority Queue Book")
    bridges.set_description("MiniHeap represented as a Binary Tree.")

    shksp_list = get_shakespeare_data("poems", True)
    pol = shksp_list[1]

    words = split_lyrics(pol.text)

    count = {}
    for w in words:
        if w in count.keys():
            count[w] += 1
        else:
            count[w] = 1

    print(count)

    my_dictionary = HashTable()
    for w in words:
        node = my_dictionary.get(w)
        if node is None:
            my_dictionary.set(w, 1)
        else:
            my_dictionary.set(w, node.value + 1)

    bst_dictionary = BSTDictionary()
    for w in words:
        node = bst_dictionary.get(w)
        if node is None:
            bst_dictionary.set(w, 1)
        else:
            bst_dictionary.set(w, node.value + 1)

    my_dictionary.visualize(bridges)

    my_heap = MyHeap()
    for k, v in count.items():
        my_heap.insert(v, k)

    my_heap.update_labels()

    bridges.set_data_structure(my_heap.root)
    bridges.visualize()

    while my_heap.size() > 10:
        my_heap.pop()

    bridges.set_data_structure(my_heap.root)
    bridges.visualize()

    bridges.set_data_structure(bst_dictionary.root)
    bridges.visualize()


if __name__ == '__main__':
    main()