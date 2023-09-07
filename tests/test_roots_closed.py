from pytest import approx

from mne.roots.closed_methods import root_bisection, MAX_ITER
from mne.functions import sqrt_of_2, sqrt_of_2_prime, sqrt_of_4


def test_root_bisection():
    assert approx(1.41406, 0.01) == root_bisection(sqrt_of_2, 0, 2)
    assert approx(1.41, 0.01) == root_bisection(sqrt_of_2, 0, 2)
    assert approx(1.41, 0.01) == root_bisection(sqrt_of_2, 0, 2)


def test_root_bisection_exact():
    assert approx(2, 0.1) == root_bisection(sqrt_of_4, 0.0, 4.0)
