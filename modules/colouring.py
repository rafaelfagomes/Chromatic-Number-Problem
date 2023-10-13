# Módulo de Coloração
# Disponibiliza as operações para a criação e manipulação de colorações diferentes para um grafo


# Implementação:
#   Data: dict[int, int]
#   A chave representa um nó do grafo
#   O valor representa a cor associada a esse nó


import graph
from random import choice


def new_colouring(base_graph):
    colouring = (dict(), 0.0, 0)
    i = 0

    for node in range(graph.dim(base_graph)):
        colouring[0][node] = i
        i += 1

    colouring = _update_colouring_values(colouring, base_graph)

    return colouring


def _update_colouring_values(colouring, base_graph):
    final_colouring = list(colouring)
    defect_count = 0

    for node in colouring[0]:
        for neighbour in graph.neighbour_list(node, base_graph):
            if colouring[0][node] == colouring[0][neighbour]:
                defect_count += 1

    final_colouring[2] = defect_count // 2

    if final_colouring[2] == 0:
        final_colouring[1] = graph.dim(base_graph) / len(colour_list(colouring))
    else:
        final_colouring[1] = 1 / (1 + final_colouring[2])

    return (final_colouring[0], final_colouring[1], final_colouring[2])


def adaptation_degree(colouring):
    return colouring[1]


def defects(colouring):
    return colouring[2]


def mutate(colouring, base_graph):
    node = choice(colouring[0])
    colour = colouring[0][node]

    temp_colour = colour_list(colouring)
    if colour in temp_colour:
        temp_colour.remove(colour)

    new_colouring_list = [colouring[0].copy(), colouring[1], colouring[2]]

    if temp_colour != []:
        target_colour = choice(temp_colour)
        new_colouring_list[0][node] = target_colour

    new_colouring = tuple(new_colouring_list)

    new_colouring = _update_colouring_values(new_colouring, base_graph)

    if colouring[1] < new_colouring[1]:
        return new_colouring
    else:
        return tuple(list(colouring))


def colour_list(colouring):
    c_list = list()

    for node in colouring[0]:
        if colouring[0][node] not in c_list:
            c_list = c_list + [colouring[0][node]]

    return c_list


def show(colouring, base_graph, graphics=False):
    import networkx as nx
    import matplotlib.pyplot as plt

    graph_colours = [0 for _ in range(graph.dim(base_graph))]
    colour_dict = dict()

    for colour in colour_list(colouring):
        hex_value = _random_hex(colour)
        colour_dict[colour] = hex_value

    for colour in colour_dict:
        for x in colouring[0]:
            if colouring[0][x] == colour:
                graph_colours[x] = colour_dict[colour]

    G = nx.Graph(base_graph)
    pos = nx.shell_layout(G)

    nx.draw_networkx(
        G,
        pos,
        ax=None,
        with_labels=False,
        font_size=14,
        node_size=500,
        node_color=graph_colours,
    )
    print(colouring[0])
    if graphics:
        plt.show()
    return len(colour_list(colouring))


def _random_hex(seed):
    import random
    from math import floor

    random.seed(seed)
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f"]

    hexCode = "#"

    while len(hexCode) < 7:
        hexCode += str(digits[floor(random.random() * len(digits))])

    return hexCode
