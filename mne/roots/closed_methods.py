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


def root_bisection(f: Function, x1: float, x2: float, rel_err: float = 0.01, iterations: int = MAX_ITER) -> float:
    res = RootResult()
    iter = 0
    res.root = 0

    while _rel_err(x2, x1) > rel_err and iter < iterations:
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
        iter += 1

    return res.root


def root_false_position(f: Function, x1: float, x2: float, rel_err: float = 0.01, iterations: int = MAX_ITER) -> float:
    return .0
    
