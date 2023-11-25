from math import e
from pytest import approx

from mne.roots.open_methods import root_nr, MAX_ITER


def f(x: float):
    return e ** (-x) - x


def test_root_nr():
    def f_prime(x):
        return -(e ** (-x)) - 1

    res = root_nr(f, f_prime, 0.0)
    # print(res.to_str())

    assert res.iterations < MAX_ITER
    assert approx(0.56714, 0.1) == res.xr
