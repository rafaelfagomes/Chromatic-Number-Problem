# Módulo de Eventos
# Disponibiliza as operações para a criação e manipulação de eventos


# Implementação:
#   Data: tuple[int,str,int]
#   O float representa o tempo em que o evento deve ser realizado, a str representa o tipo do evento
#   O int representa o identificador do individuo associado ao evento


def new_event(time, kind, object_identifier=-1):
    return (time, kind, object_identifier)


def time(event):
    return event[0]


def kind(event):
    return event[1]


def object_identifier(event):
    return event[2]
