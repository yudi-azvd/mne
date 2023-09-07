from collections.abc import Callable

MAX_ITER = 10_000

def _abs_err(a: float, b: float):
    return abs(a - b)

def _rel_err(a: float, b: float):
    return ((a - b) / (a + b))

Function = Callable[[float], float]

class RootResult:
    root: float = 0
    iterations: float = 0
    x1s: list[float] = []
    x2s: list[float] = []
    roots: list[float] = []

def root_bisection(f: Function, x1: float, x2: float, rel_err: float = 0.01, iterations: int = MAX_ITER) -> float:
    res = RootResult()
    iterations = 0
    res.root = 0

    while _rel_err(x2, x1) > rel_err and iterations < MAX_ITER:
        res.root = (x1 + x2)/2
    
        if f(res.root) == 0:
            return res.root
        if f(x1)*f(res.root) < 0:
            x2 = res.root
        else:
            x1 = res.root
        
        res.x1s.append(x1)
        res.x2s.append(x2)
        res.roots.append(res.root)
        iterations += 1

    return res.root