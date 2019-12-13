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
        if self.my_list[list_index] is None:
            my_linked_list = linked_list.LinkedList()
            my_linked_list.add_link_at_end(key)
            my_linked_list.add_link_at_end(value)
            self.my_list[list_index] = my_linked_list
        else:
            self.my_list[list_index].add_link_at_end(key)
            self.my_list[list_index].add_link_at_end(value)

    def get(self, key):
        hash_code = compute_hash_code(key)
        list_index = hash_code % len(self.my_list)
        if self.my_list[list_index] is not None:
            new_iterator = self.my_list[list_index].__iter__()
            link_value = new_iterator.__next__()
            if link_value == key:
                return self.my_list[list_index].get_last_link()
            else:
                link = self.my_list[list_index].find_link(key)
                next_link = link.get_next()
                return next_link.get_value()

    def traverse(self):
        keys_and_values = []
        for list_index in range(len(self.my_list)):
            if self.my_list[list_index] is not None:
                keys_and_values.append(list_index)
                for linked_list_index in self.my_list[list_index]:
                    keys_and_values.append([linked_list_index])
        return keys_and_values

    def remove(self, key):
        hash_code = compute_hash_code(key)
        list_index = hash_code % len(self.my_list)
        if self.my_list[list_index].size() == 2:
            self.my_list[list_index] = None
        else:
            link = self.my_list[list_index].find_link(key)
            next_link = link.get_next()
            self.my_list[list_index].remove(next_link.get_value)
            self.my_list[list_index].remove(link.get_value)


def test_Hashtable():
    amotz_hashtable = Hashtable([None] * 10)
    assert amotz_hashtable.get(6) is None
    assert amotz_hashtable.get(8) is None
    assert amotz_hashtable.get(9) is None
    amotz_hashtable.put(1000006, 1001)
    amotz_hashtable.put(1006, 142)
    amotz_hashtable.put(299, 765)
    amotz_hashtable.put(9, 32)
    assert amotz_hashtable.traverse() == [6, [1000006], [1001], [1006], [142], 9, [299], [765], [9], [32]]
    assert amotz_hashtable.get(9) == 32
    assert amotz_hashtable.get(8) is None
    amotz_hashtable.put(8, 123)
    assert amotz_hashtable.get(8) == 123
    amotz_hashtable.put("amotz", 30)
    assert amotz_hashtable.get("amotz") == 30
    assert amotz_hashtable.get("yotam") is None
    amotz_hashtable.put("hillel", 38)
    assert amotz_hashtable.get("hillel") == 38
    amotz_hashtable.put("anat", 70)
    assert amotz_hashtable.get("anat") == 70
    print(amotz_hashtable.traverse())
    amotz_hashtable.remove('anat')
    assert amotz_hashtable.get("anat") is None
    amotz_hashtable.remove(8)
    assert amotz_hashtable.get(8) is None
    print(amotz_hashtable.traverse())
    amotz_hashtable.remove(9)
    print(amotz_hashtable.traverse())
    assert amotz_hashtable.get(299) == 765



test_Hashtable()
