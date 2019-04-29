
# linked list object should have a link class and a linkedlist class.


# in the link class it should have link values and pointers to the next links.
# we will initialize the class to have a node value and a pointer to None.
# i will add a method set_next, that will help me to set a pointer to the next link
# i will add a method get_next that will return the value of the next link
# i will also add a method get_data that will return the value of the link


class Link:
    def __init__(self, link_value):
        self.link_value = link_value
        self.next = None

    def set_next(self, new_next):
        self.next = new_next

    def get_next(self):
        return self.next

    def get_data(self):
        return self.link_value


# linked list should contain constructor with a head link, in the beginning it will equal to None.
# i added a method called add_link that create a new link and connecting it to the existing linkedlist and then changing the head_link to be the new link
# i added a method to check if the linklist is empty
# for finding an element in the list:
# first i will traverse the linked list with a pointer that will start at the head_link asking if this is the element that we are searching
# then if its not i will use the get_next method to traverse the linked list and check each link for the element


class LinkedList:
    def __init__(self):
        self.head_link = None

    def is_empty(self):
        return self.head_link is None

    def add_link(self, new_link):
        temp = Link(new_link)
        temp.set_next(self.head_link)
        self.head_link = temp

    def find(self, element):
        pointer = self.head_link
        while pointer is not None:
            if pointer.get_data() == element:
                return True
            else:
                pointer = pointer.get_next()
        return False

# this is a test to the link class first i create a link called my_link with parameter 6 and then i check all the attributes and methods


def test_link_class():
    my_link = Link(6)
    assert (my_link.link_value == 6)
    assert (my_link.next is None)
    my_link.set_next(43)
    assert (my_link.next == 43)
    assert(my_link.get_next() == 43)
    assert ((my_link.get_data()) == 6)

# this is the test to the linked_list class again i check all the methods and attributes


def test_linked_list_class():
    my_list = LinkedList()
    assert (my_list.head_link is None)
    assert (my_list.is_empty() == True)
    my_list.add_link(4)
    assert(my_list.head_link.link_value == 4)
    my_list.add_link(7)
    assert (my_list.head_link.link_value == 7)
    my_list.add_link(3)
    assert (my_list.head_link.link_value == 3)
    assert (my_list.is_empty() == False)
    assert (my_list.find(7))
    assert (my_list.find(4))
    assert (my_list.find(8) == False)
    assert (my_list.find(3))


test_linked_list_class()
test_link_class()





