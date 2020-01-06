import linked_list


# [amotz]
# hashtable partial implementation int and string are supported
# the hashtable support collisions but not automatically growing array and remove method

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

    def put(self, key, value):
        hash_code = compute_hash_code(key)
        index = hash_code % len(self.backing_array)
        if self.backing_array[index] is None:
            hashtable_element = KeyValuePair(key, value)
            self.backing_array[index] = hashtable_element
        elif type(self.backing_array[index]) == KeyValuePair:
            if self.backing_array[index].key == key:
                self.backing_array[index].value = value
            else:
                hashtable_element = KeyValuePair(key, value)
                b_a_linked_list = linked_list.LinkedList()
                b_a_linked_list.add_link_at_end(self.backing_array[index])
                b_a_linked_list.add_link_at_end(hashtable_element)
                self.backing_array[index] = b_a_linked_list
        else:
            assert type(self.backing_array[index]) == linked_list.LinkedList
            for i in self.backing_array[index]:
                if i.key == key:
                    i.value = value
            hashtable_element = KeyValuePair(key, value)
            self.backing_array[index].add_link_at_end(hashtable_element)

    def get(self, key):
        hash_code = compute_hash_code(key)
        index = hash_code % len(self.backing_array)
        if self.backing_array[index] is None:
            return None
        elif type(self.backing_array[index]) == KeyValuePair:
            assert self.backing_array[index].key == key
            return self.backing_array[index].value
        else:
            assert type(self.backing_array[index]) == linked_list.LinkedList
            for i in self.backing_array[index]:
                if i.key == key:
                    return i.value

    # [amotz]
    # in my hashtable_representation below
    # i chose to use a representation of hashtable in which
    # the indexes  of the backing array are of type int and the key value pairs are of type python list

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
                representation.append(index)
                for i in self.backing_array[index]:
                    representation.append([i.key, i.value])
        return representation


def test_Hashtable():
    hashtable = Hashtable()

    # testing that an int key is not in the hashtable
    assert hashtable.get(1000006) is None

    # putting a value in that key - testing support for int
    hashtable.put(1000006, 1001)
    assert hashtable.get(1000006) == 1001

    # Testing a collision
    # (the underlying array in the hashtable has 10 elements and both 1006 and 100006 mod 10 equal 6)
    hashtable.put(1006, 142)
    assert hashtable.get(1006) == 142

    # putting another value that is int in index 6 to have 2 elements in the 6 index - testing second collision
    hashtable.put(10000006, 35)
    assert hashtable.get(10000006) == 35

    # testing that the keys 1006 and 1000006 are still in the hashtable
    assert hashtable.get(1000006) == 1001
    assert hashtable.get(1006) == 142

    # testing hash collision
    assert "abc" != "acb"
    assert compute_hash_code("abc") == compute_hash_code("acb")
    hashtable.put('abc', 142)
    hashtable.put('cab', 378)
    assert hashtable.get('abc') == 142
    assert hashtable.get('cab') == 378

    # putting a value in a key that is a string - testing support for strings
    hashtable.put('amotz', 30)
    assert hashtable.get('amotz') == 30

    # testing a number that is not in the hashtable
    assert hashtable.get(400) is None

    # putting a value in a key that is already in the hashtable - testing update to a key
    hashtable.put('amotz', 45)
    assert hashtable.get('amotz') == 45

    # testing hashtable_representation method
    assert hashtable.hashtable_representation() == [0, 1, 2, 3, 4, ['abc', 142], ['cab', 378], 5, ['amotz', 45],
                                                    6, [1000006, 1001], [1006, 142], [10000006, 35],
                                                    7, 8, 9]


test_Hashtable()

# from here on its the rest of the code that i still need to clean and rewrite
# ------------------------------------------------------------------------------------------------
# assert hashtable.get(6) is None
# assert hashtable.get(8) is None
# assert hashtable.get(9) is None
# assert hashtable.get(9) == 32
# assert hashtable.get(8) is None
# hashtable.put(8, 123)
# assert hashtable.get(8) == 123
# hashtable.put("amotz", 30)
# assert hashtable.get("amotz") == 30
# assert hashtable.get("yotam") is None
# hashtable.put("hillel", 38)
# assert hashtable.get("hillel") == 38
# hashtable.put("anat", 70)
# assert hashtable.get("anat") == 70
# print(hashtable.Hashtable_representation())
# hashtable.remove('anat')
# assert hashtable.get("anat") is None
# hashtable.remove(8)
# assert hashtable.get(8) is None
# print(hashtable.Hashtable_representation())
# hashtable.remove(9)
# print(hashtable.Hashtable_representation())
# assert hashtable.get(299) == 765


# from here it is the rest of the code that i still need to clean
# --------------------------------------------------------------------------------------------------

#
#     def remove(self, key):
#         hash_code = compute_hash_code(key)
#         index = hash_code % len(self.backing_array)
#         if self.backing_array[index].size() == 2:
#             self.backing_array[index] = None
#         else:
#             link = self.backing_array[index].find_link(key)
#             next_link = link.get_next()
#             self.backing_array[index].remove(next_link.get_value)
#             self.backing_array[index].remove(link.get_value)
