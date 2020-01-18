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
            is_key_found = False
            for i in self.backing_array[index]:
                if i.key == key:
                    is_key_found = True
                    i.value = value
                else:
                    pass
            if is_key_found is False:
                hashtable_element = KeyValuePair(key, value)
                self.backing_array[index].add_link_at_end(hashtable_element)

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
            for i in self.backing_array[index]:
                if i.key == key:
                    return i.value
            return None

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

    # testing a key that i didn't insert is not in the hashtable
    assert hashtable.get(1) is None

    # testing basic put and get
    hashtable.put(1, 1)
    assert hashtable.get(1) == 1
    # testing a different key that computes to index 1 also but is not in the hashtable
    assert hashtable.get(11) is None

    # testing hash collision
    assert "abc" != "acb"
    assert compute_hash_code("abc") == compute_hash_code("acb")
    hashtable.put('abc', 2)
    hashtable.put('cab', 3)
    assert hashtable.get('abc') == 2
    assert hashtable.get('cab') == 3
    # testing a key that computes to the same index as the keys above but is not in the hashtable
    assert hashtable.get('bac') is None
    # the key 'abc' and 'cab' computes to the index 4,
    # i add another key that computes to the index 4 to test the put method
    # when the backing array index has a linked list - test for second collision
    hashtable.put(4, 1)
    assert hashtable.get(4) == 1
    # testing that putting the third key value pair in index 4 didn't change the other key value pairs in index 4
    assert hashtable.get('abc') == 2
    assert hashtable.get('cab') == 3

    # putting a value in a key that is already in the hashtable and is in
    # a KeyValuePair object that is not in a linked list
    # testing update to a key
    hashtable.put(1, 2)
    assert hashtable.get(1) == 2
    # putting a value in a key that is already in the hashtable and is in a linked list of KeyValuePair objects
    # testing update to a key
    hashtable.put(4, 3)
    assert hashtable.get(4) == 3

    # testing hashtable_representation method
    assert hashtable.hashtable_representation() == [0, 1, [1, 2], 2, 3, 4, ['abc', 2], ['cab', 3], [4, 3], 5,
                                                    6, 7, 8, 9]


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
