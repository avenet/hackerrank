class Node:
    def __init__(self):
        self.children = []
        self._depth = None

    def depth(self):
        if self._depth:
            return self._depth
        node_depth = 1 + sum(c.depth() for c in self.children)
        self._depth = node_depth
        return node_depth


n, m = map(int, raw_input().split())
edges = []
nodes = [None] * (n+1)

for edge in range(m):
    c, p = tuple(map(int, raw_input().split()))

    c_node = nodes[c]

    if not c_node:
        nodes[c] = Node()

    p_node = nodes[p]

    if not p_node:
        nodes[p] = Node()

    nodes[p].children.append(nodes[c])

    edges.append((nodes[c], nodes[p]))

result = 0

for node in nodes:
    if node and node.depth() % 2 == 0:
        result += 1

print result - 1
