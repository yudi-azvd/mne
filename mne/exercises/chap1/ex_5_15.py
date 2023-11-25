from math import tanh, sqrt

from mne.roots.closed_methods import root_false_position_mod
from mne.roots.plot import plot


def f(H: float) -> float:
    term = sqrt(2 * 9.81 * H)
    return term * tanh(term * 2.5 / 8) - 5


x1 = 0.1
x2 = 10


def main():
    res = root_false_position_mod(f, x1, x2, _rel_err=1.0)
    print(res.to_str())
    plot(f, x1, x2)


main()
