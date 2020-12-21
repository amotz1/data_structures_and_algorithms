from data_structures import linked_list


class Queue:
    def __init__(self):
        self.linked_list = linked_list.LinkedList()
        self.size = 0

    def push(self, value):
        self.linked_list.add_tail(value)
        self.size += 1

    def pop(self):
        element = self.linked_list.remove_head()
        self.size -= 1
        if self.compute_size() == -1:
            return None
        return element

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def create_copy_of_data(self):
        element_list = []
        for i in self.linked_list:
            element_list.append(i)
        return element_list

    def compute_size(self):
        return self.size


def test_queue():
    queue = Queue()
    for i in ['marshmelo', 'bamba', 'bisly']:
        queue.push(i)
    for i in ['marshmelo', 'bamba', 'bisly']:
        queue_element = queue.pop()
        assert queue_element.value == i
    assert queue.is_empty() is True
    assert queue.pop() is None




test_queue()