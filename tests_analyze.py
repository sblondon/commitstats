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
