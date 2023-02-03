from data_structures.binary_tree import BinaryTree


def tree_intersection(tree1, tree2):
    values1 = set(tree1.in_order())
    values2 = set(tree2.in_order())
    return values1 & values2
