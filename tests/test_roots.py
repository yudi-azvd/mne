from pytest import approx

from mne.roots import root_bisection

def sqrt_of_2(x):
    return x*x - 2

def sqrt_of_4(x):
    return x*x - 4

def test_root_bisection():
    assert approx(1.41406, 0.01) == root_bisection(sqrt_of_2, 0, 2)
    assert approx(1.41, 0.01) == root_bisection(sqrt_of_2, 0, 2)
    assert approx(1.41, 0.01) == root_bisection(sqrt_of_2, 0, 2)

def test_root_bisection_exact():
    assert approx(2, 0.1) == root_bisection(sqrt_of_4, 0.0, 4.0)
