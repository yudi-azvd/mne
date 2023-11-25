from math import log

from mne.roots.closed_methods import root_bisection, StopOption
from mne.roots.closed_methods_plot import plot_closed_result
from mne.roots.plot import plot


def f(x: float) -> float:
    return log(x * x) - 0.7


x1 = 0.5
x2 = 2


def main():
    res = root_bisection(f, x1, x2, max_iterations=3, option=StopOption.ITERATIONS)
    print(res.to_str())
    plot(f, x1, x2, 'img2.png')
    plot_closed_result(res)
    error = f(res.xr)
    print('error', error)


main()
