from data_structures import linked_list
import random
import string


# [amotz]
# hashtable partial implementation int and string are supported
# the hashtable support collisions and automatically growing and shrinking of the array

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

    def __init__(self, do_resize=True):
        self.backing_array = [None] * 10
        self.size1 = 0
        self.do_resize = do_resize

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
                b_a_linked_list.add_tail(self.backing_array[index])
                b_a_linked_list.add_tail(hashtable_element)
                self.backing_array[index] = b_a_linked_list
                self.size1 += 1
        else:
            assert type(self.backing_array[index]) == linked_list.LinkedList
            assert self.backing_array[index].compute_size() >= 2
            is_key_found = False
            for i in self.backing_array[index]:
                if i.key == key:
                    is_key_found = True
                    i.value = value
            if not is_key_found:
                hashtable_element = KeyValuePair(key, value)
                self.backing_array[index].add_tail(hashtable_element)
                self.size1 += 1
            self.check_resize()

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
            assert self.backing_array[index].compute_size() >= 2
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
                assert self.backing_array[index].compute_size() >= 2
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
                self.check_resize()
                return True
            else:
                return False
        elif type(self.backing_array[index]) == linked_list.LinkedList:
            assert self.backing_array[index].compute_size() >= 2
            if self.backing_array[index].compute_size() > 2:
                for i in self.backing_array[index]:
                    if i.key == key:
                        self.backing_array[index].remove(i)
                        self.size1 -= 1
                        self.check_resize()
                        return True
                return False
            else:
                for i in self.backing_array[index]:
                    if i.key == key:
                        self.backing_array[index].remove(i)
                        key = self.backing_array[index].get_head_value().key
                        value = self.backing_array[index].get_head_value().value
                        hashtable_element = KeyValuePair(key, value)
                        self.backing_array[index] = hashtable_element
                        self.size1 -= 1
                        self.check_resize()
                        return True
                return False
        else:
            assert self.backing_array[index] is None
            return False

    # [amotz]
    # the name size1 is because the name size conflicts with the member variable self.size

    def size(self):
        return self.size1

    # this function check_resize the hashtable if needed
    def check_resize(self):
        if not self.do_resize:
            return
        if self.size() > 0.3 * len(self.backing_array):
            temp_hash = Hashtable(False)
            temp_hash.backing_array = [None] * len(self.backing_array) * 2
            for i in self:
                temp_hash.put(i.key, i.value)
            assert self.size1 == temp_hash.size1
            self.backing_array = temp_hash.backing_array
        if 3 <= self.size() <= 0.15 * len(self.backing_array):
            temp_hash = Hashtable(False)
            temp_hash.backing_array = [None] * int(len(self.backing_array) / 2)
            for i in self:
                temp_hash.put(i.key, i.value)
            assert self.size1 == temp_hash.size1
            self.backing_array = temp_hash.backing_array

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

    def __init__(self, hash):
        # [aviv] It may be that a real Python programmer would know to hint that these members (variables and methods)
        # are private by using "__", or something like that. Sorry :(

        self.hash = hash
        self.index = 0
        self.list_iter = None
        self.current = None
        self.advance()

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            out = self.current
            self.advance()
            return out

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
                    assert element.compute_size() >= 1, "This code relies on not having an empty list in the backing array"
                    self.index = self.index + 1
                    self.list_iter = iter(element)
                    # Call advance to get current from the list iterator we just found.
                    self.advance()
                    return
            self.current = None
