class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        stringval = self.head
        string_values = ""
        while stringval is not None:
            string_values += f"{ { stringval.value} } -> "
            stringval = stringval.next
        string_values += "NULL"
        return string_values

    def insert(self, value):
        node = Node(value, self.head)
        self.head = node

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False


class TargetError:
    pass
