from abc import ABC, abstractmethod
from typing import Iterator

from graph.adj_abstract import AdjacencyStruct


class GraphStruct(ABC):
    def __init__(self, struct: AdjacencyStruct, descript: str):
        self.descript = descript
        self._adj = struct

    @abstractmethod
    def add_edge(self, src, dest, size):
        pass

    @abstractmethod
    def remove_edge(self, src, tgt):
        pass

    def shortest_path(self, src: str):
        """Dijkstra's Algorithm"""
        dist = {src: 0}  # hashmap for store distances
        path = [src]
        waiting = set(self._adj.get_vertices)

        def is_visited(tgt: str):
            if tgt in dist:
                return True
            return False

        def max_distance(node: str, it: Iterator, max_node: str = None):
            # Anchor: if there is no next node then return the max node
            try:
                next_node = next(it)
            except StopIteration:
                return max_node

            # bypass method
            if next_node not in waiting:
                try:
                    next(it)
                except StopIteration:
                    return max_node
                return max_distance(node, it)

            new_distance = dist[node] + self._adj.get_edge(node, next_node).size

            # checking the current distance which can be minimum
            if is_visited(next_node):
                if dist[next_node] > new_distance:
                    dist[next_node] = new_distance
            else:
                dist[next_node] = new_distance

            # replacing the max node
            if max_node is None or dist[max_node] < dist[next_node]:
                max_node = next_node

            return max_distance(node, it, max_node)

        def min_distance():
            prev = None
            _min = None
            for i in path:
                if prev is None:
                    prev = i
                    continue

                tgt = self._adj.get_edge(prev, i)
                if _min is None:
                    _min = tgt.size
                elif _min > tgt.size:
                    _min = tgt.size

                prev = i

            return _min

        while src in waiting and self._adj.get_vertex(src) is not None:
            result = max_distance(src, iter(self._adj.get_vertex(src)))
            if result not in path:
                path.append(result)
            # removing the processed node from the waiting list
            waiting.remove(src)

            for x in self._adj.get_vertex(src):
                if x in waiting and is_visited(x):
                    src = x
                    break

        return path, int(min_distance())
