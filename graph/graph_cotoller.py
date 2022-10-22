from abc import ABC
from graph.adjlist import AdjList


class Graph(AdjList, ABC):

    def shortest_path(self, src: str):
        """Dijkstra's Algorithm"""
        dist = {src: 0}  # hashmap for store distances
        path = {src}
        waiting = set(self.vertices)

        def is_visited(tgt: str):
            if dist[tgt] is not None:
                return True
            return False

        def min_distance(node: str, next_node: str, min_node: str = None):
            if next_node is None:
                return min_node

            if next_node not in waiting:
                next_node = self.vertices[next_node]
                return min_distance(node, self.vertices[next_node])

            new_distance = dist[node] + self.get_edge(node, next_node).size

            if is_visited(next_node):
                if dist[next_node] > new_distance:
                    dist[next_node] = new_distance
            else:
                dist[next_node] = new_distance

            if min_node is None or dist[min_node] > dist[next_node]:
                min_node = next_node

            return min_distance(node, self.vertices[next_node], min_node)

        while src in self.vertices:
            path.add(min_distance(src, self.vertices[src]))
            waiting.remove(src)

            src = self.vertices[src]

        return path, dist


