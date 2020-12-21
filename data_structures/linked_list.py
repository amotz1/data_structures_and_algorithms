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
        self.size = 0

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

    def find_link(self, value):
        return self._find_link(value)

    def add_head(self, value):
        new_link = _Link(value)
        if self._head is None:
            self._head = new_link
            self._tail = self._head
            self.size += 1
        else:
            new_link.set_next(self._head)
            self._head = new_link
            self.size += 1

    def add_link_after(self, link_to_add, value):
        link_to_find = self._find_link(value)
        if link_to_find == self._tail:
            new_link = _Link(link_to_add)
            self._tail.set_next(new_link)
            self._tail = new_link
            self.size += 1
        elif link_to_find != self._tail and link_to_find is not None:
            new_link = _Link(link_to_add)
            new_link.set_next(link_to_find.get_next())
            link_to_find.set_next(new_link)
            self.size += 1
        else:
            print(value, "is not in the list so you will better use an element that is in it")

    def add_tail(self, value):
        new_link = _Link(value)
        if self._head is None:
            self._head = new_link
            self._tail = self._head
            self.size += 1
        else:
            self._tail.set_next(new_link)
            self._tail = new_link
            new_link.set_next(None)
            self.size += 1

    def remove(self, value):
        link_to_find = self._find_link(value)
        if link_to_find == self._head:
            self._head = link_to_find.get_next()
            link_to_find.set_next(None)
            self.size -= 1
            return link_to_find.value
        elif link_to_find == self._tail:
            previous_link = self._head
            # doing a loop because i don't have prev pointers (its a linked_list)
            while previous_link.get_next() is not link_to_find:
                previous_link = previous_link.get_next()
            previous_link.set_next(None)
            self._tail = previous_link
            self.size -= 1
            return link_to_find.value
        elif link_to_find is not None:
            previous_link = self._head
            while previous_link.get_next() is not link_to_find:
                previous_link = previous_link.get_next()
            previous_link.set_next(link_to_find.get_next())
            link_to_find.set_next(None)
            self.size -= 1
            return link_to_find.value
        else:
            return None

    def compute_size(self):
        return self.size

    def check_invariant(self):
        if self._head is None:
            assert self._tail is None
        else:
            assert self._tail is not None

    def remove_head(self):
        if self.compute_size() > 1:
            link = self._head.get_next()
            temp = self._head
            self._head = link
            self.size -= 1
            return temp
        else:
            temp = self._head
            self._head = None
            self._tail = None
            self.size -= 1
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

