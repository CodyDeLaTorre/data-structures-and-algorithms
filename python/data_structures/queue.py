from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.front is None:
            self.front = new_node
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.rear = new_node

    def dequeue(self):
        try:
            dequeued = self.front
            self.front = self.front.next
            return dequeued.value
        except Exception as e:
            raise InvalidOperationError(e)

    def peek(self):
        try:
            return self.front.value
        except Exception as e:
            raise InvalidOperationError(e)

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False
