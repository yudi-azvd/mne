from pytest import approx

from mne.roots.closed_methods import root_bisection, root_false_position, StopOption
from mne.functions import sqrt_of_2, sqrt_of_4


### Bisection


def test_bisection():
    assert approx(1.41406, 0.01) == root_bisection(sqrt_of_2, 0, 2).xr
    assert approx(1.41, 0.01) == root_bisection(sqrt_of_2, 0, 2).xr
    assert approx(1.41, 0.01) == root_bisection(sqrt_of_2, 0, 2).xr


def test_bisection_stop_option():
    res = root_bisection(sqrt_of_2, 0, 2, max_iterations=3, option=StopOption.ITERATIONS)
    # print(res.xr)
    assert res.iterations == 3


def test_bisection_exact():
    assert approx(2, 0.1) == root_bisection(sqrt_of_4, 0, 4).xr


### False position


def test_false_position():
    xr = root_false_position(sqrt_of_2, 0, 2).xr
    assert approx(1.41406, 0.01) == xr

    xr = root_false_position(sqrt_of_2, 0, 2).xr
    assert approx(1.41, 0.01) == xr
    
    xr = root_false_position(sqrt_of_2, 0, 2).xr
    assert approx(1.41, 0.01) == xr


def test_bisection_exact():
    xr = root_false_position(sqrt_of_4, 0, 4).xr
    assert approx(2, 0.1) == xr
