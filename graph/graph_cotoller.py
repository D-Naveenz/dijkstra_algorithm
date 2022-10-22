from abc import ABC
from typing import Iterator

from graph.adjlist import AdjList


class Graph(AdjList, ABC):

    def shortest_path(self, src: str):
        """Dijkstra's Algorithm"""
        dist = {src: 0}  # hashmap for store distances
        path = [src]
        waiting = set(self.vertices)

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
                next(it)
                return max_distance(node, it)

            new_distance = dist[node] + self.get_edge(node, next_node).size

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

                tgt = self.get_edge(prev, i)
                if _min is None:
                    _min = tgt.size
                elif _min > tgt.size:
                    _min = tgt.size

                prev = i

            return _min

        while src in waiting and self.vertices[src] is not None:
            result = max_distance(src, iter(self.vertices[src]))
            if result not in path:
                path.append(result)
            # removing the processed node from the waiting list
            waiting.remove(src)

            for x in self.vertices[src]:
                if x in waiting and is_visited(x):
                    src = x
                    break

        return path, int(min_distance())
