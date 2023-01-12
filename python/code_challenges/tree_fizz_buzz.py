from data_structures.kary_tree import KaryTree


def fizz_buzz_tree(tree):
    new_tree = tree.clone()

    def fizz_buzz_list(node):
        if node.value % 3  == 0 and node.value % 5 == 0:
            node.value = "FizzBuzz"
        elif node.value % 3  == 0:
            node.value = "Fizz"
        elif  node.value % 5  == 0:
            node .value = "Buzz"
        else:
            node.value = str(node.value)

        for x in node.children:
            fizz_buzz_list(x)

    fizz_buzz_list(new_tree.root)
    return new_tree
