# implementing Link and LinkedList


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


class LinkedList:
    def __init__(self):
        self.head_link = None

    def is_empty(self):
        return self.head_link is None

    def __find_link(self, link_value):
        link = self.head_link
        while link is not None:
            if link.get_data() == link_value:
                return link
            else:
                link = link.get_next()

    def add_link_at_start(self, link_value):
        new_link = Link(link_value)
        new_link.set_next(self.head_link)
        self.head_link = new_link

    def add_link_at_end(self, link_value):
        new_link = Link(link_value)
        if self.head_link is None:
            self.head_link = new_link
        else:
            link = self.head_link
            while link.get_next() is not None:
                link = link.get_next()
            link.set_next(new_link)

    def remove(self, link_value):
        link_to_find = self.__find_link(link_value)
        if link_to_find == self.head_link:
            self.head_link = link_to_find.get_next()
            link_to_find.set_next(None)
        else:
            previous_link = self.head_link
            while previous_link.get_next() is not link_to_find:
                previous_link = previous_link.get_next()
            previous_link.set_next(link_to_find.get_next())
            link_to_find.set_next(None)

    def traverse_Linked_List(self):
        link = self.head_link
        print("the values in the linked_list are:")
        while link is not None:
            print(link.link_value)
            link = link.get_next()

    def add_link_after_link(self, link_to_add, link_to_find):
        link_to_find = self.__find_link(link_to_find)
        new_link = Link(link_to_add)
        new_link.set_next(link_to_find.get_next())
        link_to_find.set_next(new_link)


def test_Linked_List():
    my_list = LinkedList()
    my_list.add_link_at_end("Yotam")
    assert (not my_list.is_empty())
    my_list.traverse_Linked_List()
    my_list.add_link_at_end("Amotz")
    my_list.traverse_Linked_List()
    my_list.add_link_at_end("Anat")
    my_list.traverse_Linked_List()
    my_list.add_link_at_start("hillel")
    my_list.traverse_Linked_List()
    my_list.remove("Amotz")
    my_list.traverse_Linked_List()
    my_list.add_link_after_link("Asaf", "Anat")
    my_list.traverse_Linked_List()


test_Linked_List()
