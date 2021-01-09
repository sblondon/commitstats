import pprint

RUN_TESTS = False
DISPLAY_MAX_DEPTH = 2

class Node:

    def __init__(self, path, qty, index):
        self.path = path
        self.qty = qty
        self.index = index
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __eq__(self, other):
        return self.path == other.path and self.qty == other.qty

    def __hash__(self):
        return self.index

    def __repr__(self):
        return "<Node path={path} qty={qty} index={index}>".format(
            path=self.path, qty=self.qty, index=self.index)

    def __str__(self):
        return "{path} ({qty})".format(
            path=self.path, qty=self.qty)

    def contains_path(self, path):
        for child in self.children:
            if child.path == path:
                return child

    def pprint(self, depth=0):
        if depth > DISPLAY_MAX_DEPTH:
            return
        indent = "    " * depth
        print("{indent}{node}".format(node=self, indent=indent))
        if self.children:
            #print("{indent}et ses {nchildren} enfants:".format(
            #    nchildren=len(self.children), indent=indent))
            for child in sorted(self.children, key=lambda x: x.qty, reverse=True):
                child.pprint(depth + 1)


class Tree:

    def __init__(self):
        self.nroot = Node(".", 0, 0)
        self.all_nodes = [self.nroot]

    def pprint(self):
        print("Tree:")
        self.nroot.pprint()

    def add(self, path, qty):
        current_node = self.nroot
        for chunk_path in path:
            current_node.qty += qty
            node = current_node.contains_path(chunk_path)
            if not node:
                node = Node(chunk_path, 0, len(self.all_nodes))
                current_node.add_child(node)
                self.all_nodes.append(node)
            current_node = node
        current_node.qty = qty

def get_tree():
    tree = Tree()
    with open("stats.txt") as f:
        for line in f:
            qty, raw_path = line.split(" ", maxsplit=1)
            path = raw_path.strip().split("/")
            tree.add(path, int(qty))
    return tree


import unittest


class TestTree(unittest.TestCase):

    def test_first_added_node(self):
        tree = Tree()

        tree.add(["first"], 5)

        self.assertEqual(tree.nroot.qty, 5)
        self.assertEqual(tree.nroot.children[0], Node("first", 5, 0))

    def test_two_added_nodes(self):
        tree = Tree()

        tree.add(["a"], 3)
        tree.add(["b"], 4)

        self.assertEqual(
            tree.nroot.children,
            [Node("a", 3, 0), Node("b", 4, 1)])

    def test_multiples_nodes_in_one_call(self):
        tree = Tree()

        tree.add(["a", "b", "c"], 3)

        node_a = Node("a", 3, 0)
        node_b = Node("b", 3, 1)
        node_c = Node("c", 3, 2)
        self.assertEqual(tree.nroot.children[0], node_a)
        self.assertEqual(tree.nroot.children[0].children[0], node_b)
        self.assertEqual(tree.nroot.children[0].children[0].children[0], node_c)

    def test_multiples_nodes_on_existing_path(self):
        tree = Tree()

        tree.add(["a", "b", "c"], 3)
        tree.add(["a", "b", "d"], 4)

        node_a = Node("a", 3+4, 0)
        node_b = Node("b", 3+4, 1)
        node_c = Node("c", 3, 2)
        node_d = Node("d", 4, 3)
        self.assertEqual(tree.nroot.qty, 3+4)
        self.assertEqual(tree.nroot.children[0], node_a)
        self.assertEqual(tree.nroot.children[0].children[0], node_b)
        self.assertEqual(tree.nroot.children[0].children[0].children, [node_c, node_d])


if __name__ == '__main__':
    if RUN_TESTS:
        unittest.main()
    else:
        tree = get_tree()
        tree.pprint()
