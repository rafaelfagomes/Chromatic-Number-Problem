# Módulo de Grafos
# Disponibiliza as operações para a criação e manipulação de grafos


# Implementação:
#   Data: dict[int, set[int]]
#   Cada chave do dicionário corresponde a um nó
#   Cada valor do dicionário corresponde ao conjunto de nós a que a chave está ligada


Graph = dict[int, set[int]]


def new_graph(nodes: int) -> dict[int, set[int]]:
    return {node: set() for node in range(nodes)}


def add_edge(from_node: int, to_node: int, graph: Graph) -> Graph:
    graph[from_node].add(to_node)
    graph[to_node].add(from_node)

    return graph


def del_edge(from_node: int, to_node: int, graph: Graph) -> Graph:
    graph[from_node].discard(to_node)
    graph[to_node].discard(from_node)

    return graph


def num_nodes(graph: Graph) -> int:
    return len(graph)


def copy_graph(graph: Graph) -> Graph:
    new_graph: Graph = dict()
    for node in graph:
        new_graph[node] = graph[node].copy()

    return new_graph
