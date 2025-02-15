from __future__ import annotations

from collections import deque


class Node:
    def __init__(self, vertex: int, next: Node | None = None):
        self.__vertex = vertex
        self.__next = next

    @property
    def vertex(self) -> int:
        return self.__vertex

    @property
    def next(self) -> Node | None:
        return self.__next

    @next.setter
    def next(self, node: Node | None):
        self.__next = node


class UndirectedGraph:
    def __init__(self):
        self.__adjancency_list: dict[int, Node] = {}

    def add_edge(self, source_vertex: int, destination_vertex: int):
        source_node = Node(source_vertex)
        destination_node = Node(destination_vertex)

        source_node.next = self.__adjancency_list.get(destination_vertex)
        destination_node.next = self.__adjancency_list.get(source_vertex)

        self.__adjancency_list[source_vertex] = destination_node
        self.__adjancency_list[destination_vertex] = source_node

    def bfs(self, root: int):
        visited_nodes = []
        nodes_to_visit = deque([root])

        while nodes_to_visit:
            node_to_visit = nodes_to_visit.popleft()

            if node_to_visit in visited_nodes:
                continue

            visited_nodes.append(node_to_visit)

            node = self.__adjancency_list[node_to_visit]

            while node:
                nodes_to_visit.append(node.vertex)
                node = node.next

        print(visited_nodes)

    def dfs(self, root: int):
        visited_nodes = []

        def search(target: int):
            if target in visited_nodes:
                return

            visited_nodes.append(target)

            current_node = self.__adjancency_list[target]

            while current_node:
                search(current_node.vertex)
                current_node = current_node.next

        search(root)

        print(visited_nodes)

    def __str__(self):
        message = ''

        for vertex, node in self.__adjancency_list.items():
            if not node:
                continue

            message += f'{vertex} -> '

            next = node

            while next:
                if not next:
                    break

                message += f'{next.vertex}, '
                next = next.next

            message = message.rstrip(', ')
            message += '\n'

        return message


def main():
    graph = UndirectedGraph()

    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(3, 2)
    graph.add_edge(3, 1)
    graph.add_edge(5, 4)
    graph.add_edge(4, 2)
    graph.add_edge(7, 0)

    print(graph)

    graph.bfs(5)
    graph.dfs(5)


if __name__ == '__main__':
    main()
