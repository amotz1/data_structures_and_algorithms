import linked_list
import random
import string


# [amotz]
# hashtable partial implementation int and string are supported
# the hashtable support collisions but automatically growing array but still not shrinking of the array

# TODO: Use the new HashtableIterator in the code.

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


def generate_random_number():
    number = random.randrange(100000)
    return number


def generate_random_string():
    # the line below create 100 random characters and join them up.
    # then it is putting the result in string1
    string1 = ''.join(random.choice(string.ascii_lowercase) for x in range(100))
    return string1


class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Hashtable:

    def __init__(self):
        self.backing_array = [None] * 10
        self.size1 = 0

    def put(self, key, value):
        hash_code = compute_hash_code(key)
        index = hash_code % len(self.backing_array)
        if self.backing_array[index] is None:
            hashtable_element = KeyValuePair(key, value)
            self.backing_array[index] = hashtable_element
            self.size1 += 1
        elif type(self.backing_array[index]) == KeyValuePair:
            if self.backing_array[index].key == key:
                self.backing_array[index].value = value
            else:
                hashtable_element = KeyValuePair(key, value)
                b_a_linked_list = linked_list.LinkedList()
                b_a_linked_list.add_link_at_end(self.backing_array[index])
                b_a_linked_list.add_link_at_end(hashtable_element)
                self.backing_array[index] = b_a_linked_list
                self.size1 += 1
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
                self.size1 += 1
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
                self.size1 -= 1
                self.resize()
                return True
            else:
                return False
        elif type(self.backing_array[index]) == linked_list.LinkedList:
            assert self.backing_array[index].size() >= 2
            if self.backing_array[index].size() > 2:
                for i in self.backing_array[index]:
                    if i.key == key:
                        self.backing_array[index].remove(i)
                        self.size1 -= 1
                        self.resize()
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
                        self.size1 -= 1
                        self.resize()
                        return True
                return False
        else:
            assert self.backing_array[index] is None
            return False

    # [amotz]
    # the name size1 is because the name size conflicts with the member variable self.size

    def size(self):
        return self.size1

    def resize(self):
        if self.size() > 0.3 * len(self.backing_array):
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
            assert self.size1 == new_hash.size1
        # if 3 <= self.size() <= 0.15 * len(self.backing_array):
        #     new_hash = Hashtable()
        #     new_hash.backing_array = [None] * int(len(self.backing_array) / 2)
        #     for i in range(len(self.backing_array)):
        #         if self.backing_array[i] is None:
        #             pass
        #         elif type(self.backing_array[i]) == KeyValuePair:
        #             new_hash.put(self.backing_array[i].key, self.backing_array[i].value)
        #         else:
        #             assert type(self.backing_array[i]) == linked_list.LinkedList
        #             for ii in self.backing_array[i]:
        #                 new_hash.put(ii.key, ii.value)
        #     self.backing_array = new_hash.backing_array
        #     assert self.size1 == new_hash.size1

    # TODO fix the bug of the shrinking code that is now commented

    def __iter__(self):
        return HashtableIterator(self)


# Iterates over the KeyValuePair objects.
#
# Note that if you start iterating over a Hashtable, make modifications to that Hashtable (such as a put or a remove),
# and then continue iterating, strange things could happen and we make no guarantees (the iteration may or may not
# include a newly added KeyValuePair, we may have resized the hashtable and you might get repeats, we may have downsized
# the backing array and crash, who knows...).
#
# ([aviv]: I'm no Python expert, but it looks like Python dictionaries support iterating over just the keys or over
# (key, value) pairs. This just supports one of those, and it may be the case that it will look amateurish to a real
# Python programmer.
class HashtableIterator:
    hash = None
    index = 0
    list_iter = None
    current = None

    # [aviv] It may be that a real Python programmer would know to hint that some of these are private by using "__",
    # or something like that. Sorry :(
    def advance(self):
        if self.list_iter is not None:
            try:
                self.current = next(self.list_iter)
            except StopIteration:
                self.list_iter = None
                self.current = None
                self.advance()
        else:
            while self.index < len(self.hash.backing_array):
                element = self.hash.backing_array[self.index]
                if element is None:
                    # An empty spot in the backing array, keep going..
                    self.index = self.index + 1
                    continue
                elif isinstance(element, KeyValuePair):
                    self.index = self.index + 1
                    self.current = element
                    return
                else:
                    assert isinstance(element, linked_list.LinkedList)
                    assert element.size() >= 1, "This code relies on not having an empty list in the backing array"
                    self.index = self.index + 1
                    self.list_iter = iter(element)
                    # Call advance to get current from the list iterator we just found.
                    self.advance()
                    return
            self.current = None

    def __init__(self, hash):
        self.hash = hash
        self.advance()

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            out = self.current
            self.advance()
            return out


def test_Hashtable():
    hashtable = Hashtable()
    # testing a key that i didn't insert is not in the hashtable
    # i also test the size1 method  from now on in many places in the code
    assert hashtable.get(1) is None
    assert hashtable.size() == 0
    # testing basic put and get
    hashtable.put(1, 1)
    assert hashtable.size() == 1
    assert hashtable.get(1) == 1
    # a key that its index calculates to the same bucket but is not in the hashtable
    # (the bucket contains a KeyValuePair object)
    assert (compute_hash_code(11) % len(hashtable.backing_array)
            == compute_hash_code(1) % len(hashtable.backing_array))
    assert type(hashtable.backing_array[1]) == KeyValuePair
    assert hashtable.get(11) is None
    assert hashtable.size() == 1

    # testing hash1 collision and resizing of the backing array
    assert "abc" != "acb"
    assert compute_hash_code("abc") == compute_hash_code("acb")
    hashtable.put('abc', 2)
    assert hashtable.size() == 2
    hashtable.put('cab', 3)
    assert hashtable.size() == 3
    assert hashtable.get('abc') == 2
    assert hashtable.get('cab') == 3
    # testing a key that will  be stored in the same bucket as the keys above but is not in the hashtable
    # (this time the bucket contains a linked list)
    assert type(hashtable.backing_array[4]) == linked_list.LinkedList
    assert hashtable.get('bac') is None
    assert hashtable.size() == 3
    # showing that the index of the bucket that stores 'abc' and 'bac' is 4 for later testing
    assert (compute_hash_code("abc") % len(hashtable.backing_array)
            == compute_hash_code("acb") % len(hashtable.backing_array) == 4)
    # i add another key that will be stored in the same bucket as 'abc and 'bac' to test the put method
    # when the backing array bucket has a linked list - test for second collision
    hashtable.put('acb', 1)
    assert hashtable.size() == 4
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
    assert hashtable.size() == 4
    # putting a value in a key that is already in the hashtable and is in a linked list of KeyValuePair objects
    # testing update to a key
    assert hashtable.get('abc') is not None
    assert type(hashtable.backing_array[14]) == linked_list.LinkedList
    hashtable.put('abc', 8)
    assert hashtable.get('abc') == 8
    assert hashtable.size() == 4

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
    assert hashtable.size() == 3
    # more then two KeyValuePairs in backing array location
    # assert type(hashtable.backing_array[4]) == linked_list.LinkedList
    assert hashtable.remove('cab')
    assert hashtable.get('cab') is None
    assert hashtable.size() == 2
    # test that all the key value pairs in the hashtable are still in the right places.
    # also that resizing of backing array is correct
    # assert hashtable.hashtable_representation() == [0, 1, 2, 3, 4, ['abc', 8], ['acb', 1], 5, 6, 7, 8, 9]

    assert not hashtable.remove(2)
    assert hashtable.size() == 2
    # test of removing a key that is not in the hashtable
    assert hashtable.get(2) is None
    # test that all the key value pairs in the hashtable are still in the right places
    # assert hashtable.hashtable_representation() == [0, 1, 2, 3, 4, ['abc', 8], ['acb', 1], 5,
    #                                                 6, 7, 8, 9]

    # removing a key in a bucket with exactly two keys.
    # checking consistence type of objects in a bucket with two KeyValuePair objects
    # assert len(hashtable.backing_array) == 20
    assert hashtable.remove('acb')
    assert hashtable.size() == 1
    # assert len(hashtable.backing_array) == 10
    # assert type(hashtable.backing_array[4]) == KeyValuePair
    assert hashtable.remove('abc')
    assert hashtable.size() == 0
    assert hashtable.backing_array[4] is None


test_Hashtable()


def test_iterator():
    # Test with a hashtable that has
    # [1]: a regular backing array element containing a simple KeyValuePair
    # [2]: a backing array element containing a LinkedList
    # [3]: another regular backing array element containing a simple KeyValuePair to make sure that we keep iterating
    #      over the array after we've finished iterating over the list.
    # And another 20 random values (for good measure :)
    hashtable = Hashtable()
    hashtable.put(1, "a")
    hashtable.put(2, "b")
    hashtable.put(22, "bb")
    hashtable.put(3, "c")
    assert (hashtable.size() == 4)

    for i in range(0, 20):
        hashtable.put(generate_random_string(), generate_random_string())
    assert (hashtable.size() == 24)

    py_dict = {}
    for keyValue in hashtable:
        py_dict[keyValue.key] = keyValue.value

    assert len(py_dict) == hashtable.size() == 24, \
        'len(py_dict) == {}, hashtable.size() == {}'.format(len(py_dict), hashtable.size())
    assert py_dict.get(1, "a")
    assert py_dict.get(2, "b")
    assert py_dict.get(22, "bb")
    assert py_dict.get(3, "c")


test_iterator()


def create_hash_and_dict():
    hash1 = Hashtable()
    py_dict = {}
    CONST = 1000
    for i in range(CONST):
        rand_num = generate_random_number()
        rand_num_1 = generate_random_number()
        rand_str = generate_random_string()
        rand_str_1 = generate_random_string()
        hash1.put(rand_num, rand_num_1)
        hash1.put(rand_str, rand_str_1)
        py_dict[rand_num] = rand_num_1
        py_dict[rand_str] = rand_str_1
    return hash1, py_dict


def compare_hash_and_dict(hash1, py_dict):
    # checking that every key value pair in hash1 is also in py_dict
    for keyValue in hash1:
        assert isinstance(keyValue, KeyValuePair)
        assert hash1.get(
            keyValue.key) == keyValue.value  # A gratuitous check to verify that our iterator works correctly.
        assert py_dict[keyValue.key] == hash1.get(keyValue.key)

    # checking that every key value pair in py_dict is also in hash1
    for key in py_dict:
        assert py_dict[key] == hash1.get(key)


def test_big_hashtable():
    print("test_big_hashtable in..")
    hash1, py_dict = create_hash_and_dict()
    compare_hash_and_dict(hash1, py_dict)
    print("test_big_hashtable out.")


test_big_hashtable()

# TODO a remove part for the big_hashtable test
