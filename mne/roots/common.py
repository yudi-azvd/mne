def ea(x: float, x_prev: float) -> float:
    """Erro aproximado relativo percentual"""
    return abs((x - x_prev) / x * 100.0)


def ea_alt(x1: float, x2: float):
    """Erro aproximado relativo percentual. Forma alternativa: x1 < x2

    ea = | (x2 - x1) / (x2 + x1) | * 100 %
    """
    return abs((x2 - x1) / (x2 + x1)) * 100.0
