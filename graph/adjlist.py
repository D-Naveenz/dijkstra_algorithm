from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class AdjNode:
    vertex: int
    next_node = None


@dataclass
class Edge:
    src: AdjNode
    dest: AdjNode
    size: Any


class AdjList(ABC):
    def __init__(self):
        self._edges: list[Edge] = []
        self._vertices: list[AdjNode] = []

    @property
    def no_of_edges(self):
        return len(self._edges)

    @property
    def no_of_vertices(self):
        return len(self._vertices)

    def get_vertex_by_value(self, val):
        for i in self._vertices:
            if i.vertex is val:
                return i

        return None

    def get_edge(self, src: int, dest: int):
        for i in self._edges:
            if i.src.vertex is src and i.dest.vertex is dest:
                return i

        return None

    def _create_vertex(self, v: AdjNode):
        self._vertices.append(v)

    def _remove_vertex(self, v: AdjNode):
        tmp_val = v.vertex

        # delete vertex directly from the vertices list
        self._vertices.remove(v)

        # find the occurrences of the target vertex as a node in the list. and remove
        for i in self._vertices:
            self.remove_node(i, tmp_val)

    def add_node(self, v: int, t: AdjNode = None):
        new_node = AdjNode(v)

        if t is None:
            # add the vertex to the node list as a new
            self._create_vertex(new_node)
        else:
            # search the last node of the selected path of the adjacency list
            while t.next_node is not None:
                t = t.next_node
            # link the new node
            t.next_node = new_node

        return new_node

    def remove_node(self, src: AdjNode, tgt: int):
        start_ptr = src

        while src.next_node.vertex is tgt:
            if src is None:
                return

            src = src.next_node

        # Detach the target node from the linked list
        src.next_node = src.next_node.next_node
        # remove the edge
        self.remove_edge(start_ptr, src)

    @abstractmethod
    def add_edge(self, src: int, dest: int, size=None):
        pass

    @abstractmethod
    def remove_edge(self, src: AdjNode, tgt: AdjNode):
        pass
