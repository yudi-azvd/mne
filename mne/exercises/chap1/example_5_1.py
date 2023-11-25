from math import exp

from mne.roots.closed_methods import root_bisection
from mne.roots.closed_methods_plot import plot_closed_result


def f(x: float) -> float:
    return 9.81 * 68.1 / x * (1 - exp(-10 * x / 68.1)) - 40


def main():
    res = root_bisection(f, 12, 16, _rel_err=0.5)
    print(res.to_str())
    plot_closed_result(res, step=0.05)


main()
