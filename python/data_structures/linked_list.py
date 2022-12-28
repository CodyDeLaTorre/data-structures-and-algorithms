class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class LinkedList:
    """
    """

    def __init__(self, head=None, values=None):
        self.head = head
        if values:
            for value in reversed(values):
                self.insert(value)

    def __iter__(self):
        def value_generator():
            current = self.head

            while current:
                yield current.value

                current = current.next

        return value_generator()

    def __str__(self):
        current = self.head
        text = ""
        while current:
            node_string = "{ " + current.value + " } -> "
            text += node_string
            current = current.next
        return text + "NULL"
        # string_values = ""
        # for value in self:
        #     string_values += f"{{ {value} }} -> "
        # return string_values + "NULL"

    def insert(self, value):
        self.head = Node(value, self.head)

    def insert_before(self, before, value):
        current = self.head
        previous = None
        if current is None:
            raise TargetError
        while current.value is not before:
            previous = current
            current = current.next
            if current is None:
                raise TargetError
        new_node = Node(value)
        new_node.next = current
        if previous is not None:
            previous.next = new_node
        if previous is None:
            self.head = new_node

    def insert_after(self, after, value):
        current = self.head
        if current is None:
            raise TargetError
        while current.value is not after:
            current = current.next
            if current is None:
                raise TargetError
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, value):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)


class TargetError(Exception):
    pass
