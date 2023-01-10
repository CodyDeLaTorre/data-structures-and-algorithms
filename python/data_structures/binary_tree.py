class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        self.root = None

    def pre_order(self, root=None, nodes=None):
        if root is None:
            root = self.root
        if nodes is None:
            nodes = []

        nodes.append(root.value)

        if root.left:
            self.pre_order(root.left, nodes)

        if root.right:
            self.pre_order(root.right, nodes)

        return nodes

    def post_order(self, root=None, nodes=None):
        if root is None:
            root = self.root
        if nodes is None:
            nodes = []
        if root.left:
            self.post_order(root.left, nodes)

        if root.right:
            self.post_order(root.right, nodes)

        nodes.append(root.value)

        print(nodes)

        return nodes

    def in_order(self, root=None, nodes=None):
        # method body here
        if root is None:
            root = self.root
        if nodes is None:
            nodes = []
        if root.left:
            self.in_order(root.left, nodes)
        nodes.append(root.value)
        if root.right:
            self.in_order(root.right, nodes)
        return nodes

    def find_maximum_value(self):
        if self.root is None:
            return None
        return max(self.post_order())


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

