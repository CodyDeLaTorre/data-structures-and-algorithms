from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    if tree.root is None:
        return []

    queue = Queue()
    new_list = []
    queue.enqueue(tree.root)

    while not queue.is_empty():
        current = queue.dequeue()
        new_list.append(current.value)
        if current.left:
            queue.enqueue(current.left)
        if current.right:
            queue.enqueue(current.right)
    return new_list
