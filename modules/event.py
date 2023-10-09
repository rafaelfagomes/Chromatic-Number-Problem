# Módulo de Eventos
# Disponibiliza as operações para a criação e manipulação de eventos


# Implementação:
#   Data: tuple[int,str,int]
#   O float representa o tempo em que o evento deve ser realizado, a str representa o tipo do evento
#   O int representa o identificador do individuo associado ao evento

Event = tuple[float, str, int]


def new_event(time: float, kind: str, object_identifier: int) -> Event:
    return (time, kind, object_identifier)


def time(event: Event) -> float:
    return event[0]


def kind(event: Event) -> str:
    return event[1]


def object_identifier(event: Event) -> int:
    return event[2]
