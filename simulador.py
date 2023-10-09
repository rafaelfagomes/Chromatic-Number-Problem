from math import pi, atan, e
from random import random

from modules.exprandom import exprandom


def sim(graph, initial_pop, end_t, threshold_t, rythm_t, filter_t):
    pop = population.new_population(initial_pop, graph)
    pes = pending_event_set.new_set()

    for identifier, _ in population.list_all(pop):
        eval_event = event.new_event(
            exprandom.exprandom(threshold_t), "eval", identifier
        )
        pes = pending_event_set.add_event(eval_event, pes)

        evol_event = event.new_event(exprandom.exprandom(rythm_t), "evol", identifier)
        pes = pending_event_set.add_event(evol_event, pes)

    initial_selec_event = event.new_event(filter_t, "selec")
    pes = pending_event_set.add_event(initial_selec_event, pes)

    current_event = pending_event_set.next_event()
    current_kind = event.kind(current_event)
    current_time = event.time(current_event)
    current_identifier = event.identifier(current_event)
    pes = pending_event_set.del_event(pes)

    while current_time < end_t:
        if current_kind == "eval":
            current_individual = population.get_individual(current_identifier, pop)
            eval_prob = 1 - (
                (pi / 2)
                * atan(
                    (1 + individual.adaptation_degree(current_individual))
                    ** (
                        1 + (8 / (1 + individual.age(current_time, current_individual)))
                    )
                )
            )

            if random() < eval_prob:
                pop = population.kill_individual(current_identifier)
            else:
                eval_event = event.new_event(
                    current_time + exprandom.exprandom(threshold_t),
                    "eval",
                    current_identifier,
                )
                pes = pending_event_set.add_event(eval_event, pes)
        elif current_kind == "evol":
            current_individual = population.get_individual(current_identifier, pop)
            evol_prob = 1 / (1 + (e ** (initial_pop - population.pop_size(pop)) / 10))

            if random() < evol_prob:
                pop = population.mutate_individual(current_identifier, current_time)
            else:
                pop = population.reproduce_individual(current_identifier, current_time)

            evol_event = event.new_event(
                current_time + exprandom.exprandom(rythm_t), "evol", current_identifier
            )
            pending_event_set.add_event(evol_event, pes)
        elif current_kind == "selec":
            for identifier, ind in population.list_all(pop):
                ind_colouring = individual.get_core(ind)

                if colouring.defects(ind_colouring) != 0:
                    pop = population.kill_individual(identifier)

            while population.pop_size(pop) > initial_pop * 3 / 2:
                lowest_identifier = population.lowest_adaptation(pop)
                population.kill_individual(lowest_identifier)

            selec_event = event.new_event(current_time + filter_t, "selec")
            pending_event_set.add_event(selec_event, pes)

        if pending_event_set.emptyQ(pes):
            current_time = end_t
        else:
            current_event = pending_event_set.next_event()
            current_kind = event.kind(current_event)
            current_time = event.time(current_event)
            current_identifier = event.identifier(current_event)
            pes = pending_event_set.del_event(pes)
