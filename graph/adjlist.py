from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class Edge:
    src: str
    dest: str
    size: Any


class AdjList(ABC):
    def __init__(self):
        self._edges: list[Edge] = []
        self.vertices: dict[str, list[str] | None] = {}  # key: vertex, value: next node

    @property
    def no_of_edges(self):
        return len(self._edges)

    @property
    def no_of_vertices(self):
        return len(self.vertices)

    def get_edge(self, src: str, dest: str):
        for i in self._edges:
            if i.src is src and i.dest is dest:
                return i

        return None

    def _create_vertex(self, v: str):
        self.vertices[v] = None

    def _remove_vertex(self, v: str):
        tmp_val = v

        # delete vertex directly from the vertices list
        self.vertices.pop(v)

        # find the occurrences of the target vertex as a node in the list. and remove
        for i in self.vertices:
            self.remove_node(i, tmp_val)

    def add_node(self, v: str, t: str = None):
        if t is None:
            # add the vertex to the node list as a new
            self._create_vertex(v)
        else:
            # link the new node
            if self.vertices[t] is None:
                self.vertices[t] = [v]
            else:
                self.vertices[t].append(v)

    def remove_node(self, src: str, tgt: str):
        # remove node from the list of source vertex
        self.vertices[src].remove(tgt)
        # remove the edge
        self.remove_edge(src, tgt)

    @abstractmethod
    def add_edge(self, src: str, dest: str, size=None):
        pass

    @abstractmethod
    def remove_edge(self, src: str, tgt: str):
        pass
