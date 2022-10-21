from abc import ABC, abstractmethod


class AdjNode:
    def __init__(self, vertex: int, size=None, next_node=None):
        self.vertex = vertex
        self.size = size
        self.next_node = next_node


class Edge:
    def __init__(self, src: int | AdjNode, dest: int | AdjNode, size=None):
        self.src = src
        self.dest = dest
        self.size = size


class AdjList(ABC):
    def __init__(self, edges: list[Edge]):
        self._edges: list[Edge] = edges
        self._vertices: list[AdjNode] = []

    @property
    def no_of_edges(self):
        return len(self._edges)

    @property
    def no_of_vertices(self):
        return len(self._vertices)

    def find_vertex_by_value(self, val):
        for i in self._vertices:
            if i.vertex is val:
                return i

        return None

    def get_edge(self, src: int, dest: int):
        for i in self._edges:
            if i.src.vertex is src and i.dest.vertex is dest:
                return i

        return None

    def create_vertex(self, v: AdjNode):
        self._vertices.append(v)

    def remove_vertex(self, v: AdjNode):
        tmp_val = v.vertex

        # delete vertex directly from the vertices list
        self._vertices.remove(v)

        # find the occurrences of the target vertex as a node in the list. and remove
        for i in self._vertices:
            self.remove_node(i, tmp_val)

    @abstractmethod
    def add_node(self, v: int, t: AdjNode = None):
        pass

    @abstractmethod
    def remove_node(self, src: AdjNode, tgt: int):
        pass

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

    def remove_edge(self, src: AdjNode, tgt: AdjNode):
        for i in self._edges:
            if i.src is src and i.dest is tgt:
                # delete edge directly from the edges list
                self._edges.remove(i)
