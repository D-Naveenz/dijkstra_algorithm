from dataclasses import dataclass
from typing import Any

from graph.adj_abstract import AdjacencyStruct


@dataclass
class Edge:
    src: str
    dest: str
    size: Any


class AdjList(AdjacencyStruct):
    def __init__(self):
        super().__init__()
        self._edges: list[Edge] = []
        self._vertices: dict[str, list[str] | None] = {}  # key: vertex, value: next node

    def get_vertex(self, v: str):
        return self._vertices[v]

    def get_edge(self, src: str, dest: str):
        for i in self._edges:
            if i.src is src and i.dest is dest:
                return i

        return None

    def _create_vertex(self, v: str):
        self._vertices[v] = None

    def _remove_vertex(self, v: str):
        tmp_val = v

        # delete vertex directly from the vertices list
        self._vertices.pop(v)

        # find the occurrences of the target vertex as a node in the list. and remove
        for i in self._vertices:
            self.remove_node(i, tmp_val)

    def add_node(self, v: str, loc: str = None):
        if loc is None:
            # add the vertex to the node list as a new
            self._create_vertex(v)
        else:
            # link the new node
            if self._vertices[loc] is None:
                self._vertices[loc] = [v]
            else:
                self._vertices[loc].append(v)

    def remove_node(self, loc: str, n: str):
        # remove node from the list of source vertex
        self._vertices[loc].remove(n)
        # remove the edge
        self.remove_edge(loc, n)

    def add_edge(self, src, dest, size):
        pass

    def remove_edge(self, src, tgt):
        pass
