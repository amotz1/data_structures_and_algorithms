from linked_list import LinkedList


def test_Linked_List():
    my_list = LinkedList()
    # adding a head_link
    my_list.add_tail("Yotam")
    # checking find function on something in the linked list
    assert (my_list.find_link("Yotam"))
    # removing a head_link when there is one element in the linked list
    my_list.remove("Yotam")
    # checking the find function on something that is not in the linked list
    assert (my_list.find_link("gargamel") is None)
    # checking the is_empty function
    assert (my_list.is_empty())
    # adding a link that is not the head link
    my_list.add_tail("Amotz")
    # remove a head_link
    my_list.check_invariant()
    # adding a link at start
    my_list.add_head("Yotam")
    # removing a last link
    my_list.remove("Amotz")
    my_list.add_tail("Anat")
    my_list.add_tail("Hillel")
    # removing a link that is not in the end and not in the start
    my_list.remove("Anat")
    # checking removing a link that is not in the linked list
    assert my_list.remove("element_not_in_list") is None
    # adding a link after a last link
    my_list.add_link_after("Asaf", "Hillel")
    # adding a link after a link that is not the last link
    my_list.add_link_after("moshe", "Hillel")
    # adding a link after a link that is not found in the list
    my_list.add_link_after("random_element", "yonatan")
    # checking that if a head_link is present a last link is also present
    # and if a head link is not present a last link is not present
    my_list.check_invariant()
    # checking that all the links in the linked_list are in the right places
    assert [elem for elem in my_list] == ['Yotam', 'Hillel', 'moshe', 'Asaf']
    assert my_list.compute_size() == 4
    my_list.remove_head()
    assert [elem for elem in my_list] == ['Hillel', 'moshe', 'Asaf']
    my_list.remove_head()
    assert [elem for elem in my_list] == ['moshe', 'Asaf']
    my_list.remove_head()
    assert [elem for elem in my_list] == ['Asaf']
    my_list.remove_head()
    assert [elem for elem in my_list] == []


test_Linked_List()
my_list = LinkedList()
my_list.add_tail("Yotam")
my_list.add_tail("amotz")
