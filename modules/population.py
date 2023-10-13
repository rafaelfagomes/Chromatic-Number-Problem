# Módulo de População
# Disponibiliza as operações para a criação e manipulação de populações de indivíduos


# Implementação:
#   Data: list[tuple[int, Individual]]
#   A lista representa toda a população
#

import individual
import colouring


def new_population():
    return []


# Change indentifier
def add_individual(new_individual, population):
    if population == []:
        identifier = 0
    else:
        identifier = population[-1][0] + 1
    return population + [(identifier, new_individual)], identifier


def list_all(population):
    return population


def size(population):
    return len(population)


def emptyQ(population):
    return population == []


def existsQ(identifier, population):
    found = False
    left = 0
    right = len(population) - 1

    while not (found) and left <= right:
        mid = (left + right) // 2
        if identifier == population[mid][0]:
            found = True
        elif identifier < population[mid][0]:
            right = mid - 1
        else:
            left = mid + 1

    return found


def get_individual(identifier, population):
    found = False
    left = 0
    right = len(population) - 1

    while not (found) and left <= right:
        mid = (left + right) // 2
        if identifier == population[mid][0]:
            found = True
        elif identifier < population[mid][0]:
            right = mid - 1
        else:
            left = mid + 1

    if found:
        return population[mid][1]
    else:
        print("Não existe um individuo com esse identificador.")


def change_individual(identifier, new_individual, population):
    found = False
    left = 0
    right = len(population) - 1

    while not (found) and left <= right:
        mid = (left + right) // 2
        if identifier == population[mid][0]:
            found = True
        elif identifier < population[mid][0]:
            right = mid - 1
        else:
            left = mid + 1

    if found:
        population[mid] = (population[mid][0], new_individual)
        return population
    else:
        print("Não existe um individuo com esse identificador.")


def reproduce_individual(identifier, current_time, population):
    original = get_individual(identifier, population)
    original_core = individual.get_core(original)

    new_individual = individual.new_individual(current_time, original_core)

    return add_individual(new_individual, population)


def kill_individual(identifier, population):
    final = -1
    for i in range(len(population)):
        if population[i][0] == identifier:
            final = i

    population.pop(final)

    return population


def mutate_individual(identifier, current_time, base_object, population):
    original_individual = get_individual(identifier, population)
    original_core = individual.get_core(original_individual)

    mutated_core = colouring.mutate(original_core, base_object)
    new_time = current_time - individual.age(current_time, original_individual)
    mutated_individual = individual.new_individual(new_time, mutated_core)

    if not mutated_core == original_core:
        population = change_individual(identifier, mutated_individual, population)

    return population


def highest_adaptation(population):
    population_ordered_adaptation = population[:]

    population_ordered_adaptation.sort(
        key=lambda x: colouring.adaptation_degree(individual.get_core(x[1])),
        reverse=True,
    )

    return population_ordered_adaptation


def lowest_adaptation(population):
    population_ordered_adaptation_r = population[:]

    population_ordered_adaptation_r.sort(
        key=lambda x: colouring.adaptation_degree(individual.get_core(x[1]))
    )

    return population_ordered_adaptation_r
