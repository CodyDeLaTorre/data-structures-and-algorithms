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
        string = ""
        while current is not None:
            string += "{ " + str(current.value) + " } -> "
            current = current.next
        return string + "NULL"

    def insert(self, value):
        self.head = Node(value, self.head)

    def insert_before(self, before, value):
        current = self.head
        previous = None
        try:
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
        except Exception as e:
            raise TargetError(e)

    def insert_after(self, after, value):
        current = self.head
        try:
            if current is None:
                raise TargetError
            while current.value is not after:
                current = current.next
                if current is None:
                    raise TargetError
            new_node = Node(value)
            new_node.next = current.next
            current.next = new_node
        except Exception as e:
            raise TargetError(e)

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

    def kth_from_end(self, k):
        if k < 0:
            raise TargetError()
        current = self.head
        ll_list = []
        try:
            while current is not None:
                ll_list.append(current.value)
                current = current.next
            return ll_list[-k - 1]
        except Exception as e:
            raise TargetError(e)


class TargetError(Exception):
    pass
