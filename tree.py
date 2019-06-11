
count = 0


class _Node:
    def __init__(self, value):
        self.value = value
        self.next_left_value = None
        self.next_right_value = None


class BinaryTree:
    def __init__(self):
        self.root_node = None

    def _add_node(self, current_node, value):
        if current_node is None:
            current_node = _Node(value)
            return current_node
        if value > current_node.value:
            current_node.next_right_value = self._add_node(current_node.next_right_value, value)
        elif value < current_node.value:
            current_node.next_left_value = self._add_node(current_node.next_left_value, value)
        return current_node

    def add_node(self, value):
        self.root_node = self._add_node(self.root_node, value)

    def _find(self, current_node, value):
        if current_node is None:
            return False
        elif value == current_node.value:
            return True
        elif value > current_node.value:
            returned_value = self._find(current_node.next_right_value, value)
            return returned_value
        elif value < current_node.value:
            returned_value = self._find(current_node.next_left_value, value)
            return returned_value

    def find(self, value):
        returned_value = self._find(self.root_node, value)
        return returned_value

    def _remove(self, current_node, value):
        if current_node.value == value:
            if current_node.next_left_value is not None:
                current_node.value = current_node.next_left_value.value
                current_node.next_left_value = None
            elif current_node.next_left_value is None and current_node.next_right_value is None:
                current_node.value is None
            else:
                current_node.value = current_node.next_right_value.value
                current_node.next_right_value = None
        elif value > current_node.value:
            self._remove(current_node.next_right_value, value)
        else:
            self._remove(current_node.next_left_value, value)

    def remove(self, value):
        self._remove(self.root_node, value)

    def _traverse(self, current):
        if current is not None:
            self._traverse(current.next_left_value)
            print(current.value)
            self._traverse(current.next_right_value)

    def traverse(self):
        self._traverse(self.root_node)

#[amotz] until now its all tested from here it is fragmented code that is not working and not worth reading yet,
# its the beginning of the iterator but i am still working on it, planning to do it and i am not sure how yet.

#    def tree_size(self, current_node):
#        if current_node == null:
#            return 0
#        else:
#            return tree_size(current_node.next_left_value) + 1 + tree_size(current_node.next_right_value)

#    class Stack:
#        def __init__(self, tree_size, value):
#            self.value = value
#            self.tree_size = tree_size

#        def push(self, value):
#            my_list = [None] * tree_size
#            self.my_list.push(value)
#            return my_list

#    class _TreeIterator:



def test_Binary_Tree():
    my_tree = BinaryTree()
    my_tree.add_node(35)
    my_tree.add_node(24)
    my_tree.add_node(56)
    my_tree.add_node(76)
    assert my_tree.find(24)
    assert my_tree.find(76)
    assert not my_tree.find(87)
    assert not my_tree.find(1153)
    my_tree.remove(76)
    my_tree.remove(56)
    assert not my_tree.find(56)
    my_tree.remove(35)
    assert not my_tree.find(35)
    assert my_tree.find(76)
#   print(my_tree.tree_size)

    my_tree.traverse()
#   my_tree.__iter__()
#   my_tree.__next__() == 24
#   my_tree.__next__() == 76


test_Binary_Tree()






