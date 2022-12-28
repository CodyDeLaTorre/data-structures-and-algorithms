class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class LinkedList:
    """
    Put docstring here
    def insert(self, value):
    new_node = Node(value)
    if not self.head:
        self.head = new_node
    current_node = self.head
    while current_node.next:
        current_node = current_node.next
    current_node.next = new_node
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
        string_values = ""
        # while self.head is not None:
        #     string_values += f"{{ { self.head.value } }} -> "
        #     self.head = self.head.next
        # string_values += "NULL"
        # return string_values
        for value in self:
            string_values += f"{{ {value} }} -> "

        return string_values + "NULL"

    def insert(self, value):
        self.head = Node(value, self.head)

    # def add_to_start(self, new_node):
    #     temp = self.Head
    #     self.Head = new_node
    #     new_node.next = temp
    #
    #     self.Count += 1
    #     if self.Count == 1:
    #         self.Tail = self.Head

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False


class TargetError:
    pass
