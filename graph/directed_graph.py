from graph.adjlist import Edge
from graph.graph_cotoller import Graph


class DirectedGraph(Graph):
    def __init__(self):
        super().__init__()

    def add_edge(self, src: str, dest: str, size=None):
        # check source node already in there
        if src in self.vertices:
            # add source node to the list
            self.add_node(src)

        # search destination node whether exist or not
        if dest in self.vertices:
            # add destination node to the list
            self.add_node(dest, src)

        # Create the edge
        edge = Edge(src, dest, size)
        self._edges.append(edge)

    def remove_edge(self, src: str, tgt: str):
        for i in self._edges:
            if i.src is src and i.dest is tgt:
                # delete edge directly from the edges list
                self._edges.remove(i)
