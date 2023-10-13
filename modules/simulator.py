from math import pi, atan, e, floor
from random import random

from exprandom import exprandom
import colouring
import event
import graph
import individual as individual
import pending_event_set
import population


def sim(base_graph, initial_pop, end_t, threshold_t, rythm_t, filter_t):
    pop = population.new_population()
    pes = pending_event_set.new_set()

    for _ in range(initial_pop):
        individual_colouring = colouring.new_colouring(base_graph)
        new_individual = individual.new_individual(0, individual_colouring)
        pop, _ = population.add_individual(new_individual, pop)

    for identifier, _ in population.list_all(pop):
        initial_eval_event = event.new_event(exprandom(threshold_t), "eval", identifier)
        pes = pending_event_set.add_event(initial_eval_event, pes)

        intial_evol_event = event.new_event(exprandom(rythm_t), "evol", identifier)
        pes = pending_event_set.add_event(intial_evol_event, pes)

    initial_selec_event = event.new_event(filter_t, "selec")
    pes = pending_event_set.add_event(initial_selec_event, pes)

    current_event = pending_event_set.next_event(pes)
    current_kind = event.kind(current_event)
    current_time = event.time(current_event)
    current_identifier = event.object_identifier(current_event)
    pes = pending_event_set.del_event(pes)

    while current_time < end_t:
        if current_kind == "eval" and population.existsQ(current_identifier, pop):
            current_individual = population.get_individual(current_identifier, pop)
            current_colouring = individual.get_core(current_individual)
            eval_prob = 1 - (
                (2 / pi)
                * atan(
                    (1 + colouring.adaptation_degree(current_colouring))
                    ** (
                        1 + (8 / (1 + individual.age(current_time, current_individual)))
                    )
                )
            )

            if random() < eval_prob:
                pop = population.kill_individual(current_identifier, pop)
            else:
                eval_event = event.new_event(
                    current_time + exprandom(threshold_t),
                    "eval",
                    current_identifier,
                )
                pes = pending_event_set.add_event(eval_event, pes)

        elif current_kind == "evol" and population.existsQ(current_identifier, pop):
            current_individual = population.get_individual(current_identifier, pop)
            evol_prob = 1 / (1 + e ** ((initial_pop - population.size(pop)) / 10))

            if random() < evol_prob:
                pop = population.mutate_individual(
                    current_identifier, current_time, base_graph, pop
                )
            else:
                pop, new_identifier = population.reproduce_individual(
                    current_identifier, current_time, pop
                )

                reproduced_evol_event = event.new_event(
                    current_time + exprandom(rythm_t), "evol", new_identifier
                )
                pes = pending_event_set.add_event(reproduced_evol_event, pes)

            evol_event = event.new_event(
                current_time + exprandom(rythm_t), "evol", current_identifier
            )
            pes = pending_event_set.add_event(evol_event, pes)
        elif current_kind == "selec":
            for identifier, ind in population.list_all(pop):
                ind_colouring = individual.get_core(ind)

                if colouring.defects(ind_colouring) != 0:
                    pop = population.kill_individual(identifier, pop)

            three_half_initial = floor(initial_pop * 3 / 2)

            if population.size(pop) > three_half_initial:
                identifier_ordered_list = population.lowest_adaptation(pop)

                for _ in range(population.size(pop) - three_half_initial):
                    lowest_identifier = identifier_ordered_list[0][0]
                    identifier_ordered_list = identifier_ordered_list[:-1]
                    pop = population.kill_individual(lowest_identifier, pop)

            selec_event = event.new_event(current_time + filter_t, "selec")
            pes = pending_event_set.add_event(selec_event, pes)

        # print(current_time)
        if pending_event_set.emptyQ(pes):
            current_time = end_t
        else:
            current_event = pending_event_set.next_event(pes)
            current_kind = event.kind(current_event)
            current_time = event.time(current_event)
            current_identifier = event.object_identifier(current_event)
            pes = pending_event_set.del_event(pes)

    if not population.emptyQ(pop):
        prediction_list = population.highest_adaptation(pop)
        prediction_identifier = prediction_list[0][0]
        prediction_individual = population.get_individual(prediction_identifier, pop)
        prediction_coloring = individual.get_core(prediction_individual)
        return colouring.show(prediction_coloring, base_graph)
    else:
        print("Aww Man")


# Grafo de Petersen
# grafo = graph.new_graph(10)
# grafo = graph.add_edge(0, 1, grafo)
# grafo = graph.add_edge(0, 4, grafo)
# grafo = graph.add_edge(0, 5, grafo)
# grafo = graph.add_edge(1, 2, grafo)
# grafo = graph.add_edge(1, 6, grafo)
# grafo = graph.add_edge(2, 3, grafo)
# grafo = graph.add_edge(2, 7, grafo)
# grafo = graph.add_edge(3, 4, grafo)
# grafo = graph.add_edge(3, 8, grafo)
# grafo = graph.add_edge(4, 9, grafo)
# grafo = graph.add_edge(5, 7, grafo)
# grafo = graph.add_edge(5, 8, grafo)
# grafo = graph.add_edge(6, 8, grafo)
# grafo = graph.add_edge(6, 9, grafo)
# grafo = graph.add_edge(7, 9, grafo)

# grafo2 = graph.new_graph(3)
# grafo2 = graph.add_edge(0, 1, grafo2)
# grafo2 = graph.add_edge(1, 2, grafo2)
# grafo2 = graph.add_edge(2, 0, grafo2)

# grafo3 = graph.new_graph(10)

# sim(grafo, 1000, 100, 1, 1, 25)
# sim(grafo2, 1000, 100, 1, 1, 25)
# sim(grafo3, 1000, 100, 1, 1, 25)
