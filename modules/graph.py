# Módulo de Grafos
# Disponibiliza as operações para a criação e manipulação de grafos


# Implementação:
#   Data: dict[int, set[int]]
#   Cada chave do dicionário corresponde a um nó
#   Cada valor do dicionário corresponde ao conjunto de nós a que a chave está ligada


def new_graph(nodes):
    return {node: set() for node in range(nodes)}


def add_edge(from_node, to_node, graph):
    graph[from_node].add(to_node)
    graph[to_node].add(from_node)

    return graph


def del_edge(from_node, to_node, graph):
    graph[from_node].discard(to_node)
    graph[to_node].discard(from_node)

    return graph


def neighbour_list(node, graph):
    return [x for x in graph[node]]


def dim(graph):
    return len(graph)
