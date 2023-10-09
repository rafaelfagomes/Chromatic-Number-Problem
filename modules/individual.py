# Módulo de Indivíduos
# Disponibiliza as operações para a criação e manipulação de indivíduos


# Implementação:
#   Data: list[float, colouring]
#   O float é o tempo em que o Individuo "nasceu"
#   O Any é qualquer objeto, de forma a que a cada individuo fique associado um objeto desse tipo


Individual = tuple[float, type]


def new_individual(age: float, core: type) -> Individual:
    return (age, core)


def age(current_time: float, individual: Individual) -> float:
    return current_time - individual[0]


def get_core(individual: Individual) -> type:
    return individual[1]


def update_core(individual: Individual, new_core: type) -> Individual:
    return (individual[0], new_core)
