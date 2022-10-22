from graph.adjlist import Edge
from graph.graph_cotoller import Graph


class UndirectedGraph(Graph):
    def __init__(self):
        super().__init__()

    def add_edge(self, src: str, dest: str, size=None):
        # check source node already in there
        if src not in self.vertices:
            # add source node to the list
            self.add_node(src)

        # search destination node whether exist or not
        if dest not in self.vertices:
            # add destination node to the list
            self.add_node(dest)

        # link them together
        self.add_node(dest, src)

        # Create the edge
        edge = Edge(src, dest, size)
        self._edges.append(edge)

        # create a new edge for reverse the direction
        rev_edge = Edge(dest, src, size)
        self._edges.append(rev_edge)

    def remove_edge(self, src: str, tgt: str):
        for i in self._edges:
            if i.src is src and i.dest is tgt:
                # delete edge directly from the edges list
                self._edges.remove(i)
            elif i.src is tgt and i.dest is src:
                # delete edge directly from the edges list
                self._edges.remove(i)
