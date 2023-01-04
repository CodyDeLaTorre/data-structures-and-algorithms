from data_structures.stack import Stack


class PseudoQueue:

    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, value):
        if self.stack_2.top is not None:
            while self.stack_2 is not None:
                item = self.stack_2.pop()
                self.stack_1.push(item)
        self.stack_1.push(value)

    def dequeue(self):
        if self.stack_1.top is not None:
            while self.stack_1.top is not None:
                item = self.stack_1.pop()
                self.stack_2.push(item)
        result = self.stack_2.pop()
        return result

