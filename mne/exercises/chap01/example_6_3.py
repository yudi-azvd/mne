from math import e
from mne.roots.open_methods import root_nr


def f(x: float):
    return e ** (-x) - x


def fprime(x: float):
    return -(e ** (-x)) - 1


res = root_nr(f, fprime, 0, max_iterations=5)
print(res.to_str())
