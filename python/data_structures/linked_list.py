class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_



class LinkedList:
    """
    Put docstring here
    """

    def __init__(self, head=None, values=None):
        self.head = head
        if values:
            for value in reversed(values):
                self.insert(value)

    def __str__(self):
        string_values = ""
        if self.head is None:
            return f"NULL"
        while self.head is not None:
            string_values += f"{{ { self.head.value } }} -> "
            self.head = self.head.next
        string_values += "NULL"
        return string_values

    def insert(self, value):
        self.head = Node(value, self.head)
        # self.head = node

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False


class TargetError:
    pass
