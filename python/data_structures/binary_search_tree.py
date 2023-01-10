from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        #start pointer at root
        current = self.root

        while current:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                #if there is no space go left
                current = current.left

            else:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right

    def contains(self, value):
        def walk(value, root):
            if not root:
                return False
            return (
                root.value == value or walk(value, root.left) or walk(value, root.right)
            )
        return walk(value, self.root)


