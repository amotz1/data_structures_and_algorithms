import random


class _Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root_node = None

    def _add_node(self, current_node, value):
        if current_node is None:
            current_node = _Node(value)
            return current_node
        if value > current_node.value:
            current_node.right = self._add_node(current_node.right, value)
        else:
            current_node.left = self._add_node(current_node.left, value)
        return current_node

    def add_node(self, value):
        self.root_node = self._add_node(self.root_node, value)

    def _find(self, current_node, value):
        if current_node is None:
            return False
        elif value == current_node.value:
            return True
        elif value > current_node.value:
            returned_value = self._find(current_node.right, value)
            return returned_value
        else:
            returned_value = self._find(current_node.left, value)
            return returned_value

    def find(self, value):
        returned_value = self._find(self.root_node, value)
        return returned_value

    def _right_subtree_successor(self, node):
        if node.left is None:
            return node
        else:
            return self._right_subtree_successor(node.left)

    def _remove(self, current_node, value):
        if value > current_node.value:
            current_node.right = self._remove(current_node.right, value)
            # if current_node.right is None:
            #     print(current_node.value)
            # else:
            #     print(current_node.right.value)
            #     print(current_node.value)
            return current_node
        elif value < current_node.value:
            current_node.left = self._remove(current_node.left, value)
            return current_node
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None or current_node.right is None:
                if current_node.left is not None:
                    return current_node.left
                else:
                    return current_node.right
            else:
                successor = self._right_subtree_successor(current_node.right)
                temp_value = successor.value
                self._remove(self.root_node, successor.value)
                current_node.value = temp_value
                return current_node

    def remove(self, value):
        self.root_node = self._remove(self.root_node, value)

    def _check_invariant(self, current):
        if current is not None:
            if current.left is None and current.right is not None:
                assert current.right.value > current.value
                self._check_invariant(current.left)
                self._check_invariant(current.right)
            elif current.right is None and current.left is not None:
                assert current.left.value <= current.value
                self._check_invariant(current.left)
                self._check_invariant(current.right)
            elif current.right is not None and current.left is not None:
                assert current.right.value > current.value
                assert current.left.value <= current.value
                self._check_invariant(current.left)
                self._check_invariant(current.right)
            else:
                self._check_invariant(current.left)
                self._check_invariant(current.right)

    def check_invariant(self):
        self._check_invariant(self.root_node)

    def _traverse(self, current):
        if current is not None:
            if current.left is None and current.right is None:
                print([current.value, ()])
                self._traverse(current.left)
                self._traverse(current.right)
            elif current.left is not None and current.right is None:
                print([current.value, current.left.value])
                self._traverse(current.left)
                self._traverse(current.right)
            elif current.right is not None and current.left is None:
                print([current.value, current.right.value])
                self._traverse(current.left)
                self._traverse(current.right)
            else:
                print([current.value, (current.left.value, current.right.value)])
                self._traverse(current.left)
                self._traverse(current.right)

    def traverse(self):
        print("the root node is ", self.root_node.value)
        self._traverse(self.root_node)


# [amotz] until now its all tested from here it is fragmented code that is not working and not worth reading yet,
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
    my_tree.add_node(11)
    my_tree.add_node(29)
    my_tree.add_node(38)
    my_tree.add_node(25)
    my_tree.add_node(31)
    my_tree.add_node(34)
    my_tree.add_node(9)
    my_tree.traverse()
    my_tree.check_invariant()

    assert my_tree.find(38)  # testing find method on a value that is in the list
    assert not my_tree.find(115)  # testing find method on a value that is not in the list
    my_tree.remove(76)
    my_tree.check_invariant()
    my_tree.remove(56)
    my_tree.check_invariant()
    assert not my_tree.find(76)  # testing removing a node without children
    assert not my_tree.find(56)  # testing removing a node with one left child
    my_tree.remove(24)
    my_tree.check_invariant()
    assert not my_tree.find(24)  # testing removing a node with two children
    my_tree.remove(29)
    my_tree.check_invariant()
    assert not my_tree.find(29)  # testing removing a node with one right child

    # testing that all the right connections are still in place in the my_tree
    my_tree.check_invariant()


def big_tree():
    my_tree = BinaryTree()
    my_list = []
    for i in range(100):
        random_number = random.randrange(20000)
        my_list.append(random_number)
        my_tree.add_node(random_number)
        my_tree.find(random_number)
        my_tree.check_invariant()
    for i in my_list:
        assert my_tree.find(i)
        while my_tree.find(i) is True:
            my_tree.remove(i)
        assert not my_tree.find(i)


test_Binary_Tree()
big_tree()

#    print(my_tree.tree_size)


#   my_tree.__iter__()
#   my_tree.__next__() == 24
#   my_tree.__next__() == 76


# test_Binary_Tree()
