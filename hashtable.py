import linked_list


# [amotz]
# hashtable partial implementation int and string are supported with only hashtable_representation and put methods
# the hashtable support first and second collisions but not automatically growing array still no get method
#
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
    test_case_1 = 'abc'
    test_case_2 = 3
    assert compute_hash_code(test_case_1) == 294
    assert compute_hash_code(test_case_2) == 3


test_compute_hash_code()


class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Hashtable:

    def __init__(self):
        self.backing_array = [None]*10

    def put(self, key, value):
        hash_code = compute_hash_code(key)
        index = hash_code % len(self.backing_array)
        if self.backing_array[index] is None:
            hashtable_element = KeyValuePair(key, value)
            self.backing_array[index] = hashtable_element
        elif type(self.backing_array[index]) == KeyValuePair:
            hashtable_element = KeyValuePair(key, value)
            b_a_linked_list = linked_list.LinkedList()
            b_a_linked_list.add_link_at_end(self.backing_array[index])
            b_a_linked_list.add_link_at_end(hashtable_element)
            self.backing_array[index] = b_a_linked_list
        else:
            hashtable_element = KeyValuePair(key, value)
            self.backing_array[index].add_link_at_end(hashtable_element)

    # [amotz]
    # in my hashtable_representation below
    # i chose to use a representation of index of backing array without brackets and key value pairs with brackets

    def hashtable_representation(self):
        representation = []
        for index in range(len(self.backing_array)):
            if type(self.backing_array[index]) == linked_list.LinkedList:
                representation.append(index)
                for linked_list_index in self.backing_array[index]:
                    representation.append([linked_list_index.key, linked_list_index.value])
            elif type(self.backing_array[index]) == KeyValuePair:
                representation.append(index)
                representation.append([self.backing_array[index].key, self.backing_array[index].value])
            else:
                representation.append(index)
        return representation


def test_Hashtable():
    amotz_hashtable = Hashtable()
    # putting a value in a key that is int that is not in the hashtable-testing support for int
    amotz_hashtable.put(1000006, 1001)
    # putting a value in a key that is int that is already in the hashtable- testing first collision
    amotz_hashtable.put(1006, 142)
    # putting another value that is int in the index 6 to have 3 elements in the 6 index - testing second collision
    amotz_hashtable.put(10000006, 35)
    # putting a value in a key that is a string-testing support for strings
    amotz_hashtable.put('amotz', 30)
    # testing that every element is put in the right places of the hashtable
    assert amotz_hashtable.hashtable_representation() == [0, 1, 2, 3, 4, 5, ['amotz', 30],
                                                          6, [1000006, 1001], [1006, 142], [10000006, 35],
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
#         index = hash_code % len(self.backing_array)
#         if self.backing_array[index] is not None:
#             new_iterator = self.backing_array[index].__iter__()
#             link_value = new_iterator.__next__()
#             if link_value == key:
#                 return self.backing_array[index].get_last_link()
#             else:
#                 link = self.backing_array[index].find_link(key)
#                 next_link = link.get_next()
#                 return next_link.get_value()
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
