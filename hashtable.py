import linked_list


# [amotz]
# hashtable partial implementation int and string are supported with only hashtable_representation and put methods
# the hashtable support collisions but not automatically growing array

def compute_hash_code(key):
    if type(key) == str:
        list_of_ascii_code_chars = [ord(c) for c in key]  # computing the unicode of chars and putting them in a list
        hash_code = sum(list_of_ascii_code_chars)
        return hash_code
    elif type(key) == int:
        return key
    else:
        assert False


def test_compute_hash_code():
    test_case_1 = 'abc'
    test_case_2 = 3
    assert compute_hash_code(test_case_1) == 294
    assert compute_hash_code(test_case_2) == 3


test_compute_hash_code()


class HashtableElement:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.key_value_pair = []

    def get_key_value_pair(self):
        key_value_pair = [self.key, self.value]
        return key_value_pair


class Hashtable:

    def __init__(self, backing_array):
        self.backing_array = backing_array

    def put(self, key, value):
        hash_code = compute_hash_code(key)
        backing_array_index = hash_code % len(self.backing_array)
        if self.backing_array[backing_array_index] is None:
            hashtable_element = HashtableElement(key, value)
            self.backing_array[backing_array_index] = hashtable_element
        else:
            hashtable_element = HashtableElement(key, value)
            b_a_linked_list = linked_list.LinkedList()
            b_a_linked_list.add_link_at_end(self.backing_array[backing_array_index])
            b_a_linked_list.add_link_at_end(hashtable_element)
            self.backing_array[backing_array_index] = b_a_linked_list

    # [amotz]
    # in my hashtable_representation below
    # i chose to use a representation of index of backing array without brackets and key value pairs with brackets

    def hashtable_representation(self):
        representation = []
        for backing_array_index in range(len(self.backing_array)):
            if type(self.backing_array[backing_array_index]) == linked_list.LinkedList:
                representation.append(backing_array_index)
                for b_a_linked_list_index in self.backing_array[backing_array_index]:
                    representation.append(b_a_linked_list_index.get_key_value_pair())
            elif type(self.backing_array[backing_array_index]) == HashtableElement:
                representation.append(backing_array_index)
                representation.append(self.backing_array[backing_array_index].get_key_value_pair())
            else:
                representation.append(backing_array_index)
        return representation

def test_Hashtable():
    amotz_hashtable = Hashtable([None] * 10)
    # putting a value in a key that is int that is not in the hashtable
    amotz_hashtable.put(1000006, 1001)
    # putting a value in a key that is int that is already in the hashtable
    amotz_hashtable.put(1006, 142)
    # putting values in a key that is a string
    amotz_hashtable.put('amotz', 30)
    # testing that every element is put in the right places of the hashtable
    assert amotz_hashtable.hashtable_representation() == [0, 1, 2, 3, 4, 5, ['amotz', 30],
                                                          6, [1000006, 1001], [1006, 142],
                                                          7, 8, 9]


test_Hashtable()

# from here on its the rest of the code that i still need to clean and rewrite
# ------------------------------------------------------------------------------------------------
# assert amotz_hashtable.get(6) is None
# assert amotz_hashtable.get(8) is None
# assert amotz_hashtable.get(9) is None
# assert amotz_hashtable.get(9) == 32
# assert amotz_hashtable.get(8) is None
# amotz_hashtable.put(8, 123)
# assert amotz_hashtable.get(8) == 123
# amotz_hashtable.put("amotz", 30)
# assert amotz_hashtable.get("amotz") == 30
# assert amotz_hashtable.get("yotam") is None
# amotz_hashtable.put("hillel", 38)
# assert amotz_hashtable.get("hillel") == 38
# amotz_hashtable.put("anat", 70)
# assert amotz_hashtable.get("anat") == 70
# print(amotz_hashtable.Hashtable_representation())
# amotz_hashtable.remove('anat')
# assert amotz_hashtable.get("anat") is None
# amotz_hashtable.remove(8)
# assert amotz_hashtable.get(8) is None
# print(amotz_hashtable.Hashtable_representation())
# amotz_hashtable.remove(9)
# print(amotz_hashtable.Hashtable_representation())
# assert amotz_hashtable.get(299) == 765


# from here it is the rest of the code that i still need to clean
# --------------------------------------------------------------------------------------------------
#     def get(self, key):
#         hash_code = compute_hash_code(key)
#         backing_array_index = hash_code % len(self.backing_array)
#         if self.backing_array[backing_array_index] is not None:
#             new_iterator = self.backing_array[backing_array_index].__iter__()
#             link_value = new_iterator.__next__()
#             if link_value == key:
#                 return self.backing_array[backing_array_index].get_last_link()
#             else:
#                 link = self.backing_array[backing_array_index].find_link(key)
#                 next_link = link.get_next()
#                 return next_link.get_value()
#
#     def remove(self, key):
#         hash_code = compute_hash_code(key)
#         backing_array_index = hash_code % len(self.backing_array)
#         if self.backing_array[backing_array_index].size() == 2:
#             self.backing_array[backing_array_index] = None
#         else:
#             link = self.backing_array[backing_array_index].find_link(key)
#             next_link = link.get_next()
#             self.backing_array[backing_array_index].remove(next_link.get_value)
#             self.backing_array[backing_array_index].remove(link.get_value)
