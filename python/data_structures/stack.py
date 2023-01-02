from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class Stack:
    """
    Put docstring here
    """

    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        try:
            return self.top.value
        except Exception as e:
            raise InvalidOperationError("Method not allowed on empty collection")

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False
