from collections.abc import Callable
from tabulate import tabulate

from mne.roots.common import ea

MAX_ITER = 10_000

Function = Callable[[float], float]


class OpenResult:
    def __init__(self) -> None:
        self.iterations = 0
        self.xr = 0
        self.xrs = []
        self.eas = []

    def to_str(self, xt: float | None = None) -> str:
        table = []
        if xt == None:
            for i, _ in enumerate(self.xrs):
                # table.append([i, self.xrs[i], self.eas[i]])
                table.append([i, self.xrs[i]])
        else:
            et = 0
            for i, _ in enumerate(self.xrs):
                et = abs((xt - self.xrs[i]) / xt) * 100
                table.append([i, self.xrs[i], self.eas[i], et])

        s = tabulate(table, headers=['i', 'xr', 'ea %', 'et %'], floatfmt='.4f')
        # s += '\n'+ repr(self.eas)
        return s + f'\n\nroot {self.xr}'


def root_nr(
    f: Function,
    fprime: Function,
    x0: float,
    rel_err: float = 0.01,
    max_iterations: int | None = None,
):
    """Método de Newton-Raphson"""

    if max_iterations == None:
        max_iterations = MAX_ITER

    res = OpenResult()
    xr = x0
    prev_xr = x0
    iter = 0
    _ea = 0

    while True:
        iter += 1
        prev_xr = xr
        xr = prev_xr - f(prev_xr) / fprime(prev_xr)
        res.xrs.append(xr)

        if xr != 0:
            _ea = ea(xr, prev_xr)

        if _ea < rel_err or iter >= max_iterations:
            break
        # if abs(xr - prev_xr) < rel_err or iter > interations:
        #     break

    res.iterations = iter
    res.xr = xr
    return res
