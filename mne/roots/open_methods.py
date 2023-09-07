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

    def __init__(self) -> None:
        self.root = 0
        self.iterations = 0
        self.x1s = []
        self.x2s = []
        self.roots = []

    def __repr__(self) -> str:
        return '''
roots      {0} 
root       {1} 
iterations {2}'''.format(self.roots, self.root, self.iterations)

    

def root_nr(f: Function, fprime: Function, x0: float, abs_err: float = 0.01, interations: int = MAX_ITER):
    '''Método de Newton-Raphson'''
    res = RootResult()
    x = 0
    prev_x = x0
    iter = 0

    while abs(x - prev_x) > abs_err and iter < interations: 
        prev_x = x
        x = prev_x - f(prev_x)/fprime(prev_x)
        # FIXME: essa linha interrompe a condição de parada muito antes do que deveria
        iter += 1
        res.roots.append(x)

    res.iterations = iter
    res.root = x
    return res

