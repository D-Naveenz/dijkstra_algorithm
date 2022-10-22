from adjlist import AdjNode, Edge
from graph import Graph


class UndirectedGraph(Graph):
    def __init__(self):
        super().__init__()

    def add_edge(self, src: int, dest: int, size=None):
        # check source node already in there
        src_node = self.get_vertex_by_value(src)
        if src_node is None:
            # add source node to the list
            src_node = self.add_node(src)

        # search destination node whether exist or not
        des_node = self.get_vertex_by_value(dest)
        if des_node is None:
            # add destination node to the list
            des_node = self.add_node(dest, src_node)

        # Create the edge
        edge = Edge(src_node, des_node, size)
        self._edges.append(edge)

        # create a new edge for reverse the direction
        rev_edge = Edge(des_node, src_node, size)
        self._edges.append(rev_edge)

    def remove_edge(self, src: AdjNode, tgt: AdjNode):
        for i in self._edges:
            if i.src is src and i.dest is tgt:
                # delete edge directly from the edges list
                self._edges.remove(i)
            elif i.src is tgt and i.dest is src:
                # delete edge directly from the edges list
                self._edges.remove(i)
