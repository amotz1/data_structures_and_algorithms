import linked_list
# [amotz]
# hashtable partial implementation currently int and string are supported
# (fixed the bug that you mentioned and now have test for it)
# i added also remove method with tests
# i also changed the tuple implementation to my linked_list in preparation to work on collisions.
# i temporarily changed our get method from get(key) to get(key, value)
# because we might have more then two values in our linked list (open for new solutions)

# collisions and array automatic resizing are not supported yet.


def compute_hash_code(key):
    if type(key) == str:
        list_of_ascii_code_chars = [ord(c) for c in key]
        hash_code = sum(list_of_ascii_code_chars)
        return hash_code
    if type(key) == int:
        return key


def test_compute_hash_code():
    test_case_1 = 'abc'
    test_case_2 = 3
    assert compute_hash_code(test_case_1) == 294
    assert compute_hash_code(test_case_2) == 3


test_compute_hash_code()


class Hashtable:

    def __init__(self, my_list):
        self.my_list = my_list

    def put(self, key, value):
        hash_code = compute_hash_code(key)
        list_index = hash_code % len(self.my_list)
        my_Linked_list = linked_list.LinkedList()
        my_Linked_list.add_link_at_end(key)
        my_Linked_list.add_link_at_end(value)
        self.my_list[list_index] = my_Linked_list

    def get(self, key, value):
        hash_code = compute_hash_code(key)
        list_index = hash_code % len(self.my_list)
        if self.my_list[list_index] is not None:
            return self.my_list[list_index].find_link(value).value
        else:
            return None

    def remove(self, key):
        hash_code = compute_hash_code(key)
        list_index = hash_code % len(self.my_list)
        del self.my_list[list_index]


def test_Hashtable():
    amotz_hashtable = Hashtable([None]*10)
    assert amotz_hashtable.get(6, None) is None
    assert amotz_hashtable.get(8, None) is None
    assert amotz_hashtable.get(9, None) is None
    amotz_hashtable.put(1000006, 1001)
    assert amotz_hashtable.get(1000006, 1001) == 1001
    assert amotz_hashtable.get(9, None) is None
    assert amotz_hashtable.get(8, None) is None
    amotz_hashtable.put(8, 123)
    assert amotz_hashtable.get(8, 123) == 123
    assert amotz_hashtable.get(9, None) is None
    amotz_hashtable.put(9, 1556)
    assert amotz_hashtable.get(9, 1556) == 1556
    assert amotz_hashtable.get(6, 1001) == 1001
    assert amotz_hashtable.get(8, 123) == 123
    amotz_hashtable.put("amotz", 30)
    assert amotz_hashtable.get("amotz", 30) == 30
    assert amotz_hashtable.get("yotam", None) is None
    amotz_hashtable.put("hillel", 38)
    assert amotz_hashtable.get("hillel", 38) == 38
    amotz_hashtable.put("anat", 70)
    assert amotz_hashtable.get("anat", 70) == 70
    amotz_hashtable.remove('anat')
    assert amotz_hashtable.get("anat", None) is None
    amotz_hashtable.remove('8')
    assert amotz_hashtable.get("8", None) is None

test_Hashtable()




