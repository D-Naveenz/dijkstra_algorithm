from abc import ABC, abstractmethod


class AdjacencyStruct(ABC):
    def __init__(self):
        self._edges = None
        self._vertices = None

    # PROPERTIES
    @property
    def no_of_edges(self):
        return len(self._edges)

    @property
    def no_of_vertices(self):
        return len(self._vertices)

    @property
    def get_vertices(self):
        return self._vertices

    @property
    def get_edges(self):
        return self._edges

    # PROPERTIES

    # GETTERS
    @abstractmethod
    def get_vertex(self, v):
        pass

    @abstractmethod
    def get_edge(self, src, dest):
        pass

    # GETTERS

    @abstractmethod
    def _create_vertex(self, v):
        pass

    @abstractmethod
    def _remove_vertex(self, v):
        pass

    @abstractmethod
    def add_node(self, v, loc=None):
        pass

    @abstractmethod
    def remove_node(self, loc, n):
        pass

    @abstractmethod
    def add_edge(self, src, dest, size):
        pass

    @abstractmethod
    def remove_edge(self, src, tgt):
        pass
