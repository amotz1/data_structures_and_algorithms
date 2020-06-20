import linked_list


class Queue:
    def __init__(self):
        self.linked_list = linked_list.LinkedList()
        self.size1 = 0

    def push(self, value):
        self.linked_list.add_head(value)
        self.size1 += 1

    def pop(self):
        element = self.linked_list.remove_head()
        self.size1 -= 1
        return element

    def is_empty(self):
        if self.size1 == 0:
            return True
        else:
            return False

    def show_elements(self):
        element_list = []
        for i in self.linked_list:
            element_list.append(i.label)
        return element_list

    def size(self):
        return self.size1


def test_queue():
    queue = Queue()
    for i in ['marshmel1', 'bamba', 'bisly']:
        queue.push(i)
    for i in ['marshmelo', 'bamba', 'bisly']:
        queue_element = queue.pop()
        assert queue_element == i




# test_queue()