from collections.abc import Callable

MAX_ITER = 10_000

def _abs_err(a: float, b: float):
    return abs(a - b)

def _rel_err(a: float, b: float):
    return ((a - b) / (a + b))

Function = Callable[[float], float]

def root_bisection(f: Function, x1: float, x2: float, rel_err: float = 0.01) -> float:
    iterations = 0
    root = 0

    while _rel_err(x2, x1) > rel_err and iterations < MAX_ITER:
        root = (x1 + x2)/2
    
        if f(root) == 0:
            return root
        if f(x1)*f(root) < 0:
            x2 = root
        else:
            x1 = root
        
        iterations += 1

    return root