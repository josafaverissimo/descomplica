from collections import defaultdict, deque


class Node:
    def __init__(self, vertex: int):
        self.__vertex = vertex

    @property
    def vertex(self):
        return self.__vertex


class Edge:
    def __init__(self, source: Node, destination: Node, weight: int):
        self.source = source
        self.destination = destination
        self.weight = weight


class DirectedGraph:
    def __init__(self):
        self.__matrix: defaultdict[int, dict[int, Edge]] = defaultdict(dict)

    def add_edge(
        self,
        source_vertex: int,
        destination_vertex: int,
        weight: int = 1
    ):
        source = Node(source_vertex)
        destination = Node(destination_vertex)
        edge = Edge(source, destination, weight)

        self.__matrix[source_vertex][destination_vertex] = edge

    def bfs(self, root: int):
        visited_nodes = set()
        nodes_to_visit = deque([root])
        visits = ''

        while nodes_to_visit:
            visited_node = nodes_to_visit.popleft()

            if visited_node in visited_nodes:
                continue

            visits += f'{visited_node}, '

            visited_nodes.add(visited_node)

            edges = self.__matrix[visited_node]

            for destination_vertex in edges.keys():
                nodes_to_visit.append(destination_vertex)

        print(visits.rstrip(', '))

    def dfs(self, root: int):
        visited_nodes = set()
        nodes_to_visit = deque([root])
        visits = ''

        while nodes_to_visit:
            visited_node = nodes_to_visit.pop()

            if visited_node in visited_nodes:
                continue

            visits += f'{visited_node}, '

            visited_nodes.add(visited_node)

            edges = self.__matrix[visited_node]

            for destination_vertex in edges.keys():
                nodes_to_visit.append(destination_vertex)

        print(visits.rstrip(', '))

    def __str__(self):
        string = ''

        for source_vertex, edges in self.__matrix.items():
            if not edges:
                continue

            string += f'{source_vertex} => '

            for destination_vertex, edge in edges.items():
                string += f'{destination_vertex}, '

            string = string.rstrip(', ')
            string += '\n'

        return string


def main():
    graph = DirectedGraph()

    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)

    print(graph)
    graph.bfs(1)
    graph.dfs(1)


if __name__ == '__main__':
    main()
