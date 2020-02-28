import linked_list


# [amotz]
# hashtable partial implementation int and string are supported
# the hashtable support collisions but automatically growing array but still not shrinking of the array

def compute_hash_code(key):
    if type(key) == str:
        list_of_ascii_code_chars = [ord(c) for c in key]  # computing the unicode of chars and putting them in a list
        hash_code = sum(list_of_ascii_code_chars)
        return hash_code
    elif type(key) == int:
        return key
    else:
        assert False, "only int and string are supported"


def test_compute_hash_code():
    assert compute_hash_code('abc') == 294
    assert compute_hash_code(3) == 3


test_compute_hash_code()


class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Hashtable:

    def __init__(self):
        self.backing_array = [None] * 10
        self.size = 0

    def put(self, key, value):
        hash_code = compute_hash_code(key)
        index = hash_code % len(self.backing_array)
        if self.backing_array[index] is None:
            hashtable_element = KeyValuePair(key, value)
            self.backing_array[index] = hashtable_element
            self.size += 1
        elif type(self.backing_array[index]) == KeyValuePair:
            if self.backing_array[index].key == key:
                self.backing_array[index].value = value
            else:
                hashtable_element = KeyValuePair(key, value)
                b_a_linked_list = linked_list.LinkedList()
                b_a_linked_list.add_link_at_end(self.backing_array[index])
                b_a_linked_list.add_link_at_end(hashtable_element)
                self.backing_array[index] = b_a_linked_list
                self.size += 1
        else:
            assert type(self.backing_array[index]) == linked_list.LinkedList
            assert self.backing_array[index].size() >= 2
            is_key_found = False
            for i in self.backing_array[index]:
                if i.key == key:
                    is_key_found = True
                    i.value = value
            if not is_key_found:
                hashtable_element = KeyValuePair(key, value)
                self.backing_array[index].add_link_at_end(hashtable_element)
                self.size += 1
        self.resize()

    def get(self, key):
        hash_code = compute_hash_code(key)
        index = hash_code % len(self.backing_array)
        if self.backing_array[index] is None:
            return None
        elif type(self.backing_array[index]) == KeyValuePair:
            if self.backing_array[index].key == key:
                return self.backing_array[index].value
            else:
                return None
        else:
            assert type(self.backing_array[index]) == linked_list.LinkedList
            assert self.backing_array[index].size() >= 2
            for i in self.backing_array[index]:
                if i.key == key:
                    return i.value
            return None

            # [amotz]
            # in my hashtable_representation below
            # i chose to use a representation of hashtable in which
            # the empty buckets of the backing array are represented with the index of the backing array
            # and the the buckets that are not empty are represnted with python lists of key value pairs

    def hashtable_representation(self):
        representation = []
        for index in range(len(self.backing_array)):
            if self.backing_array[index] is None:
                representation.append(index)
            elif type(self.backing_array[index]) == KeyValuePair:
                representation.append(index)
                representation.append([self.backing_array[index].key, self.backing_array[index].value])
            else:
                assert type(self.backing_array[index]) == linked_list.LinkedList
                assert self.backing_array[index].size() >= 2
                representation.append(index)
                for i in self.backing_array[index]:
                    representation.append([i.key, i.value])
        return representation

    # [amotz]
    # returns true if the key was removed and false otherwise
    def remove(self, key):
        hash_code = compute_hash_code(key)
        index = hash_code % len(self.backing_array)
        if type(self.backing_array[index]) == KeyValuePair:
            if self.backing_array[index].key == key:
                self.backing_array[index] = None
                self.size -= 1
                return True
            else:
                return False
        elif type(self.backing_array[index]) == linked_list.LinkedList:
            assert self.backing_array[index].size() >= 2
            if self.backing_array[index].size() > 2:
                for i in self.backing_array[index]:
                    if i.key == key:
                        self.backing_array[index].remove(i)
                        self.size -= 1
                        return True
                return False
            else:
                for i in self.backing_array[index]:
                    if i.key == key:
                        self.backing_array[index].remove(i)
                        key = self.backing_array[index].get_head_link().key
                        value = self.backing_array[index].get_head_link().value
                        hashtable_element = KeyValuePair(key, value)
                        self.backing_array[index] = hashtable_element
                        self.size -= 1
                        return True
                return False
        else:
            assert self.backing_array[index] is None
            return False

    # [amotz]
    # the name size1 is because the name size conflicts with the member variable self.size
    def size1(self):
        return self.size

    def resize(self):
        if self.size1() > 0.3 * len(self.backing_array):
            new_hash = Hashtable()
            new_hash.backing_array = [None] * len(self.backing_array) * 2
            for i in range(len(self.backing_array)):
                if self.backing_array[i] is None:
                    pass
                elif type(self.backing_array[i]) == KeyValuePair:
                    new_hash.put(self.backing_array[i].key, self.backing_array[i].value)
                else:
                    assert type(self.backing_array[i]) == linked_list.LinkedList
                    for ii in self.backing_array[i]:
                        new_hash.put(ii.key, ii.value)
            self.backing_array = new_hash.backing_array
            assert self.size == new_hash.size
    # TODO a code for shrinking the array


def test_Hashtable():
    hashtable = Hashtable()
    # testing a key that i didn't insert is not in the hashtable
    # i also test the size1 method  from now on in many places in the code
    assert hashtable.get(1) is None
    assert hashtable.size1() == 0
    # testing basic put and get
    hashtable.put(1, 1)
    assert hashtable.size1() == 1
    assert hashtable.get(1) == 1
    # a key that its index calculates to the same bucket but is not in the hashtable
    # (the bucket contains a KeyValuePair object)
    assert (compute_hash_code(11) % len(hashtable.backing_array)
            == compute_hash_code(1) % len(hashtable.backing_array))
    assert type(hashtable.backing_array[1]) == KeyValuePair
    assert hashtable.get(11) is None
    assert hashtable.size1() == 1

    # testing hash collision and resizing of the backing array
    assert "abc" != "acb"
    assert compute_hash_code("abc") == compute_hash_code("acb")
    hashtable.put('abc', 2)
    assert hashtable.size1() == 2
    hashtable.put('cab', 3)
    assert hashtable.size1() == 3
    assert hashtable.get('abc') == 2
    assert hashtable.get('cab') == 3
    # testing a key that will  be stored in the same bucket as the keys above but is not in the hashtable
    # (this time the bucket contains a linked list)
    assert type(hashtable.backing_array[4]) == linked_list.LinkedList
    assert hashtable.get('bac') is None
    assert hashtable.size1() == 3
    # showing that the index of the bucket that stores 'abc' and 'bac' is 4 for later testing
    assert (compute_hash_code("abc") % len(hashtable.backing_array)
            == compute_hash_code("acb") % len(hashtable.backing_array) == 4)
    # i add another key that will be stored in the same bucket as 'abc and 'bac' to test the put method
    # when the backing array bucket has a linked list - test for second collision
    hashtable.put('acb', 1)
    assert hashtable.size1() == 4
    # testing resizing of the backing_array
    # since the number of elements are now more then 0.3*(length of backing array)
    assert len(hashtable.backing_array) == 20
    assert hashtable.get('acb') == 1
    # testing that putting the third key value pair in the same bucket didn't
    # change the other key value pairs in the bucket of index 4
    assert hashtable.get('abc') == 2
    assert hashtable.get('cab') == 3

    # putting a value in a key that is already in the hashtable in a bucket that contains
    # a KeyValuePair object
    # testing update to a key
    assert hashtable.get(1) is not None
    assert type(hashtable.backing_array[1]) == KeyValuePair
    hashtable.put(1, 2)
    assert hashtable.get(1) == 2
    assert hashtable.size1() == 4
    # putting a value in a key that is already in the hashtable and is in a linked list of KeyValuePair objects
    # testing update to a key
    assert hashtable.get('abc') is not None
    assert type(hashtable.backing_array[14]) == linked_list.LinkedList
    hashtable.put('abc', 8)
    assert hashtable.get('abc') == 8
    assert hashtable.size1() == 4

    # testing hashtable_representation method and resizing of backing array
    assert hashtable.hashtable_representation() == [0, 1, [1, 2], 2, 3, 4, 5,
                                                    6, 7, 8, 9, 10, 11, 12, 13, 14, ['abc', 8], ['cab', 3], ['acb', 1],
                                                    15,
                                                    16, 17, 18, 19]
    # testing remove method
    # single KeyValuePair in backing array location
    assert type(hashtable.backing_array[1]) == KeyValuePair
    assert hashtable.remove(1)
    # assert len(hashtable.backing_array) == 10
    assert hashtable.get(1) is None
    assert hashtable.size1() == 3
    # more then two KeyValuePairs in backing array location
    assert type(hashtable.backing_array[14]) == linked_list.LinkedList
    assert hashtable.remove('cab')
    assert hashtable.get('cab') is None
    assert hashtable.size1() == 2
    # test that all the key value pairs in the hashtable are still in the right places.
    # also that resizing of backing array is correct
    assert hashtable.hashtable_representation() == [0, 1, 2, 3, 4, 5,
                                                    6, 7, 8, 9, 10, 11, 12, 13, 14, ['abc', 8], ['acb', 1], 15, 16, 17,
                                                    18, 19]

    assert not hashtable.remove(2)
    assert hashtable.size1() == 2
    # test of removing a key that is not in the hashtable
    assert hashtable.get(2) is None
    # test that all the key value pairs in the hashtable are still in the right places
    assert hashtable.hashtable_representation() == [0, 1, 2, 3, 4, 5,
                                                    6, 7, 8, 9, 10, 11, 12, 13, 14, ['abc', 8], ['acb', 1], 15, 16, 17,
                                                    18,
                                                    19]

    # removing a key in a bucket with exactly two keys.
    # checking consistence type of objects in a bucket with two KeyValuePair objects
    # assert len(hashtable.backing_array) == 20
    assert hashtable.remove('acb')
    assert hashtable.size1() == 1
    # assert len(hashtable.backing_array) == 10
    assert type(hashtable.backing_array[14]) == KeyValuePair
    assert hashtable.remove('abc')
    assert hashtable.size1() == 0
    assert hashtable.backing_array[14] is None


test_Hashtable()

# TODO test for many randomly generated numbers