from adjlist import AdjNode, Edge, AdjList


class UndirectedGraph(AdjList):
    def __init__(self, edges: list[Edge]):
        super().__init__(edges)

    def add_edge(self, edge: Edge):
        # check source node already in there
        src_node = self.find_vertex_by_value(edge.src)
        if src_node is None:
            # add source node to the list
            src_node = self.add_node(edge.src)

        # search destination node whether exist or not
        des_node = self.find_vertex_by_value(edge.dest)
        if des_node is None:
            # add destination node to the list
            des_node = self.add_node(edge.dest, src_node)

        # Create the edge
        edge.src = src_node
        edge.dest = des_node

        # create a new edge for reverse the direction
        rev_edge = Edge(des_node, src_node)
        self._edges.append(rev_edge)

    def remove_edge(self, src: AdjNode, tgt: AdjNode):
        for i in self._edges:
            if i.src is src and i.dest is tgt:
                # delete edge directly from the edges list
                self._edges.remove(i)
            elif i.src is tgt and i.dest is src:
                # delete edge directly from the edges list
                self._edges.remove(i)
