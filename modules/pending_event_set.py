# Módulo de Cadeia de Acontecimentos Pendentes
# Disponibiliza as operações para a criação e manipulação de CAPs


# Implementação:
#   Data: list[Event]
#   A lista guarda todos os acontecimentos para ser realizados no futuro
#   Cada evento corresponde ao tipo definido em event.py


import event


def new_set():
    return []


def add_event(new_event, pes):
    new_event_time = event.time(new_event)
    found = False
    left = 0
    right = len(pes) - 1

    while not found and left <= right:
        mid = (left + right) // 2

        if mid == 0:
            found = True
        elif new_event_time >= event.time(
            pes[mid - 1]
        ) and new_event_time <= event.time(pes[mid]):
            found = True
        elif new_event_time < event.time(pes[mid]):
            right = mid - 1
        else:
            left = mid + 1

    if found:
        pes.insert(mid, new_event)
    else:
        pes = pes + [new_event]

    return pes


def del_event(pes):
    return pes[1:]


def next_event(pes):
    return pes[0]


def emptyQ(pes):
    return pes == []
