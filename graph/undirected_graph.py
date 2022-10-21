from graph import AdjNode, Edge, AdjList


class UAdjNode(AdjNode):
    def __init__(self, vertex: int, size=None, next_node=None, prev_node=None):
        super().__init__(vertex, size, next_node)
        self.prev_node = prev_node


class UndirectedGraph(AdjList):
    def __init__(self, edges: list[Edge]):
        super().__init__(edges)

    def add_node(self, v: int, t: UAdjNode = None):
        new_node = UAdjNode(v)

        if t is None:
            # add the vertex to the node list as a new
            self.create_vertex(new_node)
        else:
            # search the last node of the selected path of the adjacency list
            while t.next_node is not None:
                t = t.next_node
            # link the new node
            t.next_node = new_node
            new_node.prev_node = t

        return new_node

    def remove_node(self, src: UAdjNode, tgt: int):
        start_ptr = src

        while src.next_node.vertex is tgt:
            if src is None:
                return

            src = src.next_node

        # Detach the target node from the linked list
        src.next_node = src.next_node.next_node
        src.next_node.next_node.prev_node = src
        # remove the edge
        self.remove_edge(start_ptr, src)
