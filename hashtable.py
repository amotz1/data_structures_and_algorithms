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
            if not is_key_found:
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

    def remove(self, key):
        hash_code = compute_hash_code(key)
        index = hash_code % len(self.backing_array)
        if type(self.backing_array[index]) == KeyValuePair:
            self.backing_array[index] = None
        elif type(self.backing_array[index]) == linked_list.LinkedList:
            for i in self.backing_array[index]:
                if i.key == key:
                    self.backing_array[index].remove(i)
        else:
            print("the number  is not in the hashtable so cannot be removed")

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
    # testing a different key that will be stored in the same bucket but is not in the hashtable
    # (the bucket contains a KeyValuePair object)
    assert (compute_hash_code(11) % len(hashtable.backing_array)
            == compute_hash_code(1) % len(hashtable.backing_array))
    assert type(hashtable.backing_array[1]) == KeyValuePair
    assert hashtable.get(11) is None

    # testing hash collision
    assert "abc" != "acb"
    assert compute_hash_code("abc") == compute_hash_code("acb")
    hashtable.put('abc', 2)
    hashtable.put('cab', 3)
    assert hashtable.get('abc') == 2
    assert hashtable.get('cab') == 3
    # testing a key that will be stored in the same bucket as the keys above but is not in the hashtable
    # (this time the bucket contains a linked list)
    assert type(hashtable.backing_array[4]) == linked_list.LinkedList
    assert hashtable.get('bac') is None
    # showing that the index of the bucket that stores 'abc' and 'bac is 4 for later testing
    assert (compute_hash_code("abc") % len(hashtable.backing_array)
            == compute_hash_code("acb") % len(hashtable.backing_array) == 4)
    # i add another key that will be stored in the same bucket as 'abc and 'bac' to test the put method
    # when the backing array bucket has a linked list - test for second collision
    hashtable.put(4, 1)
    assert hashtable.get(4) == 1
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
    # putting a value in a key that is already in the hashtable and is in a linked list of KeyValuePair objects
    # testing update to a key
    assert hashtable.get(4) is not None
    assert type(hashtable.backing_array[4]) == linked_list.LinkedList
    hashtable.put(4, 3)
    assert hashtable.get(4) == 3

    # testing hashtable_representation method
    assert hashtable.hashtable_representation() == [0, 1, [1, 2], 2, 3, 4, ['abc', 2], ['cab', 3], [4, 3], 5,
                                                    6, 7, 8, 9]

    # test of removing a key in a KeyValuePair object that is not in a linked list object
    assert type(hashtable.backing_array[1]) == KeyValuePair
    hashtable.remove(1)
    assert hashtable.get(1) is None
    # test of removing a key that is in a LinkedList object
    assert type(hashtable.backing_array[4]) == linked_list.LinkedList
    hashtable.remove('cab')
    assert hashtable.get('cab') is None
    # test that all the key value pairs in the hashtable are still in the right places
    assert hashtable.hashtable_representation() == [0, 1, 2, 3, 4, ['abc', 2], [4, 3], 5,
                                                    6, 7, 8, 9]
    hashtable.remove(2)
    # test of removing a key that is not in the hashtable
    assert hashtable.get(2) is None
    # test that all the key value pairs in the hashtable are still in the right places
    assert hashtable.hashtable_representation() == [0, 1, 2, 3, 4, ['abc', 2], [4, 3], 5,
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
