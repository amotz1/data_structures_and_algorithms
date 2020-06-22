# implementing Link and LinkedList

DEVELOPMENT_MODE = True


class _Link:
    def __init__(self, value):
        self.value = value
        self.next = None

    def set_next(self, new_next):
        self.next = new_next

    def get_next(self):
        return self.next

    def get_value(self):
        return self.value


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        return self._head is None

    def get_head_value(self):
        return self._head.value

    def get_tail_value(self):
        return self._tail.value

    def _find_link(self, value):
        link = self._head
        while link is not None:
            if link.get_value() == value:
                return link
            else:
                link = link.get_next()
        return None

    def find_link(self, value: str) -> bool:
        return self._find_link(value)

    def add_head(self, value):
        new_link = _Link(value)
        if self._head is None:
            self._head = new_link
            self._tail = self._head
        else:
            new_link.set_next(self._head)
            self._head = new_link

    def add_link_after(self, link_to_add, value):
        link_to_find = self._find_link(value)
        if link_to_find == self._tail:
            new_link = _Link(link_to_add)
            self._tail.set_next(new_link)
            self._tail = new_link
        elif link_to_find != self._tail and link_to_find is not None:
            new_link = _Link(link_to_add)
            new_link.set_next(link_to_find.get_next())
            link_to_find.set_next(new_link)
        else:
            print(value, "is not in the list so you will better use an element that is in it")

    def add_tail(self, value):
        new_link = _Link(value)
        if self._head is None:
            self._head = new_link
            self._tail = self._head
        else:
            self._tail.set_next(new_link)
            self._tail = new_link
            new_link.set_next(None)

    def remove(self, value: int) -> _Link:
        link_to_find = self._find_link(value)
        if link_to_find == self._head:
            self._head = link_to_find.get_next()
            link_to_find.set_next(None)
            return link_to_find.value
        elif link_to_find == self._tail:
            previous_link = self._head
            # doing a loop because i don't have prev pointers (its a linked_list)
            while previous_link.get_next() is not link_to_find:
                previous_link = previous_link.get_next()
            previous_link.set_next(None)
            self._tail = previous_link
            return link_to_find.value
        elif link_to_find is not None:
            previous_link = self._head
            while previous_link.get_next() is not link_to_find:
                previous_link = previous_link.get_next()
            previous_link.set_next(link_to_find.get_next())
            link_to_find.set_next(None)
            return link_to_find.value
        else:
            return None

    def size(self):
        count_links = 0
        link = self._head
        while link is not None:
            link = link.get_next()
            count_links += 1
        return count_links

    def check_invariant(self):
        if self._head is None:
            assert self._tail is None
        else:
            assert self._tail is not None

    def remove_head(self):
        if self.size() > 1:
            link = self._head.get_next()
            temp = self._head
            self._head = link
            return temp
        else:
            temp = self._head
            self._head = None
            self._tail = None
            return temp

    def __iter__(self):
        new_iterator = _LinkedListIterator(self._head)
        return new_iterator


class _LinkedListIterator:
    def __init__(self, current):
        self._current = current

    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            value = self._current
            self._current = self._current.get_next()
            return value.value


def test_Linked_List():
    my_list = LinkedList()
    # adding a head_link
    my_list.add_tail("Yotam")
    # checking find function on something in the linked list
    assert (my_list.find_link("Yotam"))
    #removing a head_link when there is one element in the linked list
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
    assert my_list.size() == 4
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
