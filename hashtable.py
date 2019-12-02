# [amotz]
# this hashtable implementation have a class with two methods put and get.
# the put method can have integer and string as keys,
# it puts them according to the hash function compute_list_index in a list, self.my_list.
# the get method can search the value that i put in the list and return it.

# the put method cannot take objects yet
# the hashtable does not implement collisions remove method and automatically resizing array yet
# the hashtable may break for certain keys for sure, and my tests are using keys that will not break the program.


def compute_list_index(key, list_length):
    if type(key) == str:
        list_of_ascii_code_chars = [ord(c) for c in key]
        hash_code = sum(list_of_ascii_code_chars)
        list_index = hash_code % list_length
        return list_index
    if type(key) == int:
        return key


def test_hash_function():
    test_case_1 = 'abc'
    test_case_2 = 3
    assert compute_list_index(test_case_1, 10) == 4
    assert compute_list_index(test_case_2, 10) == 3


test_hash_function()


class Hashtable:

    def __init__(self, my_list):
        self.my_list = my_list

    def put(self, key, value):
        list_index = compute_list_index(key, len(self.my_list))
        self.my_list[list_index] = (key, value)

    def get(self, key):
        hash_code = compute_list_index(key, len(self.my_list))
        if self.my_list[hash_code] is not None:
            return self.my_list[hash_code][1]
        else:
            return None


def test_Hashtable():
    amotz_hashtable = Hashtable([None]*10)
    assert amotz_hashtable.get(6) is None
    assert amotz_hashtable.get(8) is None
    assert amotz_hashtable.get(9) is None
    amotz_hashtable.put(6, 1001)
    assert amotz_hashtable.get(6) == 1001
    assert amotz_hashtable.get(9) is None
    assert amotz_hashtable.get(8) is None
    amotz_hashtable.put(8, 123)
    assert amotz_hashtable.get(8) == 123
    assert amotz_hashtable.get(9) is None
    amotz_hashtable.put(9, 1556)
    assert amotz_hashtable.get(9) == 1556
    assert amotz_hashtable.get(6) == 1001
    assert amotz_hashtable.get(8) == 123
    amotz_hashtable.put("amotz", 30)
    assert amotz_hashtable.get("amotz") == 30
    assert amotz_hashtable.get("yotam") is None
    amotz_hashtable.put("hillel", 38)
    assert amotz_hashtable.get("hillel") == 38
    amotz_hashtable.put("anat", 70)
    assert amotz_hashtable.get("anat") == 70


test_Hashtable()




