from math import exp

from mne.roots.closed_methods import root_bisection
from mne.roots.closed_methods_plot import plot_closed_result
from mne.roots.plot import plot


def f(x: float) -> float:
    m = 82
    g = 9.81
    t = 4
    v = 36
    return g * m / x * (1 - exp(-t * x / m)) - v


x1 = 3
x2 = 5


def main():
    res = root_bisection(f, x1, x2, _rel_err=2)
    print(res.to_str())
    plot(f, x1, x2, 'img2.png')
    plot_closed_result(res)
    error = f(res.xr)
    print('error', error)


main()
