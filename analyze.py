import pprint

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


if __name__ == '__main__':
    tree = get_tree()
    tree.pprint()
