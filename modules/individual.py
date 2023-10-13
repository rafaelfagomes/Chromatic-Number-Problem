# Módulo de Indivíduos
# Disponibiliza as operações para a criação e manipulação de indivíduos


# Implementação:
#   Data: list[float, colouring]
#   O float é o tempo em que o Individuo "nasceu"
#   O Any é qualquer objeto, de forma a que a cada individuo fique associado um objeto desse tipo


def new_individual(creation_time, core):
    return (creation_time, core)


def age(current_time, individual):
    return current_time - individual[0]


def get_core(individual):
    return individual[1]
