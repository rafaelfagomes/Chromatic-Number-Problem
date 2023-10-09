# Modulo de Exprandom
# Disponibiliza uma função para gerar observações de uma variavel aleatoria com distribuicao exponencial


# Implementação:
#   N/A
#
#

from random import random
from math import log


def exprandom(m: int) -> float:
    x = random()
    return -m * log(x)
