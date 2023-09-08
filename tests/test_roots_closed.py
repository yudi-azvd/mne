from pytest import approx

from mne.roots.closed_methods import root_bisection, StopOption
from mne.functions import sqrt_of_2, sqrt_of_4


def test_root_bisection():
    assert approx(1.41406, 0.01) == root_bisection(sqrt_of_2, 0, 2).xr
    assert approx(1.41, 0.01) == root_bisection(sqrt_of_2, 0, 2).xr
    assert approx(1.41, 0.01) == root_bisection(sqrt_of_2, 0, 2).xr


def test_root_bisection_stop_option():
    res = root_bisection(sqrt_of_2, 0, 2, iterations=3, option=StopOption.ITERATIONS)
    # print(res.xr)
    assert res.iterations == 3


def test_root_bisection_exact():
    assert approx(2, 0.1) == root_bisection(sqrt_of_4, 0.0, 4.0).xr
