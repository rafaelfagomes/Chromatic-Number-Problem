from exprandom import exprandom
from colouring import Colouring
from event import Event
from graph import Graph
from individual import Individual
from pending_event_set import Pending_Event_Set
from population import Population


def simulate(
    base_graph: Graph,
    initial_pop: int,
    end_t: int,
    threshold_t: int,
    rythm_t: int,
    filter_t: int,
):
    pop = Population(initial_pop, 0, base_graph)
    pes = Pending_Event_Set()

    for identifier, _ in pop.list_all():
        initial_eval_event = Event(exprandom(threshold_t), "eval", identifier)
        pes.add_event(initial_eval_event)

        initial_evol_event = Event(exprandom(rythm_t)), "evol", identifier
        pes.add_event(initial_evol_event)

    initial_selec_event = Event(exprandom(filter_t, "selec"))
    pes.add_event(initial_selec_event)

    current_event = pes.next_event()
    current_kind = current_event.kind()
    current_time = current_event.time()
    current_identifier = current_event.identifier()
    pes.delete_event()

    while current_time < end_t:
        if current_kind == "eval" and pop.exists(current_identifier):
            pass
        elif current_kind == "evol" and pop.exists(current_identifier):
            pass
        elif current_kind == "selec":
            pass

        if pes.emptyQ():
            current_time = end_t
        else:
            current_event = pes.next_event()
            current_kind = current_event.kind()
            current_time = current_event.time()
            current_identifier = current_event.identifier()
            pes.delete_event()

    if not pop.emptyQ():
        _, prediction_individual = pop.highest_adaptation(base_graph)
        prediction_colouring = prediction_individual.get_core()
        prediction_colouring.show()
    else:
        print("Aww Man")
