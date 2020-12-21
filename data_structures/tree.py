import random

DEVELOPMENT_MODE = True


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
        elif value < current_node.value:
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

    # removing the first node with the specified value that it finds

    def remove(self, value):
        self.root_node = self._remove(self.root_node, value)

    def _remove(self, current_node, value):
        if value > current_node.value:
            current_node.right = self._remove(current_node.right, value)
            return current_node
        elif value < current_node.value:
            current_node.left = self._remove(current_node.left, value)
            return current_node
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is not None and current_node.right is None:
                return current_node.left
            elif current_node.right is not None and current_node.left is None:
                return current_node.right
            else:
                successor = self._right_subtree_successor(current_node.right)
                temp_value = successor.value
                self._remove(self.root_node, successor.value)
                current_node.value = temp_value
                return current_node

    def is_empty(self):
        if self.root_node is None:
            return True
        else:
            return False

    # assert that left child value is lower then the parent value
    # and that right child value is bigger then the parent value

    def check_invariant(self):
        # type: () -> object
        self._check_invariant(self.root_node)

    def _check_invariant(self, current):
        if current is None:
            return
        if current.left is None and current.right is not None:
            assert current.right.value > current.value, ('failed on: %d > %d' %
                                                         (current.right.value, current.value))
            self._check_invariant(current.left)
            self._check_invariant(current.right)
        elif current.right is None and current.left is not None:
            assert current.left.value <= current.value, ('failed on: %d <= %d' %
                                                         (current.left.value, current.value))
            self._check_invariant(current.left)
            self._check_invariant(current.right)
        elif current.right is not None and current.left is not None:
            assert current.right.value > current.value, ('failed on: %d > %d' %
                                                         (current.right.value, current.value))
            assert current.left.value < current.value, ('failed on: %d < %d' %
                                                        (current.left.value, current.value))
            self._check_invariant(current.left)
            self._check_invariant(current.right)
        else:
            self._check_invariant(current.left)
            self._check_invariant(current.right)

    def traverse(self):
        print("the root node is ", self.root_node.value)
        self._traverse(self.root_node)

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


def create_tree():
    node_values = [35, 24, 56, 76, 11, 29, 38, 25, 31, 34, 9]
    my_tree = BinaryTree()
    for node_value in node_values:
        my_tree.add_node(node_value)
    return my_tree


def test_Binary_Tree():
    my_tree = create_tree()
    my_tree.check_invariant()
    assert my_tree.find(38), 'failed: finding the number(38)'
    assert not my_tree.find(115), 'failed: return False if number is not in the list(115)'
    my_tree.remove(76)
    assert not my_tree.find(76), 'failed: removing a node with no children (76)'
    my_tree.check_invariant()
    my_tree.remove(56)

    assert not my_tree.find(56), 'failed: removing a node with one left child(56)'
    my_tree.remove(24)
    my_tree.check_invariant()
    assert not my_tree.find(24), 'failed: removing a node with two children (24)'
    my_tree.remove(29)
    assert not my_tree.find(29), ' failed: removing a node with one right child (29)'


def test_big_tree():
    my_tree = BinaryTree()

    # the below code first produce a big tree with non-repeating random numbers
    # then it tests if the left child value is smaller then the parent value
    # and the right child is bigger then the parent value in all the nodes in the tree, and then proceed to check
    # the find method and the remove method
    TREE_NUMBERS_RANGE = 20000
    NUMBER_OF_NODES = 10000
    my_list = random.sample(range(TREE_NUMBERS_RANGE), NUMBER_OF_NODES)
    for i in my_list:
        my_tree.add_node(i)
        # testing the find method on every node value in the big tree
        assert my_tree.find(i), 'failed: find a number that is in the tree'
        my_tree.check_invariant()
    for i in my_list:
        my_tree.remove(i)
        my_tree.check_invariant()
    assert my_tree.is_empty(), 'failed: deleting all the nodes in the tree'


test_Binary_Tree()
test_big_tree()

# [amotz] until now its all tested from here it is
# fragmented code that is not working and not worth reading yet,
# its the beginning of the iterator but i am still working on it,
# planning to do it and i am not sure how yet.

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


# test_Binary_Tree()
# test_big_tree()
# test_problem_tree()
#
# #    print(my_tree.tree_size)
#
#
# #   my_tree.__iter__()
# #   my_tree.__next__() == 24
# #   my_tree.__next__() == 76
#
#
