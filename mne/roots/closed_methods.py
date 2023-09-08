from collections.abc import Callable
from tabulate import tabulate
from enum import Enum

MAX_ITER = 10_000

def _abs_err(a: float, b: float):
    return abs(a - b)

def _rel_err(a: float, b: float):
    '''a < b'''
    return abs((b - a) / (b + a))

Function = Callable[[float], float]

class ClosedResult:
    f: Function
    xr: float = 0
    iterations: float = 0
    x1s: list[float] = []
    x2s: list[float] = []
    xrs: list[float] = []
    rel_errs: list[float] = []

    def __init__(self) -> None:
        self.xr = 0
        self.iterations = 0
        self.x1s = []
        self.x2s = []
        self.xrs = []
        self.rel_errs = []

    def __repr__(self) -> str:
        table = []
        for i, _ in enumerate(self.xrs):
            table.append([i, self.xrs[i], self.x1s[i], self.x2s[i], self.rel_errs[i]])
        s = tabulate(table, headers=['i', 'root', 'x1', 'x2', 'rel e'], floatfmt='.4f')
        return s + f'\n\nroot {self.xr}'


class StopOption:
    ITERATIONS = 0
    REL_ERROR = 1

def check_stop(x1: float, x2: float, rel_err: float, iter: int, 
               iterations: int, option: StopOption
):
    if option == StopOption.REL_ERROR:
        return _rel_err(x2, x1) > rel_err and iter < iterations
    return iter < iterations
    

def root_bisection(f: Function, x1: float, x2: float, 
                   rel_err: float = 0.01, iterations: int = MAX_ITER, 
                   option: StopOption = StopOption.REL_ERROR
) -> ClosedResult:
    res = ClosedResult()
    res.xr = 0
    res.f = f
    iter = 0

    # while _rel_err(x2, x1) > rel_err and iter < iterations:
    while check_stop(x1, x2, rel_err, iter, iterations, option):
        res.x1s.append(x1)
        res.x2s.append(x2)
        res.rel_errs.append(_rel_err(x1, x2))

        res.xr = (x1 + x2)/2
        res.xrs.append(res.xr)
    
        if f(res.xr) == 0:
            return res
            
        if f(x1)*f(res.xr) < 0:
            x2 = res.xr
        else:
            x1 = res.xr
        
        iter += 1

    res.iterations = iter
    return res


def root_false_position(f: Function, x1: float, x2: float, rel_err: float = 0.01, iterations: int = MAX_ITER) -> ClosedResult:
    res = ClosedResult()
    return res
    
