# implementing Link and LinkedList


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
        self._head_link = None
        self._last_link = None

    def is_empty(self):
        return self._head_link is None

    def _find_link(self, value):
        link = self._head_link
        while link is not None:
            if link.get_value() == value:
                return link
            else:
                link = link.get_next()
        return None

    def find_link(self, value):
        return self._find_link(value) is not None

    def add_link_at_start(self, value):
        new_link = _Link(value)
        new_link.set_next(self._head_link)
        self._head_link = new_link

    def add_link_at_end(self, value):
        new_link = _Link(value)
        if self._head_link is None:
            self._head_link = new_link
            self._last_link = self._head_link
        else:
            self._last_link.set_next(new_link)
            self._last_link = new_link
            new_link.set_next(None)

    def remove(self, value):
        link_to_find = self._find_link(value)
        if link_to_find == self._head_link:
            self._head_link = link_to_find.get_next()
            link_to_find.set_next(None)
            return link_to_find.value
        elif link_to_find == self._last_link:
            previous_link = self._head_link
            while previous_link.get_next() is not link_to_find:
                previous_link = previous_link.get_next()
            previous_link.set_next(None)
            return previous_link.valu
        elif link_to_find != self._head_link and link_to_find != self._last_link and link_to_find is not None:
            previous_link = self._head_link
            while previous_link.get_next() is not link_to_find:
                previous_link = previous_link.get_next()
            previous_link.set_next(link_to_find.get_next())
            link_to_find.set_next(None)
            return link_to_find.value
        else:
            return None

    def __iter__(self):
        new_iterator = _LinkedListIterator(self._head_link)
        return new_iterator

    def add_link_after(self, link_to_add, value):
        link_to_find = self._find_link(value)
        if link_to_find == self._last_link:
            new_link = _Link(link_to_add)
            self._last_link.set_next(new_link)
            self._last_link = new_link
        elif link_to_find != self._last_link and link_to_find is not None:
            new_link = _Link(link_to_add)
            new_link.set_next(link_to_find.get_next())
            link_to_find.set_next(new_link)
        else:
            print(value, "is not in the list so you will better use an element that is in it")


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
    my_list.add_link_at_end("Yotam")
    assert (not my_list.is_empty())
    my_list.add_link_at_end("Amotz")
    my_list.add_link_at_end("Anat")
    my_list.add_link_at_start("hillel")
    assert my_list.find_link("Amotz")
    assert my_list.remove("Amotz") == "Amotz"
    assert not my_list.find_link("Amotz")
    my_list.add_link_after("Asaf", "Anat")
    my_list.add_link_after("anat", "yonatan")
    assert not my_list.find_link("yonatan") is None
    assert my_list.remove("sara") is None
    assert not my_list.find_link("sara")
    for i in my_list:
        print(i)
    my_iterator = my_list.__iter__()
    assert my_iterator.__next__() == "hillel"
    assert my_iterator.__next__() == "Yotam"
    assert my_iterator.__next__() == "Anat"
    assert my_iterator.__next__() == "Asaf"


test_Linked_List()
