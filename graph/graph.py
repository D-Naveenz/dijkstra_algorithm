from abc import ABC
from adjlist import AdjNode, AdjList


class Graph(AdjList, ABC):

    def shortest_path(self, start: int):
        """Dijkstra's Algorithm"""
        src = self.get_vertex_by_value(start)
        dist = {src: 0}  # hashmap for store distances
        path = {src}
        waiting = set(self._vertices)

        def is_visited(tgt: AdjNode):
            if dist[tgt] is not None:
                return True
            return False

        def min_distance(node: AdjNode, next_node: AdjNode, min_node: AdjNode = None):
            if next_node is None:
                return min_node

            if next_node not in waiting:
                next_node = next_node.next_node
                return min_distance(node, next_node.next_node)

            new_distance = dist[node] + self.get_edge(node.vertex, next_node.vertex).size

            if is_visited(next_node):
                if dist[next_node] > new_distance:
                    dist[next_node] = new_distance
            else:
                dist[next_node] = new_distance

            if min_node is None or dist[min_node] > dist[next_node]:
                min_node = next_node

            return min_distance(node, next_node.next_node, min_node)

        while src.next_node is not None:
            path.add(min_distance(src, src.next_node))
            waiting.remove(src)

            src = src.next_node

        return path, dist


