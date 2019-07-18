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

# removing the first node with the specified value that it finds

    def remove(self, value):
        self.root_node = self._remove(self.root_node, value)

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

    def is_empty(self):
        if self.root_node is None:
            return True
        else:
            return False

    # assert that left child value is lower then the parent value
    # and that right child value is bigger then the parent value

    def check_invariant(self):
        self._check_invariant(self.root_node)

    def _check_invariant(self, current):
        if current is None:
            return
        else:
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
                assert current.left.value <= current.value, ('failed on: %d <= %d' %
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
    # testing find method on a value that is in the list
    assert my_tree.find(38), 'failed finding the number'
    # testing find method on a value that is not in the list
    my_tree.remove(76)
    assert not my_tree.find(115), 'failed: found a number that is not in the tree'
    my_tree.check_invariant()
    my_tree.remove(56)
    my_tree.check_invariant()
    # testing removing a node without children
    assert not my_tree.find(76), ('failed: found a number that is not in the tree'
                                  'so remove function is not working properly')
    # testing removing a node with one left child
    assert not my_tree.find(56), ('failed: found a number that is not in the tree '
                                  'so remove function is not working properly')
    my_tree.remove(24)
    my_tree.check_invariant()
    # testing removing a node with two children
    assert not my_tree.find(24), ('failed: found a number that is not in the tree '
                                  'so remove function is not working properly')
    my_tree.remove(29)
    my_tree.check_invariant()
    # testing removing a node with one right child
    assert not my_tree.find(29), ('failed: found a number that is not in the tree '
                                  'so remove function is not working properly')

    # testing that all the right connections are still in place in the my_tree
    my_tree.check_invariant()


def test_big_tree():
    my_tree = BinaryTree()
    my_list = []
    max_element_value = 200

    # the below code first produce a big tree and then test if the left child value is smaller then the parent value
    # and the right child is bigger then the parent value in all the nodes in the tree, and then proceed to check
    # the find method and the remove method

    for i in range(max_element_value):
        random_number = random.randrange(50000)
        my_list.append(random_number)
        my_tree.add_node(random_number)
        assert my_tree.find(random_number), 'failed: didnt find a number that is in the tree'
        my_tree.check_invariant()
    for i in my_list:
        assert my_tree.find(i), 'failed: didnt find a number that is in the tree'
    for i in my_list:
        while my_tree.find(i) is True:
            my_tree.remove(i)
        assert not my_tree.find(i), ('failed: found a number that is not in the tree '
                                     'so remove function is not working properly')
    assert my_tree.is_empty(), ('failed: the tree is not empty so the remove function '
                                'did not remove all elements so it doesnt function properly')


test_Binary_Tree()
test_big_tree()

#    print(my_tree.tree_size)


#   my_tree.__iter__()
#   my_tree.__next__() == 24
#   my_tree.__next__() == 76


# test_Binary_Tree()
