class Stack:

    def __init__(self, array_size):
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

    # this function is still here strictly for testing purposes and i will erase it soon
    def show_vertices_labels(self):
        array = []
        for i in self.array:
            array.append(i.label)
        return array

    # TODO a stack that dynamically change size
