import linked_list


class Queuo:
    def __init__(self):
        self.linked_list = linked_list.LinkedList()

    def push(self, link_value):
        self.linked_list.add_link_at_start(link_value)

    def pop(self):
        element = self.linked_list.remove(self.linked_list.get_last_link().value)
        return element

    def show_elements(self):
        element_list = []
        for i in self.linked_list:
            element_list.append(i)
        return element_list


def test_queue():
    queue = Queuo()
    for i in ['marshmelo', 'bamba', 'bisly']:
        queue.push(i)
    print(queue.show_elements())
    for i in ['bisly', 'bamba', 'marshmelo']:
        queue_element = queue.pop()
        print(queue_element)



test_queue()