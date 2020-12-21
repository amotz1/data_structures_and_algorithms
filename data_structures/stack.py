class Stack:

    def __init__(self, array_size=1000):
        self.array = [None] * array_size
        self.top = -1
        self.size = 0

    def push(self, element):
        assert self.top != len(self.array) - 1, "the stack is full of elements"
        self.top = self.top + 1
        self.array[self.top] = element
        self.size += 1

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def pop(self):
        # return None if stack is empty
        while not self.is_empty():
            element = self.array[self.top]
            self.array[self.top] = None
            self.top = self.top - 1
            self.size -= 1
            return element
        return None

    def create_copy_of_data(self):
        element_list = []
        for i in self.array:
            if i is not None:
                element_list.append(i.label)
        return element_list


def test_stack():

    st = Stack()
    for element in [5, 3, 'hi', 'dina', 8]:
        st.push(element)
    for element in [8, 'dina', 'hi', 3, 5]:
        st_element = st.pop()
        assert st_element == element
    assert st.pop() is None


test_stack()

    # TODO a stack that dynamically change size
