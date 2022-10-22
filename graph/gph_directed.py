from graph.adj_abstract import AdjacencyStruct
from graph.adj_list import Edge
from graph.gph_abstract import GraphStruct


class DirectedGraph(GraphStruct):
    def __init__(self, struct: AdjacencyStruct, descript: str = "Directed Graph"):
        super().__init__(struct, descript)

    def add_edge(self, src, dest, size):
        # check source node already in there
        if src not in self._adj.get_vertices:
            # add source node to the list
            self._adj.add_node(src)

        # search destination node whether exist or not
        if dest not in self._adj.get_vertices:
            # add destination node to the list
            self._adj.add_node(dest)

        # connecting the node
        self._adj.add_node(dest, src)

        # Create the edge
        edge = Edge(src, dest, size)
        self._adj.get_edges.append(edge)

    def remove_edge(self, src, tgt):
        for i in self._adj.get_edges:
            if i.src is src and i.dest is tgt:
                # delete edge directly from the edges list
                self._adj.get_edges.remove(i)
