''' Implementação de grafo com lista de adjacências '''

from typing import Collection, Optional


class Node:
    def __init__(self, vertex: int, next: Optional['Node']):
        self.vertex = vertex
        self.next = next


class Graph:
    def __init__(self, length: int, adjacency_list: list[Node | None]):
        self.length = length
        self.adjacency_list = adjacency_list


def print_graph(graph: Graph):
    for vertex, node in enumerate(graph.adjacency_list):
        if not node:
            continue

        print(f'Lista de adjacências do vértice {vertex}')

        next = node

        while next:
            print(f'-> {next.vertex}')
            next = next.next


def create_node(vertex: int, next: Node | None = None) -> Node:
    return Node(vertex, next)


def create_graph(vertices: int):
    adjacency_list: list[Node | None] = [None for _ in range(vertices)]

    return Graph(vertices, adjacency_list)


def add_edge(graph: Graph, source: int, destination: int):
    destination_node = create_node(destination)

    destination_node.next = graph.adjacency_list[source]

    graph.adjacency_list[source] = destination_node


def main():
    graph = create_graph(5)

    add_edge(graph, 0, 1)
    add_edge(graph, 0, 4)

    add_edge(graph, 1, 2)
    add_edge(graph, 1, 3)
    add_edge(graph, 1, 4)

    add_edge(graph, 2, 3)

    add_edge(graph, 3, 4)
    add_edge(graph, 3, 1)

    add_edge(graph, 4, 0)

    print_graph(graph)
    breakpoint()


if __name__ == '__main__':
    main()
