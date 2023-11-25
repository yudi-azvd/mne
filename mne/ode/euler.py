from collections.abc import Callable

Function = Callable[[float, float], float]


def euler(F: Function, x: float, t: float, h: float):
    return x + F(x, t) * h


# def heun(F: Function, x: float, t: float, h: float):
# return
