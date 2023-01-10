import pytest
from data_structures.binary_tree import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected


def test_max_val_2():
    tree = BinaryTree()
    tree.root = None

    actual = tree.find_maximum_value()
    expected = None

    assert actual == expected


def test_max_val_3():
    tree = BinaryTree()
    tree.root = Node(50)
    tree.root.left = Node(-154)
    tree.root.right = Node(200)

    actual = tree.find_maximum_value()
    expected = 200

    assert actual == expected
