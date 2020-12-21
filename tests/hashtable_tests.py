from data_structures import linked_list
from data_structures import hashtable
from data_structures.hashtable import generate_random_number
from data_structures.hashtable import generate_random_string
from data_structures.hashtable import compute_hash_code
from data_structures.hashtable import KeyValuePair


def test_Hashtable():
    hasht = hashtable.Hashtable()
    # testing a key that i didn't insert is not in the hasht
    # i also test the size1 method  from now on in many places in the code
    assert hasht.get(1) is None
    assert hasht.size() == 0
    # testing basic put and get
    hasht.put(1, 1)
    assert hasht.size() == 1
    assert hasht.get(1) == 1
    # a key that its index calculates to the same bucket but is not in the hasht
    # (the bucket contains a KeyValuePair object)
    assert (compute_hash_code(11) % len(hasht.backing_array)
            == compute_hash_code(1) % len(hasht.backing_array))
    assert type(hasht.backing_array[1]) == KeyValuePair
    assert hasht.get(11) is None
    assert hasht.size() == 1

    # testing hash1 collision and resizing of the backing array
    assert "abc" != "acb"
    assert compute_hash_code("abc") == compute_hash_code("acb")
    hasht.put('abc', 2)
    assert hasht.size() == 2
    hasht.put('cab', 3)
    assert hasht.size() == 3
    assert hasht.get('abc') == 2
    assert hasht.get('cab') == 3
    # testing a key that will  be stored in the same bucket as the keys above but is not in the hasht
    # (this time the bucket contains a linked list)
    assert type(hasht.backing_array[4]) == linked_list.LinkedList
    assert hasht.get('bac') is None
    assert hasht.size() == 3
    # showing that the index of the bucket that stores 'abc' and 'bac' is 4 for later testing
    assert (compute_hash_code("abc") % len(hasht.backing_array)
            == compute_hash_code("acb") % len(hasht.backing_array) == 4)
    # i add another key that will be stored in the same bucket as 'abc and 'bac' to test the put method
    # when the backing array bucket has a linked list - test for second collision
    hasht.put('acb', 1)
    assert hasht.size() == 4
    # testing resizing of the backing_array
    # since the number of elements are now more then 0.3*(length of backing array)
    assert len(hasht.backing_array) == 20
    assert hasht.get('acb') == 1
    # testing that putting the third key value pair in the same bucket didn't
    # change the other key value pairs in the bucket of index 4
    assert hasht.get('abc') == 2
    assert hasht.get('cab') == 3

    # putting a value in a key that is already in the hasht in a bucket that contains
    # a KeyValuePair object
    # testing update to a key
    assert hasht.get(1) is not None
    assert type(hasht.backing_array[1]) == KeyValuePair
    hasht.put(1, 2)
    assert hasht.get(1) == 2
    assert hasht.size() == 4
    # putting a value in a key that is already in the hasht and is in a linked list of KeyValuePair objects
    # testing update to a key
    assert hasht.get('abc') is not None
    assert type(hasht.backing_array[14]) == linked_list.LinkedList
    hasht.put('abc', 8)
    assert hasht.get('abc') == 8
    assert hasht.size() == 4
    # testing hashtable_representation method and resizing of backing array
    assert hasht.hashtable_representation() == [0, 1, [1, 2], 2, 3, 4, 5,
                                                6, 7, 8, 9, 10, 11, 12, 13, 14, ['abc', 8], ['cab', 3], ['acb', 1],
                                                15,
                                                16, 17, 18, 19]
    # testing remove method
    # single KeyValuePair in backing array location
    assert type(hasht.backing_array[1]) == KeyValuePair
    assert hasht.remove(1)
    assert len(hasht.backing_array) == 10
    assert hasht.get(1) is None
    assert hasht.size() == 3
    # more then two KeyValuePairs in backing array location
    assert type(hasht.backing_array[4]) == linked_list.LinkedList
    assert hasht.remove('cab')
    assert hasht.get('cab') is None
    assert hasht.size() == 2
    # test that all the key value pairs in the hasht are still in the right places.
    # also that resizing of backing array is correct
    assert hasht.hashtable_representation() == [0, 1, 2, 3, 4, ['abc', 8], ['acb', 1], 5, 6, 7, 8, 9]

    assert not hasht.remove(2)
    assert hasht.size() == 2
    # test of removing a key that is not in the hasht
    assert hasht.get(2) is None
    # test that all the key value pairs in the hasht are still in the right places
    assert hasht.hashtable_representation() == [0, 1, 2, 3, 4, ['abc', 8], ['acb', 1], 5,
                                                6, 7, 8, 9]

    # removing a key in a bucket with exactly two keys.
    # checking consistence type of objects in a bucket with two KeyValuePair objects
    assert hasht.remove('acb')
    assert hasht.size() == 1
    assert len(hasht.backing_array) == 10
    assert type(hasht.backing_array[4]) == KeyValuePair
    assert hasht.remove('abc')
    assert hasht.size() == 0
    assert hasht.backing_array[4] is None


test_Hashtable()


def test_iterator():
    # Test with a hasht that has
    # [1]: a regular backing array element containing a simple KeyValuePair
    # [2]: a backing array element containing a LinkedList
    # [3]: another regular backing array element containing a simple KeyValuePair to make sure that we keep iterating
    #      over the array after we've finished iterating over the list.
    hasht = hashtable.Hashtable(False)  # We don't want this Hashtable to grow and spread lists out during this test.
    hasht.put(1, "a")
    hasht.put(2, "b")
    hasht.put(22, "bb")
    hasht.put(3, "c")
    assert hasht.size() == 4
    assert isinstance(hasht.backing_array[1], KeyValuePair)
    assert isinstance(hasht.backing_array[2], linked_list.LinkedList)
    assert isinstance(hasht.backing_array[3], KeyValuePair)

    py_dict = {}
    for keyValue in hasht:
        py_dict[keyValue.key] = keyValue.value

    assert len(py_dict) == hasht.size() == 4, \
        'len(py_dict) == {}, hasht.size() == {}'.format(len(py_dict), hasht.size())
    assert py_dict.get(1, "a")
    assert py_dict.get(2, "b")
    assert py_dict.get(22, "bb")
    assert py_dict.get(3, "c")


test_iterator()


def create_hash_and_dict():
    hash1 = hashtable.Hashtable()
    py_dict = {}
    STRESS_TEST_SIZE = 1000
    for i in range(STRESS_TEST_SIZE):
        rand_num_key = generate_random_number()
        rand_num_value = generate_random_number()
        rand_str_key = generate_random_string()
        rand_str_value = generate_random_string()
        hash1.put(rand_num_key, rand_num_value)
        hash1.put(rand_str_key, rand_str_value)
        py_dict[rand_num_key] = rand_num_value
        py_dict[rand_str_key] = rand_str_value

    for i in hash1:
        hash1.remove(i.key)
        del py_dict[i.key]
        if hash1.size() == 500:
            break
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

# TODO to make sure that the big tests test for updates
# TODO refactoring the check_resize method
# TODO testing the shrinking of the array and growing of the array in the big tests...
