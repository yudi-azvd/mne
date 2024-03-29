from collections.abc import Callable
from tabulate import tabulate
from enum import Enum

from mne.roots.common import ea_alt, ea

MAX_ITER = 100_000

Function = Callable[[float], float]


class ClosedResult:
    f: Function
    xr: float = 0
    iterations: float = 0
    x1s: list[float] = []
    x2s: list[float] = []
    xrs: list[float] = []
    eas: list[float] = []

    def __init__(self) -> None:
        self.xr = 0
        self.iterations = 0
        self.x1s = []
        self.x2s = []
        self.xrs = []
        self.eas = []

    def to_str(self, xt: float | None = None) -> str:
        table = []
        if xt == None:
            for i, _ in enumerate(self.xrs):
                table.append([i, self.x1s[i], self.x2s[i], self.xrs[i], self.eas[i]])
        else:
            et = 0
            for i, _ in enumerate(self.xrs):
                et = abs((xt - self.xrs[i]) / xt) * 100
                table.append(
                    [i, self.x1s[i], self.x2s[i], self.xrs[i], self.eas[i], et]
                )

        s = tabulate(
            table, headers=['i', 'x1', 'x2', 'xr', 'ea %', 'et %'], floatfmt='.4f'
        )
        return s + f'\n\nroot {self.xr}'


class StopOption(Enum):
    ITERATIONS = 0
    REL_ERROR = 1


def should_stop(
    _ea: float, _rel_err: float, iter: int, max_iterations: int, option: StopOption
):
    if option == StopOption.REL_ERROR:
        return _ea < _rel_err or iter >= max_iterations
    return iter >= max_iterations


def root_bisection(
    f: Function,
    x1: float,
    x2: float,
    _rel_err: float = 0.01,
    max_iterations: int = MAX_ITER,
    option: StopOption = StopOption.REL_ERROR,
) -> ClosedResult:
    res = ClosedResult()
    res.xr = 0
    res.f = f
    # OPT:
    f1 = f(x1)

    while True:
        _ea = ea_alt(x1, x2)

        res.x1s.append(x1)
        res.x2s.append(x2)
        res.eas.append(_ea)

        res.xr = (x1 + x2) / 2
        # OPT:
        fr = f(res.xr)
        res.xrs.append(res.xr)

        # test = f(x1)*f(res.xr)
        # OPT:
        test = f1 * fr
        if test < 0:
            x2 = res.xr
        elif test > 0:
            x1 = res.xr
            # OPT:
            f1 = fr
        else:
            # FIXME: parece gambiarra
            if option == StopOption.REL_ERROR:
                res.eas.append(0)
                res.iterations += 1
                break

        res.iterations += 1
        if should_stop(_ea, _rel_err, res.iterations, max_iterations, option):
            break
    # FIXME: checar f(res.xr) != 0 e emitir alerta
    return res


def root_false_position(
    f: Function,
    x1: float,
    x2: float,
    x0: float = 0.0,
    _rel_err: float = 0.01,
    max_iterations: int = MAX_ITER,
    option: StopOption = StopOption.REL_ERROR,
) -> ClosedResult:
    """
    O intervalo [x1, x2] não diminui na mesma velocidade que no mét. bisseção.

    Ver exemplo `example_5_5.py`.

    Não funciona muito bem quando um dos limites é zero
    """

    res = ClosedResult()
    res.xr = 0
    res.f = f
    f1 = f(x1)
    f2 = f(x2)
    prev_xr = x0

    while True:
        res.x1s.append(x1)
        res.x2s.append(x2)

        res.xr = x2 - f2 * (x1 - x2) / (f1 - f2)

        fr = f(res.xr)
        res.xrs.append(res.xr)
        _ea = ea(res.xr, prev_xr)
        res.eas.append(_ea)

        prev_xr = res.xr

        test = f1 * fr
        if test < 0:
            x2 = res.xr
            f2 = fr
        elif test > 0:
            x1 = res.xr
            f1 = fr
        else:
            # FIXME: parece gambiarra
            if option == StopOption.REL_ERROR:
                res.eas.append(0)
                res.iterations += 1
                break

        res.iterations += 1
        if should_stop(_ea, _rel_err, res.iterations, max_iterations, option):
            break
    # FIXME: checar f(res.xr) != 0 e emitir alerta
    return res


def root_false_position_mod(
    f: Function,
    x1: float,
    x2: float,
    x0: float = 0.0,
    _rel_err: float = 0.01,
    max_iterations: int = MAX_ITER,
    option: StopOption = StopOption.REL_ERROR,
) -> ClosedResult:
    """
    Divide um dos limites (x1 x2) pela metade quando percebe que tá travado.
    """

    res = ClosedResult()
    res.xr = 0
    res.f = f
    prev_xr = x0
    # OPT:
    f1 = f(x1)
    f2 = f(x2)
    stuck_counter_1 = 0
    stuck_counter_2 = 0

    while True:
        res.x1s.append(x1)
        res.x2s.append(x2)

        res.xr = x2 - (f2 * (x1 - x2)) / (f1 - f2)

        fr = f(res.xr)
        res.xrs.append(res.xr)
        _ea = ea(res.xr, prev_xr)
        res.eas.append(_ea)

        prev_xr = res.xr

        test = f1 * fr
        if test < 0:
            x2 = res.xr
            f2 = f(x2)
            stuck_counter_2 = 0
            stuck_counter_1 += 1
            if stuck_counter_1 >= 2:
                f1 = f1 / 2
        elif test > 0:
            x1 = res.xr
            f1 = f(x1)
            stuck_counter_1 = 0
            stuck_counter_2 += 1
            if stuck_counter_2 >= 2:
                f2 = f2 / 2
        else:
            # FIXME: parece gambiarra
            if option == StopOption.REL_ERROR:
                res.eas.append(0)
                res.iterations += 1
                break

        res.iterations += 1
        if should_stop(_ea, _rel_err, res.iterations, max_iterations, option):
            break
    # FIXME: checar f(res.xr) != 0 e emitir alerta
    return res
