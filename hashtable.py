def hash_integer_function(key):
    return key


def hash_string_function(key):
    ascii_code_list = [ord(c) for c in key]
    hash_code = sum(ascii_code_list)
    list_index = hash_code
    return list_index


def test_hash_string_function():
    test_case_1 = 'abc'
    assert hash_string_function(test_case_1) == 294


test_hash_string_function()


class Hashtable:

    def __init__(self, my_list):
        self.my_list = my_list

    def put(self, key, value):
        if type(key) == int:
            hash_code = hash_integer_function(key)
            self.my_list[hash_code] = (key, value)
            return self.my_list

        if type(key) == str:
            hash_code = hash_string_function(key)
            list_index = hash_code % len(self.my_list)
            self.my_list[list_index] = (key, value)
            return self.my_list

    def get_key(self, key):
        if type(key) == int:
            hash_code = hash_integer_function(key)
            if self.my_list[key] is not None:
                return self.my_list[hash_code][1]
            else:
                return None
        if type(key) == str:
            hash_code = hash_string_function(key)
            list_index = hash_code % len(self.my_list)
            if self.my_list[list_index] is not None:
                return self.my_list[list_index][1]
            else:
                return None


def test_Hashtable():
    amotz_hashtable = Hashtable([None]*10)
    assert amotz_hashtable.get_key(6) is None
    assert amotz_hashtable.get_key(8) is None
    assert amotz_hashtable.get_key(9) is None
    amotz_hashtable.put(6, 1001)
    assert amotz_hashtable.get_key(6) == 1001
    assert amotz_hashtable.get_key(9) is None
    assert amotz_hashtable.get_key(8) is None
    amotz_hashtable.put(8, 123)
    assert amotz_hashtable.get_key(8) == 123
    assert amotz_hashtable.get_key(9) is None
    amotz_hashtable.put(9, 1556)
    assert amotz_hashtable.get_key(9) == 1556
    assert amotz_hashtable.get_key(6) == 1001
    assert amotz_hashtable.get_key(8) == 123
    amotz_hashtable.put("amotz", 30)
    assert amotz_hashtable.get_key("amotz") == 30
    assert amotz_hashtable.get_key("yotam") is None
    amotz_hashtable.put("hillel", 38)
    assert amotz_hashtable.get_key("hillel") == 38
    assert amotz_hashtable.put("anat", 70)
    assert amotz_hashtable.get_key("anat") == 70


test_Hashtable()




